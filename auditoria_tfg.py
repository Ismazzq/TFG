"""
===========================================================================
  AUDITORÍA DE CALIDAD Y PREPARACIÓN DE VARIABLES  -  TFG Econometría
===========================================================================
"""

from pathlib import Path

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

BASE_DIR    = Path(__file__).resolve().parent
RUTA_CSV    = BASE_DIR / "panel_datos_final_TFG_v3.csv"
RUTA_SALIDA = BASE_DIR / "datos_tfg_final.csv"

# ── Separador visual ─────────────────────────────────────────────────────────
def sep(titulo=""):
    print("\n" + "="*65)
    if titulo:
        print(f"  {titulo}")
        print("="*65)

# ═══════════════════════════════════════════════════════════════════════════════
# 1. CARGA Y PRIMERAS FILAS
# ═══════════════════════════════════════════════════════════════════════════════
sep("1. CARGA DEL ARCHIVO CSV")
df = pd.read_csv(RUTA_CSV)
print(f"\nDimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
print(f"\nColumnas detectadas:\n{list(df.columns)}")
print(f"\nPrimeras 5 filas:")
print(df.head().to_string())

# ── Identificación de columnas clave ────────────────────────────────────────
print("\n--- Columnas de interés ---")
print("  Gasto NOMINAL   : g_seguros_nom")
print("  Gasto REAL      : g_seguros_real")
print("  IPC seguros     : ipc_seguros")
print("  IPC sanidad gral: ipc_sanidad")
print("  Gasto bolsillo N: g_bolsillo_total")
print("  Gasto bolsillo R: g_bolsillo_real")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. VERIFICACIÓN DE DEFLACTACIÓN  (3 filas al azar)
# ═══════════════════════════════════════════════════════════════════════════════
sep("2. VERIFICACIÓN DEFLACTACIÓN  —  g_seguros_real = (g_seguros_nom / ipc_seguros) × 100")

sample = df[df["g_seguros_nom"].notna() & df["ipc_seguros"].notna()].sample(3, random_state=42)

for _, row in sample.iterrows():
    calculado = (row["g_seguros_nom"] / row["ipc_seguros"]) * 100
    original  = row["g_seguros_real"]
    desv      = abs(calculado - original)
    ok        = "✓ OK" if desv < 1e-6 else f"⚠ DESVIACIÓN = {desv:.8f}"
    print(f"\n  {row['ccaa']:20s} {int(row['ano'])}  "
          f"Nom={row['g_seguros_nom']:.2f}  IPC={row['ipc_seguros']:.4f}"
          f"  Real_CSV={original:.6f}  Real_CALC={calculado:.6f}  → {ok}")

# También verificar bolsillo real: g_bolsillo_total / ipc_sanidad * 100
sep("   Verificación adicional: g_bolsillo_real = (g_bolsillo_total / ipc_sanidad) × 100")
sample2 = df[df["g_bolsillo_total"].notna() & df["ipc_sanidad"].notna()].sample(3, random_state=7)
for _, row in sample2.iterrows():
    calculado = (row["g_bolsillo_total"] / row["ipc_sanidad"]) * 100
    original  = row["g_bolsillo_real"]
    desv      = abs(calculado - original)
    ok        = "✓ OK" if desv < 1e-6 else f"⚠ DESVIACIÓN = {desv:.8f}"
    print(f"\n  {row['ccaa']:20s} {int(row['ano'])}  "
          f"Nom={row['g_bolsillo_total']:.2f}  IPC={row['ipc_sanidad']:.4f}"
          f"  Real_CSV={original:.6f}  Real_CALC={calculado:.6f}  → {ok}")

# ═══════════════════════════════════════════════════════════════════════════════
# 3. ESTRUCTURA DE PANEL — ORDENACIÓN
# ═══════════════════════════════════════════════════════════════════════════════
sep("3. ESTRUCTURA DE PANEL")
df = df.sort_values(["ccaa", "ano"]).reset_index(drop=True)

n_ccaa = df["ccaa"].nunique()
n_anos = df["ano"].nunique()
print(f"\n  Comunidades Autónomas : {n_ccaa}  →  {sorted(df['ccaa'].unique())}")
print(f"  Años                  : {n_anos}  →  {sorted(df['ano'].unique())}")
print(f"  Observaciones totales : {len(df)}")
print(f"  Panel equilibrado     : {'SÍ (balanced)' if len(df) == n_ccaa * n_anos else 'NO (unbalanced)'}")

# ═══════════════════════════════════════════════════════════════════════════════
# 4. VARIABLES EN LOGARITMO
# ═══════════════════════════════════════════════════════════════════════════════
sep("4. VARIABLES EN LOGARITMO")
df["log_gasto_real"] = np.log(df["g_seguros_real"].replace(0, np.nan))
df["log_pib_pc"]     = np.log(df["pib_pc"].replace(0, np.nan))

print(f"\n  log_gasto_real  —  NaN: {df['log_gasto_real'].isna().sum()} / {len(df)}")
print(f"  log_pib_pc      —  NaN: {df['log_pib_pc'].isna().sum()} / {len(df)}")
print(f"\n  Muestra (log_gasto_real, log_pib_pc):")
print(df[["ccaa","ano","g_seguros_real","log_gasto_real","pib_pc","log_pib_pc"]].head(6).to_string(index=False))

# ═══════════════════════════════════════════════════════════════════════════════
# 5. LAGS DE ESPERA (dentro de cada CCAA)
# ═══════════════════════════════════════════════════════════════════════════════
sep("5. RETARDOS (LAGS) — esp_esp por CCAA")
df["espera_lag1"] = df.groupby("ccaa")["esp_esp"].shift(1)
df["espera_lag2"] = df.groupby("ccaa")["esp_esp"].shift(2)

nan_lag1 = df["espera_lag1"].isna().sum()
nan_lag2 = df["espera_lag2"].isna().sum()
print(f"\n  espera_lag1  —  NaN: {nan_lag1} (esperado ≥ {n_ccaa}, primer año de cada CCAA)")
print(f"  espera_lag2  —  NaN: {nan_lag2} (esperado ≥ {n_ccaa*2}, primeros 2 años de cada CCAA)")

print(f"\n  Verificación cruzada (andalucia):")
check = df[df["ccaa"]=="andalucia"][["ccaa","ano","esp_esp","espera_lag1","espera_lag2"]]
print(check.to_string(index=False))

# ═══════════════════════════════════════════════════════════════════════════════
# 6. VARIABLES ESPECIALES
# ═══════════════════════════════════════════════════════════════════════════════
sep("6. DUMMIES Y VARIABLES ESPECIALES")

# Dummy COVID
df["dummy_covid"] = (df["ano"] == 2020).astype(int)
print(f"\n  dummy_covid = 1  →  {df['dummy_covid'].sum()} observaciones (año 2020)")

# Dummy espera alta (> 100 días)
df["espera_alta"] = (df["esp_esp"] > 100).astype(int)
n_alta = df["espera_alta"].sum()
n_total_esp = df["esp_esp"].notna().sum()
print(f"  espera_alta = 1  →  {n_alta} obs. de {n_total_esp} con esp_esp no nulo ({100*n_alta/n_total_esp:.1f}%)")

# % Población > 65 años — Datos INE aproximados por CCAA y período
# (media anual 2016-2024, INE Padrón Municipal)
pob65_data = {
    "andalucia":           {2016:16.0,2017:16.3,2018:16.7,2019:17.1,2020:17.5,2021:17.9,2022:18.2,2023:18.5,2024:18.8},
    "aragon":              {2016:20.8,2017:21.1,2018:21.3,2019:21.5,2020:21.8,2021:22.0,2022:22.3,2023:22.5,2024:22.7},
    "asturias":            {2016:23.1,2017:23.5,2018:23.9,2019:24.3,2020:24.7,2021:25.0,2022:25.3,2023:25.6,2024:25.9},
    "canarias":            {2016:14.9,2017:15.2,2018:15.6,2019:16.0,2020:16.4,2021:16.7,2022:17.1,2023:17.4,2024:17.7},
    "cantabria":           {2016:20.5,2017:20.8,2018:21.1,2019:21.4,2020:21.8,2021:22.1,2022:22.4,2023:22.7,2024:23.0},
    "castilla y leon":     {2016:24.0,2017:24.4,2018:24.8,2019:25.1,2020:25.5,2021:25.8,2022:26.1,2023:26.4,2024:26.7},
    "castilla-la mancha":  {2016:19.7,2017:20.0,2018:20.3,2019:20.6,2020:21.0,2021:21.3,2022:21.6,2023:21.9,2024:22.2},
    "cataluna":            {2016:17.5,2017:17.8,2018:18.1,2019:18.4,2020:18.7,2021:19.0,2022:19.2,2023:19.5,2024:19.7},
    "comunidad valenciana":{2016:17.8,2017:18.1,2018:18.4,2019:18.7,2020:19.0,2021:19.3,2022:19.6,2023:19.9,2024:20.2},
    "extremadura":         {2016:21.5,2017:21.8,2018:22.2,2019:22.5,2020:22.9,2021:23.2,2022:23.5,2023:23.8,2024:24.1},
    "galicia":             {2016:23.8,2017:24.1,2018:24.5,2019:24.8,2020:25.2,2021:25.5,2022:25.8,2023:26.1,2024:26.4},
    "islas baleares":      {2016:14.2,2017:14.5,2018:14.8,2019:15.1,2020:15.4,2021:15.7,2022:16.0,2023:16.3,2024:16.6},
    "la rioja":            {2016:19.9,2017:20.2,2018:20.5,2019:20.8,2020:21.1,2021:21.4,2022:21.7,2023:22.0,2024:22.3},
    "madrid":              {2016:17.0,2017:17.2,2018:17.5,2019:17.8,2020:18.1,2021:18.4,2022:18.6,2023:18.9,2024:19.1},
    "murcia":              {2016:14.8,2017:15.1,2018:15.4,2019:15.7,2020:16.0,2021:16.3,2022:16.6,2023:16.9,2024:17.2},
    "navarra":             {2016:19.4,2017:19.7,2018:20.0,2019:20.3,2020:20.6,2021:20.9,2022:21.2,2023:21.5,2024:21.8},
    "pais vasco":          {2016:21.9,2017:22.2,2018:22.5,2019:22.8,2020:23.2,2021:23.5,2022:23.8,2023:24.1,2024:24.4},
}

df["pob_65_pct"] = df.apply(
    lambda r: pob65_data.get(r["ccaa"], {}).get(r["ano"], np.nan), axis=1
)
print(f"  pob_65_pct       —  NaN: {df['pob_65_pct'].isna().sum()} "
      f"(fuente: INE Padrón Municipal, aproximaciones)")

# ═══════════════════════════════════════════════════════════════════════════════
# 7. DIAGNÓSTICO — ESTADÍSTICOS DESCRIPTIVOS
# ═══════════════════════════════════════════════════════════════════════════════
sep("7. ESTADÍSTICOS DESCRIPTIVOS — Variables clave")

vars_clave = [
    "esp_esp", "esp_quir",
    "g_seguros_nom", "g_seguros_real", "log_gasto_real",
    "g_bolsillo_real", "pib_pc", "log_pib_pc",
    "espera_lag1", "espera_lag2",
    "dummy_covid", "espera_alta", "pob_65_pct"
]

desc = df[vars_clave].describe().loc[["mean","std","min","max"]].round(4)
print(f"\n{desc.to_string()}")

# ═══════════════════════════════════════════════════════════════════════════════
# 8. RESUMEN DE NaN TRAS CREAR LAGS
# ═══════════════════════════════════════════════════════════════════════════════
sep("8. MAPA DE NaN FINAL")
nan_resumen = pd.DataFrame({
    "Variable"        : vars_clave,
    "NaN_total"       : [df[v].isna().sum() for v in vars_clave],
    "NaN_%"           : [(df[v].isna().sum()/len(df)*100).round(1) for v in vars_clave],
    "Tipo"            : df[vars_clave].dtypes.values
})
print(f"\n{nan_resumen.to_string(index=False)}")
print(f"\n  ► NaN en espera_lag1: {nan_lag1} — 1 por CCAA × {n_ccaa} CCAA = {n_ccaa} esperados")
print(f"  ► NaN en espera_lag2: {nan_lag2} — 2 por CCAA × {n_ccaa} CCAA = {n_ccaa*2} esperados")

# ═══════════════════════════════════════════════════════════════════════════════
# 9. GUARDAR CSV FINAL
# ═══════════════════════════════════════════════════════════════════════════════
sep("9. GUARDANDO datos_tfg_final.csv")
df.to_csv(RUTA_SALIDA, index=False, encoding="utf-8-sig")
print(f"\n  ✓ Archivo guardado en:\n    {RUTA_SALIDA}")
print(f"  Dimensiones finales: {df.shape[0]} filas × {df.shape[1]} columnas")
print(f"\n  Columnas del dataset final:\n  {list(df.columns)}")

sep("AUDITORÍA COMPLETADA")
