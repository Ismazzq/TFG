# Diagnóstico de Estacionariedad y Cointegración en Panel

**Dataset:** datos_tfg_final.csv  |  N=17, T=9  |  Período 2016–2024

---

## 1. Tests de Raíz Unitaria en Niveles

> **H₀ (IPS / Maddala-Wu):** Todas las series del panel tienen raíz unitaria (no estacionarias)  
> **H₁ (IPS):** Una fracción de las series es estacionaria  
> Rechazo si **p-value < 0.05** (IPS: cola izquierda)  

### Variable: `log_gasto_real` — Log Gasto Real Seguros (€ p.p.)

| Test | Estadístico | p-value | Decisión 5% |
|------|------------|---------|-------------|
| IPS (W) | 1.9722 | 0.9757 | ❌ No rechaza H₀ (I(1)) |
| Maddala-Wu (χ²) | 20.6368 | 0.9654 | ❌ No rechaza H₀ (I(1)) |

<details><summary>ADF individuales por CCAA</summary>

| CCAA | t-stat | p-value |
|------|--------|---------|
| andalucia | -0.9802 | 0.7604 |
| aragon | -0.5945 | 0.8722 |
| asturias | -0.4626 | 0.8991 |
| canarias | 0.3581 | 0.9799 |
| cantabria | -2.1067 | 0.2418 |
| castilla y leon | -0.0910 | 0.9503 |
| castilla-la mancha | -0.3258 | 0.9218 |
| cataluna | -2.0238 | 0.2762 |
| comunidad valenciana | -0.0129 | 0.9575 |
| extremadura | -0.0506 | 0.9541 |
| galicia | -0.5906 | 0.8731 |
| islas baleares | -2.7485 | 0.0660* |
| la rioja | -0.9338 | 0.7766 |
| madrid | -1.3615 | 0.6006 |
| murcia | -2.1470 | 0.2260 |
| navarra | -1.8305 | 0.3654 |
| pais vasco | -1.6137 | 0.4760 |

</details>

### Variable: `log_pib_pc` — Log PIB per cápita (€)

| Test | Estadístico | p-value | Decisión 5% |
|------|------------|---------|-------------|
| IPS (W) | 4.1637 | 1.0000 | ❌ No rechaza H₀ (I(1)) |
| Maddala-Wu (χ²) | 7.5863 | 1.0000 | ❌ No rechaza H₀ (I(1)) |

<details><summary>ADF individuales por CCAA</summary>

| CCAA | t-stat | p-value |
|------|--------|---------|
| andalucia | -0.3026 | 0.9251 |
| aragon | -0.1009 | 0.9494 |
| asturias | -0.2445 | 0.9330 |
| canarias | -2.0320 | 0.2727 |
| cantabria | -0.2194 | 0.9362 |
| castilla y leon | -0.1394 | 0.9454 |
| castilla-la mancha | -0.3149 | 0.9234 |
| cataluna | -0.6373 | 0.8623 |
| comunidad valenciana | -0.3618 | 0.9163 |
| extremadura | 0.1535 | 0.9695 |
| galicia | -0.0374 | 0.9553 |
| islas baleares | -2.0274 | 0.2747 |
| la rioja | -0.5884 | 0.8736 |
| madrid | -0.3736 | 0.9144 |
| murcia | -0.1484 | 0.9444 |
| navarra | -0.3952 | 0.9109 |
| pais vasco | -0.4959 | 0.8928 |

</details>

### Variable: `esp_esp` — Días de Espera Especialistas

| Test | Estadístico | p-value | Decisión 5% |
|------|------------|---------|-------------|
| IPS (W) | -0.2575 | 0.3984 | ❌ No rechaza H₀ (I(1)) |
| Maddala-Wu (χ²) | 61.9812 | 0.0023*** | ✅ Rechaza H₀ (I(0)) |

<details><summary>ADF individuales por CCAA</summary>

| CCAA | t-stat | p-value |
|------|--------|---------|
| andalucia | -5.7025 | 0.0000*** |
| aragon | -2.1334 | 0.2313 |
| asturias | -0.3200 | 0.9226 |
| canarias | -0.6401 | 0.8617 |
| cantabria | -1.7441 | 0.4085 |
| castilla y leon | -1.2717 | 0.6420 |
| castilla-la mancha | -1.0045 | 0.7516 |
| cataluna | -2.7561 | 0.0648* |
| comunidad valenciana | -1.1671 | 0.6876 |
| extremadura | -1.6613 | 0.4511 |
| galicia | -2.6582 | 0.0816* |
| islas baleares | -0.4918 | 0.8936 |
| la rioja | -0.1845 | 0.9403 |
| madrid | -0.5290 | 0.8862 |
| murcia | -0.6138 | 0.8678 |
| navarra | -0.0143 | 0.9573 |
| pais vasco | -4.0345 | 0.0012*** |

