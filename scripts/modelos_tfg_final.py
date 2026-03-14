"""
===========================================================================
  ESTIMACIÓN DE MODELOS DE PANEL — TFG Econometría de la Salud
  M1: 1 retardo espera  |  M2: 2 retardos espera
  M3: 1 retardo espera + gasto seguros anterior
  M1-U: Dummy umbral (>100d)  |  M3-U: Dummy umbral + gasto anterior
===========================================================================
"""

from pathlib import Path

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import warnings
warnings.filterwarnings("ignore")

from linearmodels.panel import PanelOLS, RandomEffects

BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_CSV = BASE_DIR / "data" / "datos_tfg_final.csv"
RUTA_MD  = BASE_DIR / "borradores" / "tablas_regresion.md"

def sep(titulo="", ancho=70):
    print("\n" + "═"*ancho)
    if titulo:
        print(f"  {titulo}")
        print("═"*ancho)

def stars(p):
    if p is None or (isinstance(p, float) and np.isnan(p)): return ""
    if p < 0.01: return "***"
    if p < 0.05: return "**"
    if p < 0.10: return "*"
    return ""

def fmt(val, dec=4):
    return "—" if (val is None or (isinstance(val, float) and np.isnan(val))) else f"{val:.{dec}f}"

def r2(m):
    """Devuelve R² overall (entre individuos y tiempo) para cualquier modelo de panel."""
    return getattr(m, 'rsquared_overall', m.rsquared)

md_lines = []
def md(line=""): md_lines.append(line)

# ═══════════════════════════════════════════════════════════════════════════════
# 0. CARGA Y PREPARACIÓN
# ═══════════════════════════════════════════════════════════════════════════════
sep("0. CARGA Y PREPARACIÓN DE DATOS")

df = pd.read_csv(RUTA_CSV)
df = df.sort_values(["ccaa", "ano"]).reset_index(drop=True)

# Renombramos para claridad
df["control_mayores"] = df["pob_65_pct"]
df["covid"]           = df["dummy_covid"]

# ── CREAR LAG DEL LOG GASTO EN SEGUROS REAL ──────────────────────────────────
df["log_g_seguros"] = np.log(df["g_seguros_real"])
df["log_g_seguros_lag1"] = df.groupby("ccaa")["log_g_seguros"].shift(1)
print(f"  Variable 'log_g_seguros_lag1' creada (log del gasto en seguros retardado)")

# ── CREAR LAG DE LA DUMMY DE ESPERA ALTA ─────────────────────────────────────
df["espera_alta_lag1"] = df.groupby("ccaa")["espera_alta"].shift(1)
print(f"  Variable 'espera_alta_lag1' creada (dummy espera alta retardada)")

# ── Variables por modelo ─────────────────────────────────────────────────────
# M1: 1 retardo de espera
VARS_M1 = ["log_pib_pc", "espera_lag1", "covid", "control_mayores"]

# M2: 2 retardos de espera
VARS_M2 = ["log_pib_pc", "espera_lag1", "espera_lag2", "covid", "control_mayores"]

# M3: 1 retardo de espera + log gasto seguros anterior (modelo dinámico)
VARS_M3 = ["log_pib_pc", "espera_lag1", "log_g_seguros_lag1", "covid", "control_mayores"]

# M1-U: Dummy umbral retardada en vez de espera lag
VARS_M1U = ["log_pib_pc", "espera_alta_lag1", "covid", "control_mayores"]

# M3-U: Dummy umbral retardada + log gasto seguros anterior
VARS_M3U = ["log_pib_pc", "espera_alta_lag1", "log_g_seguros_lag1", "covid", "control_mayores"]

# ── DataFrames por modelo (dropna según variables usadas) ────────────────────
def prepare_panel(df_orig, vars_modelo):
    """Prepara panel eliminando NAs y creando MultiIndex."""
    all_vars = vars_modelo + ["log_gasto_real"]
    df_clean = df_orig.dropna(subset=all_vars).copy()
    df_clean = df_clean.set_index(["ccaa", "ano"])
    return df_clean

