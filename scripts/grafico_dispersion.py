"""
Gráfico de dispersión: log_pib_pc vs log_gasto_real
TFG — Econometría de la Salud
Capítulo 4: Datos y descripción empírica
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
import os

# ── Rutas ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "datos_tfg_final.csv")
OUT_PATH = os.path.join(BASE_DIR, "figuras", "scatter_pib_gasto.png")

# ── Carga de datos ─────────────────────────────────────────────────────────────
df = pd.read_csv(CSV_PATH).dropna(subset=["log_pib_pc", "log_gasto_real"])

# Paleta de color por año (gradiente temporal)
years = sorted(df["ano"].unique())
cmap = plt.cm.viridis
den = max(len(years) - 1, 1)
colors = {yr: cmap(i / den) for i, yr in enumerate(years)}
N = len(df)

# ── Regresión lineal (MCO simple) para línea de tendencia ─────────────────────
slope, intercept, r_value, p_value, se = stats.linregress(
    df["log_pib_pc"], df["log_gasto_real"]
)
x_line = np.linspace(df["log_pib_pc"].min() - 0.02,
                     df["log_pib_pc"].max() + 0.02, 200)
y_line = intercept + slope * x_line

# ── Figura ─────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6))

# Dispersión con color por año
for yr in years:
    sub = df[df["ano"] == yr]
    sc = ax.scatter(
        sub["log_pib_pc"], sub["log_gasto_real"],
        color=colors[yr], s=55, alpha=0.82,
        label=str(yr), zorder=3
    )

# Línea de tendencia OLS
trend_line, = ax.plot(
    x_line, y_line,
    color="#e63946", linewidth=2.2, linestyle="--",
    label=f"Tendencia OLS (β={slope:.3f}, R²={r_value**2:.3f})", zorder=4
)

# Etiquetas de CCAA extremas (outliers visibles)
threshold_lo = df["log_gasto_real"].quantile(0.08)
threshold_hi = df["log_gasto_real"].quantile(0.92)
for _, row in df.iterrows():
    if row["log_gasto_real"] < threshold_lo or row["log_gasto_real"] > threshold_hi:
        ax.annotate(
            row["ccaa"][:3],  # abreviatura 3 letras
            xy=(row["log_pib_pc"], row["log_gasto_real"]),
            xytext=(4, 3), textcoords="offset points",
            fontsize=6.5, color="#444", alpha=0.8
        )

# ── Leyenda única y ejes ──────────────────────────────────────────────────────
handles_yr = [plt.Line2D([0], [0], marker='o', color='w',
              markerfacecolor=colors[yr], markersize=7, label=str(yr))
              for yr in years]
all_handles = handles_yr + [plt.Line2D([0], [0], color="#e63946", linewidth=2.2,
                                       linestyle="--", label=trend_line.get_label())]
ax.legend(handles=all_handles, title="Año y tendencia", loc="upper left",
          fontsize=7.5, title_fontsize=8, ncol=3, framealpha=0.9)

ax.set_xlabel("Log PIB per cápita real (€)", fontsize=11)
ax.set_ylabel("Log gasto real en seguros privados (€/p.p.)", fontsize=11)
ax.set_title(
    "Gasto en seguros sanitarios privados y renta per cápita\n"
    f"17 CCAA · {years[0]}–{years[-1]}  (N={N} observaciones)",
    fontsize=12, fontweight="bold", pad=14
)
ax.grid(True, linestyle=":", alpha=0.5)
ax.set_facecolor("#f9f9f9")
fig.patch.set_facecolor("white")

# Nota al pie
fig.text(
    0.5, 0.01,
    "Fuentes: INE (EPF, Contabilidad Regional) · Deflactado por IPC Seguros (base=2025)",
    ha="center", fontsize=7.5, color="#555"
)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig(OUT_PATH, dpi=180, bbox_inches="tight")
print(f"Gráfico guardado en: {OUT_PATH}")
plt.close()

print(f"\nEstadístico de la regresión simple:")
print(f"  Pendiente (β): {slope:.4f}")
print(f"  Intercepto:    {intercept:.4f}")
print(f"  R²:            {r_value**2:.4f}")
print(f"  p-valor:       {p_value:.2e}")
print(f"  N observaciones: {N}")
