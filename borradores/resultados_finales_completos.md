# Resultados Finales Completos — TFG Econometría de la Salud

> **Variable dependiente:** `log_gasto_real` (log del gasto real en seguros privados €/p.p.)  
> **Panel:** N=17 CCAA, T=2016–2024  |  Estimación: `linearmodels` (Python)  
> **Errores estándar:** Cluster por CCAA (FE) · Robustos HC (RE)  

---

## Tabla Comparativa de los 5 Modelos

| Variable | M1-FE | M1-RE | M2-FE | M3-FE | M1-U | M3-U |
|---|---|---|---|---|---|---|
| **Constante** | -5.1640* | -9.2143*** | -4.9325* | -5.1925* | -6.0774** | -5.7288* |
| **Log PIB pc** | +1.0151*** | +1.5414*** | +0.9656*** | +0.9246** | +1.1367*** | +1.0014*** |
| | (0.3687) | (0.2082) | (0.3397) | (0.4364) | (0.3443) | (0.3551) |
| **Espera esp. (lag 1)** | +0.0002 | +0.0005 | -0.0001 | -0.0000 | — | — |
| | (0.0006) | (0.0006) | (0.0006) | (0.0006) | | |
| **Espera esp. (lag 2)** | — | — | +0.0003 | — | — | — |
| | | | (0.0005) | | | |
| **Dummy espera > 100d (t-1)** | — | — | — | — | +0.0926** | +0.0558** |
| | | | | | (0.0381) | (0.0271) |
| **Log Gasto seguros (t-1)** | — | — | — | +0.2104* | — | +0.2010* |
| | | | | (0.1165) | | (0.1133) |
| **Dummy COVID-19** | +0.0906 | +0.1657*** | +0.0888 | +0.0780 | +0.1063* | +0.0880 |
| | (0.0586) | (0.0511) | (0.0575) | (0.0572) | (0.0586) | (0.0550) |
| **Pob. > 65 años (%)** | +0.0045 | -0.0608*** | +0.0176 | -0.0018 | -0.0114 | -0.0118 |
| | (0.0519) | (0.0225) | (0.0535) | (0.0476) | (0.0429) | (0.0404) |
| **R² within** | 0.3274 | — | 0.3475 | 0.3688 | 0.3524 | 0.3774 |
| **R² overall** | 0.2816 | 0.5484 | 0.2002 | 0.5841 | 0.3895 | 0.6271 |
| **Observaciones** | 118 | 118 | 101 | 116 | 118 | 116 |
| **CCAA** | 17 | 17 | 17 | 17 | 17 | 17 |
| **Efectos Fijos** | SÍ | NO | SÍ | SÍ | SÍ | SÍ |
| **SE** | Cluster | HC | Cluster | Cluster | Cluster | Cluster |

> `***` p<0.01  `**` p<0.05  `*` p<0.10 · SE en paréntesis  
> Test de Hausman: χ²(4)=11.44, p=0.022 → **Se prefiere FE** (FE consistente)

---

## Tests de Especificación

### Test de Hausman: FE vs RE

| Estadístico | gl | p-value | Decisión |
|-------------|----|---------|---------|
| χ² = 11.4388 | 4 | 0.0221** | Se prefiere **FE** |

**Interpretación:** Se rechaza H₀ (RE eficiente) al 5%. Existe evidencia de correlación entre los efectos individuales y los regresores. Las estimaciones FE son consistentes y preferidas.

### Test de Wald: Significatividad conjunta de retardos (M2)

| Test | χ²(2) | p-value | Decisión |
|------|-------|---------|----------|
| Wald | 0.3879 | 0.8237 | No significativos conjuntamente |

---

## Conclusiones Econométricas Finales

### 1. Renta y capacidad de pago (log PIB pc) — H1

El PIB per cápita es el determinante **más robusto y significativo** en todos los modelos (β ≈ 0.92–1.54). En el modelo FE preferido (β=1.02, p=0.007), la elasticidad es aproximadamente unitaria. En RE (β=1.54), el seguro privado se comporta como **bien superior**. **Hipótesis confirmada.**

### 2. Listas de espera — efecto diferido lineal (H2)

La espera en especialistas (lag1) no es significativa en M1-FE (coef.=+0.0002, p=0.769), y el **test de Wald conjunto** en M2 tampoco resulta significativo (χ²(2)=0.39, p=0.82). El efecto diferido lineal no queda confirmado. **Hipótesis no confirmada en su forma continua.**

### 3. Efecto umbral (no linealidad) — H4

La dummy de espera > 100 días es **significativa** en M1-U (coef.=+0.0926, p=0.017): cuando la espera supera los 100 días, el gasto en seguros privados se incrementa un **9,3%**. **Hipótesis confirmada.**

### 4. COVID-19 — H3

El año 2020 elevó el gasto en seguros privados ~9–17%. Significativo en RE (p<0.01, coef.=+0.166) y marginalmente en M1-U (p=0.075). En FE, el efecto es positivo pero no alcanza significación estadística convencional. **Hipótesis parcialmente confirmada** (dependiente del estimador).

### 5. Persistencia del gasto (M3-FE) — H5

ρ = 0.2104 (p=0.075): el coeficiente de la variable dependiente retardada es marginalmente significativo. Aproximadamente el **21% del nivel de gasto del año anterior persiste** al año siguiente. Existe inercia moderada debida a contratos anuales y hábitos de consumo. **Hipótesis parcialmente confirmada.**

Efecto de largo plazo del PIB: β^LP = 0.9246 / (1 - 0.2104) = **1.171**, coherente con el carácter de bien superior.

### Recomendación Final de Modelo para el TFG

| Criterio | Modelo recomendado |
|---------|-------------------|
| Parámetros de largo plazo | **M1-FE** (Hausman confirma FE consistente, β=1.02) |
| Dinámica acumulada de espera | **M2-FE** (Wald ns, retardos no significativos) |
| No linealidad umbral | **M1-U** (confirmado, δ=0.093**, p=0.017) |
| Persistencia del hábito | **M3-FE** (ρ=0.210*, marginalmente significativo) |
| **Modelo principal TFG** | **M1-FE** con robustez en M1-U y M3-FE |

---

### Resumen de Hipótesis

| Hipótesis | Variable | Coef. | p-value | Resultado |
|-----------|----------|-------|---------|-----------|
| H1: Renta | log_pib_pc (M1-FE) | +1.0151 | 0.0070*** | **Confirmada** |
| H2: Espera lineal | espera_lag1 (M1-FE) | +0.0002 | 0.7691 | No confirmada |
| H3: COVID | covid (M1-FE) | +0.0906 | 0.1269 | Parcialmente (RE sí significativo) |
| H4: Umbral | espera_alta_lag1 (M1-U) | +0.0926 | 0.0168** | **Confirmada** |
| H5: Inercia | log_g_seguros_lag1 (M3-FE) | +0.2104 | 0.0748* | Parcialmente confirmada |

---

### Notas metodológicas finales

- Estimación: `linearmodels 6.x` (Python). FE = within estimator; RE = GLS Swamy-Arora.
- SE: cluster por CCAA en FE (corrige autocorrelación intragrupo y heterocedasticidad); HC robustos en RE.
- Panel: 17 CCAA × 9 años (2016–2024). 153 observaciones teóricas.
- Muestra efectiva: N=118 (M1-FE, M1-RE, M1-U), N=101 (M2-FE), N=116 (M3-FE, M3-U).
- Datos: INE Encuesta de Presupuestos Familiares, Ministerio de Sanidad (Listas de Espera), IPC Sanidad (base 2025).