df_m1  = prepare_panel(df, VARS_M1)
df_m2  = prepare_panel(df, VARS_M2)
df_m3  = prepare_panel(df, VARS_M3)
df_m1u = prepare_panel(df, VARS_M1U)
df_m3u = prepare_panel(df, VARS_M3U)

print(f"\n  Observaciones por modelo:")
print(f"    M1  (1 retardo espera)          : N = {len(df_m1)}")
print(f"    M2  (2 retardos espera)         : N = {len(df_m2)}")
print(f"    M3  (1 retardo + gasto ant.)    : N = {len(df_m3)}")
print(f"    M1-U (dummy umbral)             : N = {len(df_m1u)}")
print(f"    M3-U (dummy umbral + gasto ant.): N = {len(df_m3u)}")

print(f"\n  CCAA total: {df['ccaa'].nunique()}")
print(f"  Años: {sorted(df['ano'].unique())}")

# ── Markdown header ──────────────────────────────────────────────────────────
md("# Resultados de las Regresiones de Panel — TFG Econometría de la Salud\n")
md(f"**Variable dependiente:** `log_gasto_real` (Log Gasto Real en Seguros Privados, €pp)  ")
md(f"**Período:** 2016–2024  |  **17 CCAA** (con datos faltantes)  ")
md(f"**Errores estándar:** Robustos cluster por CCAA  \n")
md("---\n")

# ═══════════════════════════════════════════════════════════════════════════════
# HELPER: extraer coeficientes
# ═══════════════════════════════════════════════════════════════════════════════
def extract_results(res, varnames):
    """Devuelve dict {var: (coef, se, tstat, pval)} para las variables pedidas."""
    out = {}
    for v in varnames:
        if v in res.params.index:
            c  = res.params[v]
            se = res.std_errors[v]
            t  = res.tstats[v]
            p  = res.pvalues[v]
            out[v] = (c, se, t, p)
        else:
            out[v] = (np.nan, np.nan, np.nan, np.nan)
    return out

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 1 — FE y RE (1 retardo de espera)
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 1 — 1 RETARDO DE ESPERA (FE & RE)")
md("## Modelo 1: Especificación con 1 retardo de espera\n")
md("$$\\log(\\text{gasto})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib\\_pc})_{it} + \\beta_2 \\text{espera}_{i,t-1} + \\beta_3 \\text{covid}_{it} + \\beta_4 \\text{pob65}_{it} + \\varepsilon_{it}$$\n")

# Añadir constante a las exógenas
X_fe1 = sm.add_constant(df_m1[VARS_M1])

fe1 = PanelOLS(
    dependent=df_m1["log_gasto_real"],
    exog=X_fe1,
    entity_effects=True
).fit(cov_type="clustered", cluster_entity=True)

re1 = RandomEffects(
    dependent=df_m1["log_gasto_real"],
    exog=X_fe1
).fit(cov_type="robust")

coef_fe1 = extract_results(fe1, ["const"] + VARS_M1)
coef_re1 = extract_results(re1, ["const"] + VARS_M1)

