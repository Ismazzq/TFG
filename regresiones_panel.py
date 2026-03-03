"""
===========================================================================
  ESTIMACIÓN DE MODELOS DE PANEL DE DATOS — TFG Econometría de la Salud
  Efectos Fijos · Efectos Aleatorios · Hausman · Wald · Stargazer
===========================================================================
"""

from pathlib import Path

import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

from linearmodels.panel import PanelOLS, RandomEffects, PooledOLS
from linearmodels.panel.results import PanelEffectsResults

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "datos_tfg_final.csv"
RUTA_MD  = BASE_DIR / "tablas_regresion.md"

def sep(titulo="", ancho=65):
    print("\n" + "═"*ancho)
    if titulo:
        print(f"  {titulo}")
        print("═"*ancho)

def stars(p):
    if p is None or np.isnan(p): return ""
    if p < 0.01: return "***"
    if p < 0.05: return "**"
    if p < 0.10: return "*"
    return ""

# ═══════════════════════════════════════════════════════════════════════════════
# 0. CARGA Y PREPARACIÓN
# ═══════════════════════════════════════════════════════════════════════════════
sep("0. CARGA Y PREPARACIÓN DE DATOS")

df = pd.read_csv(RUTA_CSV)
df = df.sort_values(["ccaa", "ano"]).reset_index(drop=True)

# Renombramos para claridad en fórmulas
df["control_mayores"] = df["pob_65_pct"]
df["covid"]           = df["dummy_covid"]
df["espera_alta"]     = df["espera_alta"]       # ya existe

# Variables del modelo — eliminar filas con NaN en cualquier variable usada
VARS_MODELO = ["log_gasto_real", "log_pib_pc", "espera_lag1",
               "espera_lag2", "covid", "control_mayores", "espera_alta"]

df_clean = df.dropna(subset=VARS_MODELO).copy()

print(f"  Obs. originales      : {len(df)}")
print(f"  Obs. tras dropna     : {len(df_clean)}")
print(f"  CCAA                 : {df_clean['ccaa'].nunique()}")
print(f"  Años cubiertos       : {sorted(df_clean['ano'].unique())}")

# ── Crear índice MultiIndex (ccaa, ano) requerido por linearmodels ────────────
df_clean = df_clean.set_index(["ccaa", "ano"])

# ── Markdown acumulador ───────────────────────────────────────────────────────
md_lines = []
def md(line=""): md_lines.append(line)

md("# Resultados de las Regresiones de Panel — TFG Econometría de la Salud\n")
md(f"**Variable dependiente:** `log_gasto_real` (Log Gasto Real en Seguros Privados, €pp)  ")
md(f"**Período:** 2016–2024  |  **N CCAA:** {df_clean.index.get_level_values(0).nunique()}  ")
md(f"**Errores estándar:** Robustos cluster por CCAA  \n")
md("---\n")

# ═══════════════════════════════════════════════════════════════════════════════
# HELPER: extraer coeficientes de un resultado linearmodels
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

def fmt(val, decimals=4):
    if val is None or (isinstance(val, float) and np.isnan(val)):
        return "—"
    return f"{val:.{decimals}f}"

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 1 — FE  y  RE
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 1 — EFECTOS FIJOS Y ALEATORIOS")
md("## Modelo 1: Especificación Base\n")
md("$$\\log(\\text{gasto\\_real})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib\\_pc})_{it} + \\beta_2 \\text{espera\\_lag1}_{it} + \\beta_3 \\text{covid}_{it} + \\beta_4 \\text{control\\_mayores}_{it} + \\varepsilon_{it}$$\n")

VARS_M1 = ["log_pib_pc", "espera_lag1", "covid", "control_mayores"]

# ── Efectos Fijos ─────────────────────────────────────────────────────────────
fe1 = PanelOLS(
    dependent = df_clean["log_gasto_real"],
    exog      = df_clean[VARS_M1],
    entity_effects=True,
    time_effects=False
).fit(cov_type="clustered", cluster_entity=True)

