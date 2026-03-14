"""
===========================================================================
  TESTS DE ESTACIONARIEDAD Y COINTEGRACIÓN EN DATOS DE PANEL
  TFG — Economia de la Salud
  Im-Pesaran-Shin (IPS) · Maddala-Wu (Fisher) · Pedroni · Kao
===========================================================================
"""

from pathlib import Path

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller, coint
import warnings
warnings.filterwarnings("ignore")

BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_CSV    = BASE_DIR / "data" / "datos_tfg_final.csv"
RUTA_MD     = BASE_DIR / "borradores" / "diagnostico_estacionariedad.md"

# ── helpers ──────────────────────────────────────────────────────────────────
def sep(titulo="", ancho=65):
    print("\n" + "═"*ancho)
    if titulo:
        print(f"  {titulo}")
        print("═"*ancho)

def stars(p):
    if p < 0.01: return "***"
    if p < 0.05: return "**"
    if p < 0.10: return "*"
    return ""

# ── Valores tabulados Im, Pesaran & Shin (2003, Tabla 3) — sin tendencia ─────
# Interpolados para T≈9 a partir de T=10 y T=5 de las tablas originales
IPS_MEAN = -1.520   # E[t_iT]  para T=10 (usamos como aprox. T=9)
IPS_VAR  =  1.048   # Var[t_iT] para T=10

# ═══════════════════════════════════════════════════════════════════════════════
# 0. CARGA DE DATOS
# ═══════════════════════════════════════════════════════════════════════════════
df = pd.read_csv(RUTA_CSV)
df = df.sort_values(["ccaa", "ano"]).reset_index(drop=True)

CCAA   = sorted(df["ccaa"].unique())
N      = len(CCAA)
ANOS   = sorted(df["ano"].unique())
T      = len(ANOS)

sep("DATOS CARGADOS")
print(f"  Panel: N={N} CCAA  ×  T={T} años (2016–2024)")
print(f"  Obs. totales: {len(df)}")

# Variables a analizar
VARS = {
    "log_gasto_real" : "Log Gasto Real Seguros (€ p.p.)",
    "log_pib_pc"     : "Log PIB per cápita (€)",
    "esp_esp"        : "Días de Espera Especialistas"
}

# ── Contenedor de resultados para el Markdown ────────────────────────────────
md_lines = []

def md(line=""):
    md_lines.append(line)

# ═══════════════════════════════════════════════════════════════════════════════
# FUNC: ADF individual para cada unidad de panel
# ═══════════════════════════════════════════════════════════════════════════════
def panel_adf(df, variable, maxlag=1, regression="c"):
    """
    Corre ADF por cada CCAA y devuelve DataFrame con resultados.
    regression: 'c' = constante, 'ct' = constante+tendencia, 'n' = ninguna
    """
    rows = []
    for ccaa in CCAA:
        serie = df[df["ccaa"]==ccaa][variable].dropna().values
        if len(serie) < 4:
            continue
        try:
            result = adfuller(serie, maxlag=maxlag, regression=regression,
                              autolag=None)
            rows.append({
                "ccaa"   : ccaa,
                "t_stat" : result[0],
                "p_val"  : result[1],
                "n_obs"  : result[3],
                "lags"   : result[2]
            })
        except Exception:
            pass
    return pd.DataFrame(rows)

# ═══════════════════════════════════════════════════════════════════════════════
# FUNC: Im-Pesaran-Shin (IPS) W-bar statistic
# ═══════════════════════════════════════════════════════════════════════════════
def ips_test(adf_df, e_mean=IPS_MEAN, e_var=IPS_VAR):
    """
    W = sqrt(N) * (t_bar - E[t_iT]) / sqrt(Var[t_iT])  ~ N(0,1)
    H0: todas las series tienen raíz unitaria
    H1: fracción de las series es estacionaria
    """
    t_bar = adf_df["t_stat"].mean()
    n     = len(adf_df)
    W     = np.sqrt(n) * (t_bar - e_mean) / np.sqrt(e_var)
    p_val = stats.norm.cdf(W)          # cola izquierda (rechazo = valores muy negativos)
    return {"t_bar": t_bar, "W": W, "p_value": p_val, "N": n}