print(f"\n  ── Efectos Fijos (M1-FE) ──  N = {int(fe1.nobs)}")
print(f"  {'Variable':22s}  {'Coef':>10}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe1.items():
    print(f"  {v:22s}  {c:+10.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"  R² within = {fe1.rsquared:.4f}   R² overall = {r2(fe1):.4f}")

print(f"\n  ── Efectos Aleatorios (M1-RE) ──  N = {int(re1.nobs)}")
for v in ["const"] + VARS_M1:
    c, se, t, p = coef_re1[v]
    print(f"  {v:22s}  {c:+10.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"  R² overall = {r2(re1):.4f}")

# ── TEST DE HAUSMAN ──────────────────────────────────────────────────────────
sep("  TEST DE HAUSMAN — M1")
md("### Test de Hausman: FE vs RE\n")

b_fe = np.array([fe1.params[v] for v in VARS_M1])
b_re = np.array([re1.params[v] for v in VARS_M1])
V_fe = fe1.cov.loc[VARS_M1, VARS_M1].values
V_re = re1.cov.loc[VARS_M1, VARS_M1].values
diff = b_fe - b_re
V_diff = V_fe - V_re
V_diff_sym = (V_diff + V_diff.T) / 2

try:
    eigvals = np.linalg.eigvalsh(V_diff_sym)
    if np.all(eigvals > 0):
        V_inv = np.linalg.inv(V_diff_sym)
    else:
        V_inv = np.linalg.pinv(V_diff_sym)
except:
    V_inv = np.linalg.pinv(V_diff_sym)

H_stat = float(diff @ V_inv @ diff)
k = len(VARS_M1)
H_pval = 1 - stats.chi2.cdf(H_stat, df=k)

print(f"\n  Hausman χ²({k}) = {H_stat:.4f}   p-value = {H_pval:.4f} {stars(H_pval)}")
MODELO_PREFERIDO = "FE" if H_pval < 0.05 else "RE"
hausman_decision = f"Se prefiere **{MODELO_PREFERIDO}**" + (" (RE consistente)" if MODELO_PREFERIDO == "RE" else " (FE consistente)")
print(f"  Conclusión: {hausman_decision}")

md(f"| Estadístico | gl | p-value | Decisión |\n|-------------|----|---------|---------|\n")
md(f"| χ² = {H_stat:.4f} | {k} | {H_pval:.4f}{stars(H_pval)} | {hausman_decision} |\n")

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 2 — 2 RETARDOS DE ESPERA
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 2 — 2 RETARDOS DE ESPERA (FE)")
md("---\n## Modelo 2: Especificación con 2 retardos de espera\n")
md("$$\\log(\\text{gasto})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib})_{it} + \\beta_2 \\text{espera}_{i,t-1} + \\beta_3 \\text{espera}_{i,t-2} + \\beta_4 \\text{covid}_{it} + \\beta_5 \\text{pob65}_{it} + \\varepsilon_{it}$$\n")

# Añadir constante a las exógenas
X_fe2 = sm.add_constant(df_m2[VARS_M2])

fe2 = PanelOLS(
    dependent=df_m2["log_gasto_real"],
    exog=X_fe2,
    entity_effects=True
).fit(cov_type="clustered", cluster_entity=True)

coef_fe2 = extract_results(fe2, ["const"] + VARS_M2)

print(f"\n  ── M2-FE ──  N = {int(fe2.nobs)}")
print(f"  {'Variable':22s}  {'Coef':>10}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe2.items():
    print(f"  {v:22s}  {c:+10.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"  R² within = {fe2.rsquared:.4f}   R² overall = {r2(fe2):.4f}")

# ── TEST DE WALD: significatividad conjunta de espera_lag1, espera_lag2 ──────
sep("  TEST DE WALD — Retardos conjuntos")
md("### Test de Wald: β(lag1) = β(lag2) = 0\n")

# Crear lista de variables con constante para el test
VARS_M2_full = ["const"] + VARS_M2
idx_lag1 = VARS_M2_full.index("espera_lag1")
idx_lag2 = VARS_M2_full.index("espera_lag2")
R = np.zeros((2, len(VARS_M2_full)))
R[0, idx_lag1] = 1
R[1, idx_lag2] = 1

b = np.array([fe2.params[v] for v in VARS_M2_full])
V = fe2.cov.loc[VARS_M2_full, VARS_M2_full].values
Rb = R @ b
RVR = R @ V @ R.T
try:
    wald_stat = float(Rb @ np.linalg.inv(RVR) @ Rb)
except:
    wald_stat = float(Rb @ np.linalg.pinv(RVR) @ Rb)
wald_pval = 1 - stats.chi2.cdf(wald_stat, df=2)

print(f"\n  Wald χ²(2) = {wald_stat:.4f}   p-value = {wald_pval:.4f} {stars(wald_pval)}")
wald_dec = "Significativos conjuntamente" if wald_pval < 0.05 else "No significativos conjuntamente"
print(f"  Conclusión: {wald_dec}")

md(f"| Test | χ²(2) | p-value | Decisión |\n|------|-------|---------|----------|\n")
md(f"| Wald | {wald_stat:.4f} | {wald_pval:.4f}{stars(wald_pval)} | {wald_dec} |\n")

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 3 — 1 RETARDO ESPERA + LOG GASTO SEGUROS ANTERIOR (DINÁMICO)
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 3 — 1 RETARDO ESPERA + LOG GASTO SEGUROS ANTERIOR (FE)")
md("---\n## Modelo 3: 1 retardo espera + Log Gasto en seguros del año anterior\n")
md("$$\\log(\\text{gasto})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib})_{it} + \\beta_2 \\text{espera}_{i,t-1} + \\rho \\log(\\text{gasto})_{i,t-1} + \\beta_3 \\text{covid}_{it} + \\beta_4 \\text{pob65}_{it} + \\varepsilon_{it}$$\n")

# Añadir constante a las exógenas
X_fe3 = sm.add_constant(df_m3[VARS_M3])

fe3 = PanelOLS(
    dependent=df_m3["log_gasto_real"],
    exog=X_fe3,
    entity_effects=True
).fit(cov_type="clustered", cluster_entity=True)

coef_fe3 = extract_results(fe3, ["const"] + VARS_M3)

print(f"\n  ── M3-FE ──  N = {int(fe3.nobs)}")
print(f"  {'Variable':22s}  {'Coef':>10}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe3.items():
    print(f"  {v:22s}  {c:+10.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"  R² within = {fe3.rsquared:.4f}   R² overall = {r2(fe3):.4f}")

# Interpretación persistencia (ahora es elasticidad porque está en log)
rho_seguros = fe3.params.get("log_g_seguros_lag1", np.nan)
p_seguros = fe3.pvalues.get("log_g_seguros_lag1", np.nan)
print(f"\n  ► Coef. log gasto anterior (elasticidad) = {rho_seguros:.4f}{stars(p_seguros)}")
if not np.isnan(p_seguros) and p_seguros < 0.05:
    print(f"    Indica fuerte inercia/persistencia en el gasto privado")

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 1-U — DUMMY UMBRAL (>100 días)
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 1-U — DUMMY UMBRAL (>100 días)")
md("---\n## Modelo 1-U: Especificación con dummy umbral (espera > 100 días)\n")
md("$$\\log(\\text{gasto})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib})_{it} + \\beta_2 \\mathbf{1}_{\\text{espera}>100} + \\beta_3 \\text{covid}_{it} + \\beta_4 \\text{pob65}_{it} + \\varepsilon_{it}$$\n")

# Añadir constante a las exógenas
X_fe1u = sm.add_constant(df_m1u[VARS_M1U])

fe1u = PanelOLS(
    dependent=df_m1u["log_gasto_real"],
    exog=X_fe1u,
    entity_effects=True
).fit(cov_type="clustered", cluster_entity=True)

coef_fe1u = extract_results(fe1u, ["const"] + VARS_M1U)

print(f"\n  ── M1-U (FE) ──  N = {int(fe1u.nobs)}")
print(f"  {'Variable':22s}  {'Coef':>10}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe1u.items():
    print(f"  {v:22s}  {c:+10.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"  R² within = {fe1u.rsquared:.4f}   R² overall = {r2(fe1u):.4f}")

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 3-U — DUMMY UMBRAL + LOG GASTO SEGUROS ANTERIOR
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 3-U — DUMMY UMBRAL + LOG GASTO SEGUROS ANTERIOR")
md("---\n## Modelo 3-U: Dummy umbral + Log Gasto en seguros anterior\n")
md("$$\\log(\\text{gasto})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib})_{it} + \\beta_2 \\mathbf{1}_{\\text{espera}>100} + \\rho \\log(\\text{gasto})_{i,t-1} + \\beta_3 \\text{covid}_{it} + \\beta_4 \\text{pob65}_{it} + \\varepsilon_{it}$$\n")

# Añadir constante a las exógenas
X_fe3u = sm.add_constant(df_m3u[VARS_M3U])

fe3u = PanelOLS(
    dependent=df_m3u["log_gasto_real"],
    exog=X_fe3u,
    entity_effects=True
).fit(cov_type="clustered", cluster_entity=True)

coef_fe3u = extract_results(fe3u, ["const"] + VARS_M3U)

print(f"\n  ── M3-U (FE) ──  N = {int(fe3u.nobs)}")
print(f"  {'Variable':22s}  {'Coef':>10}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe3u.items():
    print(f"  {v:22s}  {c:+10.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"  R² within = {fe3u.rsquared:.4f}   R² overall = {r2(fe3u):.4f}")

# ═══════════════════════════════════════════════════════════════════════════════
# TABLA COMPARATIVA — 5 MODELOS
# ═══════════════════════════════════════════════════════════════════════════════
sep("TABLA COMPARATIVA — 5 MODELOS")
md("\n---\n## Tabla Comparativa\n")

MODELS      = [fe1, re1, fe2, fe3, fe1u, fe3u]
MODEL_NAMES = ["M1-FE", "M1-RE*", "M2-FE", "M3-FE", "M1-U", "M3-U"]
MODEL_VARS  = [["const"] + VARS_M1, ["const"] + VARS_M1, ["const"] + VARS_M2, 
               ["const"] + VARS_M3, ["const"] + VARS_M1U, ["const"] + VARS_M3U]

ALL_VARS = ["const", "log_pib_pc", "espera_lag1", "espera_lag2", "espera_alta_lag1",
            "log_g_seguros_lag1", "covid", "control_mayores"]
VAR_LABELS = {
    "const"              : "Constante",
    "log_pib_pc"         : "Log PIB pc",
    "espera_lag1"        : "Espera esp. (lag 1)",
    "espera_lag2"        : "Espera esp. (lag 2)",
    "espera_alta_lag1"   : "Dummy espera > 100d (t-1)",
    "log_g_seguros_lag1" : "Log Gasto seguros (t-1)",
    "covid"              : "Dummy COVID-19",
    "control_mayores"    : "Pob. > 65 años (%)",
}

# Markdown table
md("| Variable | M1-FE | M1-RE* | M2-FE | M3-FE | M1-U | M3-U |")
md("|----------|-------|--------|-------|-------|------|------|")

for v in ALL_VARS:
    row = f"| {VAR_LABELS.get(v, v)} |"
    for m, mvars in zip(MODELS, MODEL_VARS):
        if v in mvars:
            c = m.params[v]
            p = m.pvalues[v]
            row += f" {c:+.4f}{stars(p)} |"
        else:
            row += " — |"
    md(row)

md("")
md("| **Estadísticos** |  |  |  |  |  |  |")
row_n = "| N |"
row_r2 = "| R² overall |"
for m in MODELS:
    row_n += f" {int(m.nobs)} |"
    row_r2 += f" {r2(m):.4f} |"
md(row_n)
md(row_r2)

md("\n*Nota: * indica modelo preferido por test de Hausman. Errores robustos cluster.*")

# Console table
W = 12
print(f"\n  {'Variable':24s}" + "".join(f"{n:>{W}}" for n in MODEL_NAMES))
print("  " + "─"*(24 + W*len(MODELS)))
for v in ALL_VARS:
    row = f"  {VAR_LABELS.get(v, v):24s}"
    for m, mvars in zip(MODELS, MODEL_VARS):
        if v in mvars:
            c = m.params[v]
            p = m.pvalues[v]
            coef_str = f"{c:+.4f}"[:9] + stars(p).ljust(3)
            row += f"{coef_str:>{W}}"
        else:
            row += f"{'—':>{W}}"
    print(row)

print("  " + "─"*(24 + W*len(MODELS)))
print(f"  {'N':24s}" + "".join(f"{int(m.nobs):>{W}}" for m in MODELS))
print(f"  {'R² overall':24s}" + "".join(f"{r2(m):>{W}.4f}" for m in MODELS))

# ═══════════════════════════════════════════════════════════════════════════════
# RESUMEN DE HIPÓTESIS
# ═══════════════════════════════════════════════════════════════════════════════
sep("RESUMEN DE HIPÓTESIS")
md("\n---\n## Resumen de Hipótesis\n")

# H1: Nivel de renta (log_pib_pc) → signo esperado +
c_pib = fe1.params["log_pib_pc"]
p_pib = fe1.pvalues["log_pib_pc"]
h1_result = "Confirmada" if c_pib > 0 and p_pib < 0.05 else "No confirmada"
print(f"  H1 (Renta → +): coef = {c_pib:+.4f}{stars(p_pib)}  →  {h1_result}")

# H2: Lista de espera (espera_lag1) → signo esperado +
c_esp = fe1.params.get("espera_lag1", np.nan)
p_esp = fe1.pvalues.get("espera_lag1", np.nan)
h2_result = "Confirmada" if c_esp > 0 and p_esp < 0.05 else "Parcialmente confirmada (signo correcto)" if c_esp > 0 else "No confirmada"
print(f"  H2 (Espera → +): coef = {c_esp:+.4f}{stars(p_esp)}  →  {h2_result}")

# H3: COVID → signo esperado ambiguo o +
c_cov = fe1.params["covid"]
p_cov = fe1.pvalues["covid"]
h3_result = "Confirmada" if p_cov < 0.05 else "No significativo"
print(f"  H3 (COVID): coef = {c_cov:+.4f}{stars(p_cov)}  →  {h3_result}")

# H4: Umbral (espera_alta_lag1) → signo esperado +
c_umb = fe1u.params.get("espera_alta_lag1", np.nan)
p_umb = fe1u.pvalues.get("espera_alta_lag1", np.nan)
h4_result = "Confirmada" if c_umb > 0 and p_umb < 0.05 else "No confirmada"
print(f"  H4 (Umbral 100d → +): coef = {c_umb:+.4f}{stars(p_umb)}  →  {h4_result}")

# H5: Gasto anterior (inercia) - ahora en logaritmos, coef = elasticidad
c_gas = fe3.params.get("log_g_seguros_lag1", np.nan)
p_gas = fe3.pvalues.get("log_g_seguros_lag1", np.nan)
h5_result = "Confirmada" if c_gas > 0 and p_gas < 0.05 else "No confirmada"
print(f"  H5 (Log Gasto ant. → +): coef = {c_gas:+.4f}{stars(p_gas)}  →  {h5_result}")

md("| Hipótesis | Variable | Coef. | p-value | Resultado |")
md("|-----------|----------|-------|---------|-----------|")
md(f"| H1: Renta | log_pib_pc | {c_pib:+.4f} | {p_pib:.4f}{stars(p_pib)} | {h1_result} |")
md(f"| H2: Espera | espera_lag1 | {c_esp:+.4f} | {p_esp:.4f}{stars(p_esp)} | {h2_result} |")
md(f"| H3: COVID | covid | {c_cov:+.4f} | {p_cov:.4f}{stars(p_cov)} | {h3_result} |")
md(f"| H4: Umbral | espera_alta_lag1 | {c_umb:+.4f} | {p_umb:.4f}{stars(p_umb)} | {h4_result} |")
md(f"| H5: Inercia | log_g_seguros_lag1 | {c_gas:+.4f} | {p_gas:.4f}{stars(p_gas)} | {h5_result} |")

# ═══════════════════════════════════════════════════════════════════════════════
# GUARDAR MARKDOWN
# ═══════════════════════════════════════════════════════════════════════════════
with open(RUTA_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"\n  ✓ Resultados guardados en: {RUTA_MD}")
sep("FIN")