# ── Efectos Aleatorios ────────────────────────────────────────────────────────
re1 = RandomEffects(
    dependent = df_clean["log_gasto_real"],
    exog      = df_clean[["Intercept"] + VARS_M1]
              if "Intercept" in df_clean.columns
              else df_clean[VARS_M1].assign(Intercept=1)[["Intercept"]+VARS_M1]
).fit(cov_type="robust")

# Añadir constante para RE correctamente
import statsmodels.api as sm
X_re = sm.add_constant(df_clean[VARS_M1])
re1 = RandomEffects(
    dependent = df_clean["log_gasto_real"],
    exog      = X_re
).fit(cov_type="robust")

coef_fe1 = extract_results(fe1, VARS_M1)
coef_re1 = extract_results(re1, VARS_M1 + ["const"])

print("\n  ── Efectos Fijos (M1-FE) ──")
print(f"  {'Variable':22s}  {'Coef':>9}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe1.items():
    print(f"  {v:22s}  {c:9.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"\n  R² within = {fe1.rsquared:.4f}  |  Obs = {int(fe1.nobs)}  |  Entidades = {fe1.entity_info['total']}")

print("\n  ── Efectos Aleatorios (M1-RE) ──")
print(f"  {'Variable':22s}  {'Coef':>9}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v in VARS_M1:
    c, se, t, p = coef_re1[v]
    print(f"  {v:22s}  {c:9.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"\n  R² overall = {re1.rsquared:.4f}  |  Obs = {int(re1.nobs)}")

# ───────────────────────────────────────────────────────────────────────────────
# TEST DE HAUSMAN (manual — comparación FE vs RE)
# ───────────────────────────────────────────────────────────────────────────────
sep("  TEST DE HAUSMAN — M1")
md("### Test de Hausman: FE vs RE\n")
md("> **H₀:** Los estimadores RE son consistentes y eficientes (efectos individuales no correlacionados con regresores)  ")
md("> **H₁:** Los estimadores FE son preferidos (efectos correlacionados con regresores)  \n")

# Hausman: H = (b_FE - b_RE)' * [Var(b_FE) - Var(b_RE)]^{-1} * (b_FE - b_RE) ~ Chi2(K)
b_fe = np.array([fe1.params[v] for v in VARS_M1])
b_re = np.array([re1.params[v] for v in VARS_M1])

# Matrices de varianza-covarianza
V_fe = fe1.cov.loc[VARS_M1, VARS_M1].values
V_re = re1.cov.loc[VARS_M1, VARS_M1].values

diff      = b_fe - b_re
V_diff    = V_fe - V_re

# Asegurar simetría y positividad antes de invertir
V_diff_sym = (V_diff + V_diff.T) / 2
# Si no es definida positiva, usar pseudoinversa
try:
    eigvals = np.linalg.eigvalsh(V_diff_sym)
    if np.all(eigvals > 0):
        V_inv = np.linalg.inv(V_diff_sym)
    else:
        V_inv = np.linalg.pinv(V_diff_sym)
except Exception:
    V_inv = np.linalg.pinv(V_diff_sym)

H_stat = float(diff @ V_inv @ diff)
k      = len(VARS_M1)
H_pval = 1 - stats.chi2.cdf(H_stat, df=k)

print(f"\n  Hausman χ²({k}) = {H_stat:.4f}   p-value = {H_pval:.4f}  {stars(H_pval)}")
if H_pval < 0.05:
    hausman_decision = "Se RECHAZA H₀ → **Efectos Fijos preferido** (diferencias sistemáticas entre estimadores)"
else:
    hausman_decision = "No se rechaza H₀ → **Efectos Aleatorios preferido** (RE consistente y eficiente)"
print(f"  Conclusión: {hausman_decision}")

md(f"| Estadístico | gl | p-value | Decisión |\n|-------------|----|---------|---------|\n")
md(f"| χ² = {H_stat:.4f} | {k} | {H_pval:.4f}{stars(H_pval)} | {hausman_decision} |\n")

MODELO_PREFERIDO = "FE" if H_pval < 0.05 else "RE"
print(f"\n  ► Modelo preferido para la continuación: **{MODELO_PREFERIDO}**")

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 2 — FE con espera_lag2 + Test de Wald
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 2 — DINÁMICA DE RETARDOS (FE + espera_lag2)")
md("---\n## Modelo 2: Especificación con Dinámica de Retardos\n")
md("$$\\log(\\text{gasto})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib})_{it} + \\beta_2 \\text{lag1}_{it} + \\beta_3 \\text{lag2}_{it} + \\beta_4 \\text{covid}_{it} + \\beta_5 \\text{control\\_mayores}_{it} + \\varepsilon_{it}$$\n")

VARS_M2 = ["log_pib_pc", "espera_lag1", "espera_lag2", "covid", "control_mayores"]

fe2 = PanelOLS(
    dependent=df_clean["log_gasto_real"],
    exog=df_clean[VARS_M2],
    entity_effects=True
).fit(cov_type="clustered", cluster_entity=True)

coef_fe2 = extract_results(fe2, VARS_M2)

print(f"\n  {'Variable':22s}  {'Coef':>9}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe2.items():
    print(f"  {v:22s}  {c:9.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"\n  R² within = {fe2.rsquared:.4f}  |  Obs = {int(fe2.nobs)}")

# ── Test de Wald: espera_lag1 = espera_lag2 = 0
sep("  TEST DE WALD — espera_lag1 = espera_lag2 = 0")
md("### Test de Wald: Significatividad Conjunta de espera_lag1 y espera_lag2\n")
md("> **H₀:** β(espera_lag1) = β(espera_lag2) = 0  ")
md("> **H₁:** Al menos uno ≠ 0  \n")

c1, se1, t1, p1 = coef_fe2["espera_lag1"]
c2, se2, t2, p2 = coef_fe2["espera_lag2"]

# Wald manual: R * b ~ N(0, R*V*R')
R   = np.array([[1,0,0,0,0],[0,1,0,0,0]])   # restricciones sobre lag1 y lag2
b   = np.array([fe2.params[v] for v in VARS_M2])
V   = fe2.cov.loc[VARS_M2, VARS_M2].values
Rb  = R @ b
RVR = R @ V @ R.T
try:
    wald_stat = float(Rb @ np.linalg.inv(RVR) @ Rb)
except Exception:
    wald_stat = float(Rb @ np.linalg.pinv(RVR) @ Rb)
wald_pval = 1 - stats.chi2.cdf(wald_stat, df=2)
wald_F    = wald_stat / 2
wald_pF   = 1 - stats.f.cdf(wald_F, 2, int(fe2.nobs) - len(VARS_M2) - int(fe2.entity_info["total"]))

print(f"\n  Wald χ²(2) = {wald_stat:.4f}   p-value = {wald_pval:.4f}  {stars(wald_pval)}")
print(f"  Wald F(2,N)= {wald_F:.4f}   p-value = {wald_pF:.4f}  {stars(wald_pF)}")
if wald_pval < 0.05:
    wald_dec = "Se RECHAZA H₀ → espera_lag1 y espera_lag2 son conjuntamente significativos"
else:
    wald_dec = "No se rechaza H₀ → espera_lag1 y espera_lag2 no son conjuntamente significativos"
print(f"  Conclusión: {wald_dec}")

md(f"| Test | Estadístico | gl | p-value | Decisión |\n|------|------------|----|---------|---------|\n")
md(f"| Wald χ² | {wald_stat:.4f} | 2 | {wald_pval:.4f}{stars(wald_pval)} | {wald_dec} |")
md(f"| Wald F  | {wald_F:.4f}  | (2,N) | {wald_pF:.4f}{stars(wald_pF)} | — |\n")

# ═══════════════════════════════════════════════════════════════════════════════
# MODELO 3 — Efecto Umbral (dummy espera_alta)
# ═══════════════════════════════════════════════════════════════════════════════
sep("MODELO 3 — EFECTO UMBRAL (dummy espera_alta > 100 días)")
md("---\n## Modelo 3: Efecto Umbral (No Linealidad)\n")
md("$$\\log(\\text{gasto})_{it} = \\alpha_i + \\beta_1 \\log(\\text{pib})_{it} + \\beta_2 \\mathbf{1}_{\\text{espera}>100} + \\beta_3 \\text{covid}_{it} + \\beta_4 \\text{control\\_mayores}_{it} + \\varepsilon_{it}$$\n")

VARS_M3 = ["log_pib_pc", "espera_alta", "covid", "control_mayores"]

fe3 = PanelOLS(
    dependent=df_clean["log_gasto_real"],
    exog=df_clean[VARS_M3],
    entity_effects=True
).fit(cov_type="clustered", cluster_entity=True)

coef_fe3 = extract_results(fe3, VARS_M3)

print(f"\n  {'Variable':22s}  {'Coef':>9}  {'SE':>9}  {'t':>7}  {'p':>8}")
for v, (c, se, t, p) in coef_fe3.items():
    print(f"  {v:22s}  {c:9.4f}  {se:9.4f}  {t:7.3f}  {p:8.4f} {stars(p)}")
print(f"\n  R² within = {fe3.rsquared:.4f}  |  Obs = {int(fe3.nobs)}")

# ═══════════════════════════════════════════════════════════════════════════════
# TABLA COMPARATIVA TIPO STARGAZER
# ═══════════════════════════════════════════════════════════════════════════════
sep("TABLA COMPARATIVA — STARGAZER")

ALL_VARS = ["log_pib_pc", "espera_lag1", "espera_lag2", "espera_alta",
            "covid", "control_mayores"]
VAR_LABELS = {
    "log_pib_pc"       : "Log PIB pc",
    "espera_lag1"      : "Espera esp. (lag 1)",
    "espera_lag2"      : "Espera esp. (lag 2)",
    "espera_alta"      : "Dummy espera > 100d",
    "covid"            : "Dummy COVID-19",
    "control_mayores"  : "Pob. > 65 años (%)",
}

models     = [fe1, re1, fe2, fe3]
model_names = ["M1-FE", "M1-RE", "M2-FE+Lags", "M3-Umbral"]
model_vars  = [VARS_M1, VARS_M1, VARS_M2, VARS_M3]

# Anchos de columna
W_VAR  = 24
W_COL  = 14

def hline(char="-"):
    return char * (W_VAR + W_COL * len(models) + 4)

header = f"{'':>{W_VAR}}" + "".join(f"{'   '+n:>{W_COL}}" for n in model_names)
print(f"\n{hline('═')}")
print(f"  Tabla comparativa — Variable dependiente: log_gasto_real")
print(f"{hline('═')}")
print(f"  {header}")
print(f"  {hline()}")

def cell(res, var):
    if var not in res.params.index:
        return f"{'':>{W_COL}}"
    c = res.params[var]; p = res.pvalues[var]
    return f"{c:+.4f}{stars(p):3s}".rjust(W_COL)

def cell_se(res, var):
    if var not in res.std_errors.index:
        return f"{'':>{W_COL}}"
    se = res.std_errors[var]
    return f"({se:.4f})".rjust(W_COL)

for var in ALL_VARS:
    row_c  = f"  {VAR_LABELS[var]:<{W_VAR}}"
    row_se = f"  {'':>{W_VAR}}"
    for i, (res, mvars) in enumerate(zip(models, model_vars)):
        row_c  += cell(res, var)
        row_se += cell_se(res, var)
    print(row_c)
    print(row_se)

print(f"  {hline()}")

# Estadísticos de ajuste
r2s   = [m.rsquared        for m in models]
nobs  = [int(m.nobs)        for m in models]
ncaa  = [int(m.entity_info["total"]) for m in models]

row_r2  = f"  {'R² (within)':<{W_VAR}}" + "".join(f"{r:>13.4f} " for r in r2s)
row_n   = f"  {'Observaciones':<{W_VAR}}" + "".join(f"{n:>13d} " for n in nobs)
row_e   = f"  {'Entidades CCAA':<{W_VAR}}" + "".join(f"{e:>13d} " for e in ncaa)
row_fe  = f"  {'Efectos Fijos':<{W_VAR}}" + "".join(f"{'SÍ' if 'FE' in nm else 'NO':>13s} " for nm in model_names)
row_rob = f"  {'SE cluster CCAA':<{W_VAR}}" + "".join(f"{'SÍ' if 'FE' in nm else 'Robustos':>13s} " for nm in model_names)

for row in [row_r2, row_n, row_e, row_fe, row_rob]:
    print(row)
print(f"  {hline('═')}")
print(f"  Nota: *** p<0.01  ** p<0.05  * p<0.10  |  (errores estándar en paréntesis)")

# ═══════════════════════════════════════════════════════════════════════════════
# MARKDOWN — TABLA STARGAZER
# ═══════════════════════════════════════════════════════════════════════════════
md("---\n## Tabla Comparativa de Modelos (Stargazer)\n")
md("**Variable dependiente:** `log_gasto_real`  \n")

# Cabecera
md(f"| Variable | {' | '.join(model_names)} |")
md(f"|{'---------|' * (len(models)+1)}")

for var in ALL_VARS:
    row_c  = f"| **{VAR_LABELS[var]}** "
    row_se = f"| "
    for res in models:
        if var in res.params.index:
            c = res.params[var]; p = res.pvalues[var]; se = res.std_errors[var]
            row_c  += f"| {c:+.4f}{stars(p)} "
            row_se += f"| ({se:.4f}) "
        else:
            row_c  += "| — "
            row_se += "| "
    md(row_c + "|")
    md(row_se + "|")

md(f"| **R² within** | {' | '.join(f'{r:.4f}' for r in r2s)} |")
md(f"| **Observaciones** | {' | '.join(str(n) for n in nobs)} |")
md(f"| **CCAA** | {' | '.join(str(e) for e in ncaa)} |")
md(f"| **Efectos Fijos** | {' | '.join('SÍ' if 'FE' in nm else 'NO' for nm in model_names)} |")
md(f"| **SE cluster CCAA** | {' | '.join('SÍ' if 'FE' in nm else 'Robustos' for nm in model_names)} |")
md("")
md("> `***` p<0.01  `**` p<0.05  `*` p<0.10  |  Errores estándar en paréntesis\n")

# ═══════════════════════════════════════════════════════════════════════════════
# INTERPRETACIÓN ECONÓMICA DETALLADA
# ═══════════════════════════════════════════════════════════════════════════════
sep("INTERPRETACIÓN ECONÓMICA")
md("---\n## Interpretación Econométrica Detallada\n")

c_pib_fe1, se_pib_fe1, t_pib_fe1, p_pib_fe1   = coef_fe1["log_pib_pc"]
c_lag1_fe1, se_lag1, t_lag1, p_lag1             = coef_fe1["espera_lag1"]
c_cov_fe1, se_cov, t_cov, p_cov                 = coef_fe1["covid"]
c_may_fe1, se_may, t_may, p_may                  = coef_fe1["control_mayores"]
c_lag2_fe2, se_lag2, t_lag2, p_lag2             = coef_fe2["espera_lag2"]
c_alta_fe3, se_alta, t_alta, p_alta             = coef_fe3["espera_alta"]
c_pib_fe3, se_pib3, t_pib3, p_pib3             = coef_fe3["log_pib_pc"]

lines = [
    f"### Modelo 1 — Efectos Fijos (preferido por Hausman: {MODELO_PREFERIDO})\n",
    f"- **Log PIB pc** (β={c_pib_fe1:+.4f}{stars(p_pib_fe1)}): Un incremento del 1% en el PIB per cápita se asocia "
    f"con un {'aumento' if c_pib_fe1>0 else 'descenso'} del {abs(c_pib_fe1):.2f}% en el gasto real en seguros privados. "
    f"{'Elástico' if abs(c_pib_fe1)>1 else 'Inelástico'} al ingreso.",
    f"- **Espera lag1** (β={c_lag1_fe1:+.4f}{stars(p_lag1)}): Un día adicional de espera en t-1 {'aumenta' if c_lag1_fe1>0 else 'reduce'} "
    f"el gasto en seguros en {abs(c_lag1_fe1)*100:.2f}% —consistente con el mecanismo de 'huida' hacia el sector privado.",
    f"- **COVID** (β={c_cov_fe1:+.4f}{stars(p_cov)}): Durante 2020 el gasto {'aumentó' if c_cov_fe1>0 else 'cayó'} un {abs(c_cov_fe1*100):.2f}% "
    f"respecto al contrafactual.",
    f"- **Pob. >65 años** (β={c_may_fe1:+.4f}{stars(p_may)}): Cada punto porcentual adicional de población mayor "
    f"{'eleva' if c_may_fe1>0 else 'reduce'} el gasto real en {abs(c_may_fe1)*100:.2f}%.",
    "",
    "### Modelo 2 — Dinámica de Retardos\n",
    f"- **Espera lag2** (β={c_lag2_fe2:+.4f}{stars(p_lag2)}): El efecto de la espera tiene componente de retardo de 2 años.",
    f"- **Test de Wald χ²(2) = {wald_stat:.4f} (p={wald_pval:.4f}{stars(wald_pval)})**: "
    f"{'Los lags son conjuntamente significativos.' if wald_pval<0.05 else 'Los lags NO son conjuntamente significativos.'}",
    "",
    "### Modelo 3 — Efecto No Lineal (Umbral)\n",
    f"- **Dummy espera>100d** (β={c_alta_fe3:+.4f}{stars(p_alta)}): Cuando las listas de espera superan los 100 días, "
    f"el gasto en seguros privados {'sube' if c_alta_fe3>0 else 'baja'} un {abs(c_alta_fe3)*100:.2f}% adicional. "
    f"{'Efecto umbral significativo — evidencia de no linealidad.' if p_alta<0.05 else 'Efecto umbral no significativo al 5%.'}",
]

for line in lines:
    print(f"  {line}")
    md(line)

# ═══════════════════════════════════════════════════════════════════════════════
# RESUMEN DE TESTS ADICIONALES
# ═══════════════════════════════════════════════════════════════════════════════
md("\n---\n## Resumen de Tests de Especificación\n")
md(f"| Test | Estadístico | p-value | Conclusión |")
md(f"|------|------------|---------|------------|")
md(f"| Hausman (FE vs RE) | χ²({k})={H_stat:.4f} | {H_pval:.4f}{stars(H_pval)} | {MODELO_PREFERIDO} preferido |")
md(f"| Wald (lag1=lag2=0) | χ²(2)={wald_stat:.4f} | {wald_pval:.4f}{stars(wald_pval)} | {'Significativos' if wald_pval<0.05 else 'No significativos'} |")
md("")
md("---\n### Notas metodológicas\n")
md("- Estimación por `linearmodels.PanelOLS` con `entity_effects=True`.")
md("- M1-RE estimado por GLS (Swamy-Arora) con SE robustos (HC).")
md("- SE en FE: cluster por entidad (CCAA) para corregir autocorrelación intragrupo.")
md("- `espera_lag1` y `espera_lag2` generados dentro de cada CCAA para evitar contaminación entre regiones.")
md("- `control_mayores` = % población > 65 años (INE Padrón Municipal, 2016–2024).")
md("- La dummy `covid` = 1 únicamente para el año 2020.")
md("- `***` p<0.01  `**` p<0.05  `*` p<0.10\n")

# ═══════════════════════════════════════════════════════════════════════════════
# GUARDAR MARKDOWN
# ═══════════════════════════════════════════════════════════════════════════════
sep("GUARDANDO tablas_regresion.md")
with open(RUTA_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print(f"\n  ✓ Guardado en: {RUTA_MD}")
sep("ESTIMACIÓN COMPLETADA")