# ═══════════════════════════════════════════════════════════════════════════════
# FUNC: Maddala-Wu Fisher Chi2 (1999)
# ═══════════════════════════════════════════════════════════════════════════════
def maddala_wu(adf_df):
    """
    P = -2 * sum(ln(p_i))  ~ Chi2(2N)
    H0: todas las series tienen raíz unitaria
    """
    pvals = adf_df["p_val"].values
    pvals = np.clip(pvals, 1e-10, 1.0)       # evitar log(0)
    stat  = -2.0 * np.sum(np.log(pvals))
    p_val = 1 - stats.chi2.cdf(stat, df=2*len(pvals))
    return {"chi2": stat, "df": 2*len(pvals), "p_value": p_val}

# ═══════════════════════════════════════════════════════════════════════════════
# 1. TESTS EN NIVELES
# ═══════════════════════════════════════════════════════════════════════════════
sep("1. TESTS DE RAÍZ UNITARIA — NIVELES")
md("# Diagnóstico de Estacionariedad y Cointegración en Panel")
md(f"\n**Dataset:** datos_tfg_final.csv  |  N={N}, T={T}  |  Período 2016–2024\n")
md("---\n")
md("## 1. Tests de Raíz Unitaria en Niveles\n")
md("> **H₀ (IPS / Maddala-Wu):** Todas las series del panel tienen raíz unitaria (no estacionarias)  ")
md("> **H₁ (IPS):** Una fracción de las series es estacionaria  ")
md("> Rechazo si **p-value < 0.05** (IPS: cola izquierda)  \n")

nivel_results = {}

for var, label in VARS.items():
    print(f"\n  ── {label} ({var}) ──")
    adf_df = panel_adf(df, var, maxlag=1, regression="c")

    if adf_df.empty:
        print(f"    Insuficientes datos.")
        continue

    ips = ips_test(adf_df)
    mw  = maddala_wu(adf_df)

    nivel_results[var] = {"adf_df": adf_df, "ips": ips, "mw": mw}

    # Consola
    print(f"    Unidades: {ips['N']}  |  t̄ = {ips['t_bar']:.4f}")
    print(f"    IPS  W = {ips['W']:.4f}   p-value = {ips['p_value']:.4f}  {stars(ips['p_value'])}")
    print(f"    MW   χ²({mw['df']}) = {mw['chi2']:.4f}   p-value = {mw['p_value']:.4f}  {stars(mw['p_value'])}")
    decision = "NO se rechaza H₀ → Raíz Unitaria (I(1))" if ips["p_value"] > 0.05 \
               else "Se RECHAZA H₀ → Estacionaria (I(0))"
    print(f"    Conclusión: {decision}")

    # ADF individuales (primeras 5)
    print(f"\n    ADF individuales (muestra):")
    for _, r in adf_df.head(5).iterrows():
        print(f"      {r['ccaa']:22s}  t={r['t_stat']:7.4f}  p={r['p_val']:.4f} {stars(r['p_val'])}")

    # Markdown
    md(f"### Variable: `{var}` — {label}\n")
    md(f"| Test | Estadístico | p-value | Decisión 5% |")
    md(f"|------|------------|---------|-------------|")
    dec_ips = "✅ Rechaza H₀ (I(0))" if ips["p_value"] < 0.05 else "❌ No rechaza H₀ (I(1))"
    dec_mw  = "✅ Rechaza H₀ (I(0))" if mw["p_value"]  < 0.05 else "❌ No rechaza H₀ (I(1))"
    md(f"| IPS (W) | {ips['W']:.4f} | {ips['p_value']:.4f}{stars(ips['p_value'])} | {dec_ips} |")
    md(f"| Maddala-Wu (χ²) | {mw['chi2']:.4f} | {mw['p_value']:.4f}{stars(mw['p_value'])} | {dec_mw} |")
    md("")
    md(f"<details><summary>ADF individuales por CCAA</summary>\n")
    md(f"| CCAA | t-stat | p-value |")
    md(f"|------|--------|---------|")
    for _, r in adf_df.iterrows():
        md(f"| {r['ccaa']} | {r['t_stat']:.4f} | {r['p_val']:.4f}{stars(r['p_val'])} |")
    md(f"\n</details>\n")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. TESTS EN PRIMERAS DIFERENCIAS