</details>

---

## 2. Tests en Primeras Diferencias

> Si las variables son I(1), sus primeras diferencias deben ser I(0).  

### Δ`log_gasto_real`

| Test | Estadístico | p-value | Decisión 5% |
|------|------------|---------|-------------|
| IPS (W) | -6.4169 | 0.0000*** | ✅ Rechaza H₀ → I(1) confirmado |
| Maddala-Wu (χ²) | 156.7752 | 0.0000*** | ✅ Rechaza H₀ → I(1) confirmado |

### Δ`log_pib_pc`

| Test | Estadístico | p-value | Decisión 5% |
|------|------------|---------|-------------|
| IPS (W) | -1.9049 | 0.0284** | ✅ Rechaza H₀ → I(1) confirmado |
| Maddala-Wu (χ²) | 42.3721 | 0.1535 | ❌ No rechaza H₀ |

### Δ`esp_esp`

| Test | Estadístico | p-value | Decisión 5% |
|------|------------|---------|-------------|
| IPS (W) | -5.1957 | 0.0000*** | ✅ Rechaza H₀ → I(1) confirmado |
| Maddala-Wu (χ²) | 114.4394 | 0.0000*** | ✅ Rechaza H₀ → I(1) confirmado |

---

## 3. Tests de Cointegración de Pedroni (1999, 2004)

> **H₀:** No cointegración para todos los paneles  
> **H₁:** Cointegración (al menos para algunos paneles)  
> Modelo estimado: `log_gasto_real = αᵢ + β₁·log_pib_pc + β₂·esp_esp + εᵢₜ`  

| Test | Estadístico | p-value | Decisión 5% |
|------|------------|---------|-------------|
| Pedroni Group-ADF (Z) | -4.1838 | 0.0000*** | ✅ Cointegración |
| Maddala-Wu (residuos) | 154.9940 (χ²) | 0.0000*** | ✅ Cointegración |

**Coeficientes medios de la ecuación de largo plazo:**

| Variable | Media β | Std |
|----------|---------|-----|
| log_pib_pc | 0.8181 | 1.2596 |
| esp_esp | 0.000945 | 0.004805 |

---

## 4. Test de Cointegración de Kao (1999)

> El test de Kao es más restrictivo: impone coeficientes homogéneos (H₁ restringida).  
> H₀: No cointegración  
> Estadístico: ADF sobre residuos de regresión within-panel  

| Test | t-stat | p-value approx. | VC 5% | Decisión |
|------|--------|----------------|-------|---------|
| Kao ADF | -8.0736 | 0.0000*** | -1.96 | ✅ Cointegración |

---

## 5. Resumen de Órdenes de Integración

| Variable | IPS Niveles p | MW Niveles p | IPS Δ p | MW Δ p | Orden |
|----------|--------------|-------------|---------|--------|-------|
| `log_gasto_real` | 0.9757 | 0.9654 | 0.0000*** | 0.0000*** | **I(1)** |
| `log_pib_pc` | 1.0000 | 1.0000 | 0.0284** | 0.1535 | **I(1)** |
| `esp_esp` | 0.3984 | 0.0023*** | 0.0000*** | 0.0000*** | **I(1)** |

---

## 6. Conclusión Técnica y Recomendación de Modelo


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

---

### Notas metodológicas

- **Período muestral corto** (T=9): los tests de panel tienen mayor potencia que los univariados,
  pero con T=9 el poder sigue siendo limitado. Los resultados deben interpretarse con cautela.
- **IPS (2003)**: estadístico W normalizado, valores tabulados para T=10 usados como aproximación.
- **Maddala-Wu (1999)**: test no paramétrico combinado (Fisher), robusto a T cortos.
- **Pedroni (1999, 2004)**: residuos de la regresión de cointegración individual, estadístico Group-ADF.
- **Kao (1999)**: coeficientes homogéneos (within), ADF pooled sobre residuos.
- `***` p<0.01  `**` p<0.05  `*` p<0.10