# ═══════════════════════════════════════════════════════════════════════════════
sep("2. TESTS DE RAÍZ UNITARIA — PRIMERAS DIFERENCIAS")
md("---\n")
md("## 2. Tests en Primeras Diferencias\n")
md("> Si las variables son I(1), sus primeras diferencias deben ser I(0).  \n")

diff_results = {}

for var, label in VARS.items():
    dvar = f"d_{var}"
    df[dvar] = df.groupby("ccaa")[var].diff(1)

    adf_df = panel_adf(df, dvar, maxlag=0, regression="c")

    if adf_df.empty:
        continue

    ips = ips_test(adf_df)
    mw  = maddala_wu(adf_df)

    diff_results[var] = {"adf_df": adf_df, "ips": ips, "mw": mw}

    print(f"\n  Δ{var}:")
    print(f"    IPS  W = {ips['W']:.4f}   p-value = {ips['p_value']:.4f}  {stars(ips['p_value'])}")
    print(f"    MW   χ²({mw['df']}) = {mw['chi2']:.4f}   p-value = {mw['p_value']:.4f}  {stars(mw['p_value'])}")
    decision = "Se RECHAZA H₀ → I(1) confirmado ✓" if ips["p_value"] < 0.05 \
               else "NO se rechaza H₀ → podría ser I(2)"
    print(f"    Conclusión: {decision}")

    md(f"### Δ`{var}`\n")
    md(f"| Test | Estadístico | p-value | Decisión 5% |")
    md(f"|------|------------|---------|-------------|")
    dec_ips = "✅ Rechaza H₀ → I(1) confirmado" if ips["p_value"] < 0.05 else "❌ No rechaza H₀"
    dec_mw  = "✅ Rechaza H₀ → I(1) confirmado" if mw["p_value"]  < 0.05 else "❌ No rechaza H₀"
    md(f"| IPS (W) | {ips['W']:.4f} | {ips['p_value']:.4f}{stars(ips['p_value'])} | {dec_ips} |")
    md(f"| Maddala-Wu (χ²) | {mw['chi2']:.4f} | {mw['p_value']:.4f}{stars(mw['p_value'])} | {dec_mw} |")
    md("")

# ═══════════════════════════════════════════════════════════════════════════════
# 3. TESTS DE COINTEGRACIÓN DE PEDRONI (1999, 2004)
# ═══════════════════════════════════════════════════════════════════════════════
sep("3. TEST DE COINTEGRACIÓN DE PEDRONI")
md("---\n")
md("## 3. Tests de Cointegración de Pedroni (1999, 2004)\n")
md("> **H₀:** No cointegración para todos los paneles  ")
md("> **H₁:** Cointegración (al menos para algunos paneles)  ")
md("> Modelo estimado: `log_gasto_real = αᵢ + β₁·log_pib_pc + β₂·esp_esp + εᵢₜ`  \n")

# Estimar residuos de la regresión panel por MCO individual
def pedroni_residuals(df, y_var="log_gasto_real",
                      x_vars=["log_pib_pc","esp_esp"]):
    """
    Para cada CCAA, estima por MCO: y = a + b*x + e
    Devuelve dict {ccaa: residuos} y tabla de coeficientes.
    """
    residuals = {}
    coefs     = []
    for ccaa in CCAA:
        sub = df[df["ccaa"]==ccaa][[y_var]+x_vars].dropna()
        if len(sub) < 4:
            continue
        y = sub[y_var].values
        X = np.column_stack([np.ones(len(sub))] + [sub[v].values for v in x_vars])
        try:
            b, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
            e = y - X @ b
            residuals[ccaa] = e
            coefs.append({"ccaa": ccaa, **{x_vars[i]: b[i+1] for i in range(len(x_vars))}})
        except Exception:
            pass
    return residuals, pd.DataFrame(coefs)

residuals, coef_df = pedroni_residuals(df)

# ADF sobre los residuos (sin constante — son residuos de regresión)
def pedroni_stats(residuals, maxlag=1):
    """
    Computa estadísticos de Pedroni a partir de los residuos de cointegración.
    Usamos el test ADF grupo-medio (Between-dim ADF) y el panel ADF (Within-dim).
    """
    adf_stats = []
    for ccaa, e in residuals.items():
        if len(e) < 4:
            continue
        try:
            res = adfuller(e, maxlag=maxlag, regression="n", autolag=None)
            adf_stats.append({"ccaa": ccaa, "t_stat": res[0], "p_val": res[1]})
        except Exception:
            pass
    return pd.DataFrame(adf_stats)

resid_adf = pedroni_stats(residuals, maxlag=1)

# Estadístico Group-mean ADF (Pedroni Between-dimension)
N_coint = len(resid_adf)
group_t_bar = resid_adf["t_stat"].mean()

# Valores críticos aproximados para Pedroni Group-ADF (N=17, T=9)
# Pedroni (1999, Tabla 2): mean=-1.73, var=0.501 (no trend, N grandes)
PEDRONI_MEAN = -1.730
PEDRONI_VAR  =  0.501

Z_pedroni = np.sqrt(N_coint) * (group_t_bar - PEDRONI_MEAN) / np.sqrt(PEDRONI_VAR)
p_pedroni = stats.norm.cdf(Z_pedroni)

# Panel v-stat (within-dimension, Pedroni 2004)
# Simplificado: Fisher combinado sobre p-values de los ADF de residuos
mw_coint = maddala_wu(resid_adf)

print(f"\n  Ecuación de cointegración estimada por CCAA:")
print(f"  log_gasto_real = αᵢ + β₁·log_pib_pc + β₂·esp_esp + εᵢₜ\n")
print(f"  Coeficientes medios estimados:")
print(f"    β₁(log_pib_pc) = {coef_df['log_pib_pc'].mean():.4f}  "
      f"(std={coef_df['log_pib_pc'].std():.4f})")
print(f"    β₂(esp_esp)    = {coef_df['esp_esp'].mean():.6f}  "
      f"(std={coef_df['esp_esp'].std():.6f})")

print(f"\n  Pedroni Group-mean ADF:")
print(f"    t̄_resid = {group_t_bar:.4f}")
print(f"    Z       = {Z_pedroni:.4f}   p-value = {p_pedroni:.4f}  {stars(p_pedroni)}")

print(f"\n  Maddala-Wu sobre residuos (panel v-stat aprox):")
print(f"    χ²({mw_coint['df']}) = {mw_coint['chi2']:.4f}   p-value = {mw_coint['p_value']:.4f}  "
      f"{stars(mw_coint['p_value'])}")

dec_p = "Se RECHAZA H₀ → COINTEGRACIÓN CONFIRMADA" if p_pedroni < 0.05 \
        else "NO se rechaza H₀ → Sin evidencia de cointegración"
dec_mw2 = "Se RECHAZA H₀ → COINTEGRACIÓN CONFIRMADA" if mw_coint["p_value"] < 0.05 \
          else "NO se rechaza H₀ → Sin evidencia de cointegración"
print(f"\n  Pedroni: {dec_p}")
print(f"  MW-res:  {dec_mw2}")

md(f"| Test | Estadístico | p-value | Decisión 5% |")
md(f"|------|------------|---------|-------------|")
md(f"| Pedroni Group-ADF (Z) | {Z_pedroni:.4f} | {p_pedroni:.4f}{stars(p_pedroni)} | {'✅ Cointegración' if p_pedroni<0.05 else '❌ Sin cointegración'} |")
md(f"| Maddala-Wu (residuos) | {mw_coint['chi2']:.4f} (χ²) | {mw_coint['p_value']:.4f}{stars(mw_coint['p_value'])} | {'✅ Cointegración' if mw_coint['p_value']<0.05 else '❌ Sin cointegración'} |")
md("")
md(f"**Coeficientes medios de la ecuación de largo plazo:**\n")
md(f"| Variable | Media β | Std |")
md(f"|----------|---------|-----|")
md(f"| log_pib_pc | {coef_df['log_pib_pc'].mean():.4f} | {coef_df['log_pib_pc'].std():.4f} |")
md(f"| esp_esp | {coef_df['esp_esp'].mean():.6f} | {coef_df['esp_esp'].std():.6f} |")
md("")

# ═══════════════════════════════════════════════════════════════════════════════
# 4. TEST DE KAO (1999) — VERSIÓN SIMPLIFICADA
# ═══════════════════════════════════════════════════════════════════════════════
sep("4. TEST DE COINTEGRACIÓN DE KAO (1999)")
md("---\n")
md("## 4. Test de Cointegración de Kao (1999)\n")
md("> El test de Kao es más restrictivo: impone coeficientes homogéneos (H₁ restringida).  ")
md("> H₀: No cointegración  ")
md("> Estadístico: ADF sobre residuos de regresión within-panel  \n")

# Regresión within (demeaned) con coeficientes restringidos
def kao_test(df, y_var="log_gasto_real", x_vars=["log_pib_pc","esp_esp"]):
    """
    Kao (1999): regresión pooled con efectos individuales (within).
    ADF sobre los residuos pooled.
    """
    sub = df[[y_var, "ccaa"]+x_vars].dropna().copy()
    # Demeaning individual (within transformation)
    for v in [y_var]+x_vars:
        sub[f"{v}_dm"] = sub[v] - sub.groupby("ccaa")[v].transform("mean")
    y_dm = sub[f"{y_var}_dm"].values
    X_dm = np.column_stack([sub[f"{v}_dm"].values for v in x_vars])
    b, _, _, _ = np.linalg.lstsq(X_dm, y_dm, rcond=None)
    e = y_dm - X_dm @ b

    # ADF sobre los residuos pooled (regresión = sin constante, ya demeaned)
    res = adfuller(e, maxlag=1, regression="n", autolag=None)
    t_stat, p_val = res[0], res[1]

    # Estadístico ADF de Kao (aprox): t_stat normalizado
    # Valores críticos Kao (1999): -1.64 (10%), -1.96 (5%), -2.58 (1%)
    return {"t_stat": t_stat, "p_val": p_val}

kao = kao_test(df)
print(f"\n  Kao ADF (residuos within): t = {kao['t_stat']:.4f}   p-value ≈ {kao['p_val']:.4f}  {stars(kao['p_val'])}")
print(f"  Valores críticos Kao: -1.64 (10%), -1.96 (5%), -2.58 (1%)")
dec_kao = "Se RECHAZA H₀ → COINTEGRACIÓN (Kao)" if kao["p_val"] < 0.05 \
          else "NO se rechaza H₀ → Sin cointegración (Kao)"
print(f"  Conclusión: {dec_kao}")

md(f"| Test | t-stat | p-value approx. | VC 5% | Decisión |")
md(f"|------|--------|----------------|-------|---------|")
md(f"| Kao ADF | {kao['t_stat']:.4f} | {kao['p_val']:.4f}{stars(kao['p_val'])} | -1.96 | {'✅ Cointegración' if kao['p_val']<0.05 else '❌ Sin cointegración'} |")
md("")

# ═══════════════════════════════════════════════════════════════════════════════
# 5. TABLA RESUMEN Y CONCLUSIÓN TÉCNICA
# ═══════════════════════════════════════════════════════════════════════════════
sep("5. TABLA RESUMEN Y CONCLUSIÓN TÉCNICA")
md("---\n")
md("## 5. Resumen de Órdenes de Integración\n")
md("| Variable | IPS Niveles p | MW Niveles p | IPS Δ p | MW Δ p | Orden |\n|----------|--------------|-------------|---------|--------|-------|")

orden_vars = {}
for var in VARS:
    if var not in nivel_results or var not in diff_results:
        continue
    ips_n = nivel_results[var]["ips"]["p_value"]
    mw_n  = nivel_results[var]["mw"]["p_value"]
    ips_d = diff_results[var]["ips"]["p_value"]
    mw_d  = diff_results[var]["mw"]["p_value"]
    orden = "I(0)" if ips_n < 0.05 else ("I(1)" if ips_d < 0.05 else "I(2)?")
    orden_vars[var] = orden
    md(f"| `{var}` | {ips_n:.4f}{stars(ips_n)} | {mw_n:.4f}{stars(mw_n)} | {ips_d:.4f}{stars(ips_d)} | {mw_d:.4f}{stars(mw_d)} | **{orden}** |")
md("")

all_i1 = all(v == "I(1)" for v in orden_vars.values())
any_i0 = any(v == "I(0)" for v in orden_vars.values())

# Imprimir resumen en consola
print("\n  RESUMEN DE ÓRDENES DE INTEGRACIÓN:")
for var, orden in orden_vars.items():
    print(f"    {var:25s} → {orden}")

print(f"\n  COINTEGRACIÓN:")
print(f"    Pedroni Group-ADF   p = {p_pedroni:.4f}  {stars(p_pedroni)}")
print(f"    Kao ADF             p = {kao['p_val']:.4f}  {stars(kao['p_val'])}")

# Conclusión técnica
md("---\n")
md("## 6. Conclusión Técnica y Recomendación de Modelo\n")

if all_i1:
    if p_pedroni < 0.05 or kao["p_val"] < 0.05:
        rec = """
### ✅ Variables I(1) + Cointegración detectada

Las tres variables son integradas de orden 1 **[I(1)]** y los tests de Pedroni/Kao
detectan una **relación de largo plazo estable** entre el gasto real, el PIB pc y las
listas de espera.

**Recomendación:** Proceder con el modelo de **Efectos Fijos en Niveles** es válido
(los estimadores FE son *superconsistentes* en presencia de cointegración).
Adicionalmente, se recomienda:

1. **Panel DOLS** (Dynamic OLS) o **Panel FMOLS** (Fully Modified OLS) para obtener
   estimaciones eficientes y sin sesgo de los parámetros de largo plazo.
2. Si interesa la dinámica de corto plazo, estimar un **ECM en panel** (Error
   Correction Model).
3. **No** trabajar en primeras diferencias si hay cointegración, pues se pierde la
   información de largo plazo.
"""
    else:
        rec = """
### ⚠️ Variables I(1) + Sin evidencia de cointegración

Las variables son I(1) pero **no** se detecta cointegración significativa.

**Recomendación:** Trabajar en **primeras diferencias** para evitar regresiones
espurias. El modelo más apropiado sería:

1. **FE en primeras diferencias**: Δlog_gasto_real = αᵢ + β·Δlog_pib_pc + γ·Δesp_esp + uᵢₜ
2. Alternativamente, aplicar **primeras diferencias** y verificar que los residuos
   sean ruido blanco (Portmanteau test, Wooldridge serial correlation test).
3. **No** usar niveles directamente: riesgo de regresión espuria (R² alto, t-stats
   inflados, DW cercano a 0).
"""
elif any_i0:
    rec = """
### ℹ️ Variables I(0) detectadas

Al menos una variable es estacionaria en niveles.

**Recomendación:** Si las variables tienen órdenes de integración mixtos (I(0) e I(1)),
los tests de cointegración clásicos no aplican directamente. Considerar:

1. **Bounds Testing (ARDL)** de Pesaran et al. (2001), que permite variables I(0) e I(1).
2. **FE estándar en niveles** si la variable dependiente es I(0).
"""
else:
    rec = "No determinado con certeza. Revisar individualmente."

md(rec)

md("---")
md("\n### Notas metodológicas\n")
md("- **Período muestral corto** (T=9): los tests de panel tienen mayor potencia que los univariados,")
md("  pero con T=9 el poder sigue siendo limitado. Los resultados deben interpretarse con cautela.")
md("- **IPS (2003)**: estadístico W normalizado, valores tabulados para T=10 usados como aproximación.")
md("- **Maddala-Wu (1999)**: test no paramétrico combinado (Fisher), robusto a T cortos.")
md("- **Pedroni (1999, 2004)**: residuos de la regresión de cointegración individual, estadístico Group-ADF.")
md("- **Kao (1999)**: coeficientes homogéneos (within), ADF pooled sobre residuos.")
md("- `***` p<0.01  `**` p<0.05  `*` p<0.10\n")

print(rec)

# ═══════════════════════════════════════════════════════════════════════════════
# 6. GUARDAR EL MARKDOWN
# ═══════════════════════════════════════════════════════════════════════════════
sep("6. GUARDANDO diagnostico_estacionariedad.md")
with open(RUTA_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"\n  ✓ Archivo guardado en:\n    {RUTA_MD}")
sep("ANÁLISIS COMPLETADO")
