# Resultados de las Regresiones de Panel — TFG Econometría de la Salud

**Variable dependiente:** `log_gasto_real` (Log Gasto Real en Seguros Privados, €pp)  
**Período:** 2016–2024  |  **17 CCAA** (con datos faltantes)  
**Errores estándar:** Robustos cluster por CCAA  

---

## Modelo 1: Especificación con 1 retardo de espera

$$\log(\text{gasto})_{it} = \alpha_i + \beta_1 \log(\text{pib\_pc})_{it} + \beta_2 \text{espera}_{i,t-1} + \beta_3 \text{covid}_{it} + \beta_4 \text{pob65}_{it} + \varepsilon_{it}$$

### Test de Hausman: FE vs RE

| Estadístico | gl | p-value | Decisión |
|-------------|----|---------|---------|

| χ² = 11.4388 | 4 | 0.0221** | Se prefiere **FE** (FE consistente) |

---
## Modelo 2: Especificación con 2 retardos de espera

$$\log(\text{gasto})_{it} = \alpha_i + \beta_1 \log(\text{pib})_{it} + \beta_2 \text{espera}_{i,t-1} + \beta_3 \text{espera}_{i,t-2} + \beta_4 \text{covid}_{it} + \beta_5 \text{pob65}_{it} + \varepsilon_{it}$$

### Test de Wald: β(lag1) = β(lag2) = 0

| Test | χ²(2) | p-value | Decisión |
|------|-------|---------|----------|

| Wald | 0.3879 | 0.8237 | No significativos conjuntamente |

---
## Modelo 3: 1 retardo espera + Log Gasto en seguros del año anterior

$$\log(\text{gasto})_{it} = \alpha_i + \beta_1 \log(\text{pib})_{it} + \beta_2 \text{espera}_{i,t-1} + \rho \log(\text{gasto})_{i,t-1} + \beta_3 \text{covid}_{it} + \beta_4 \text{pob65}_{it} + \varepsilon_{it}$$

---
## Modelo 1-U: Especificación con dummy umbral (espera > 100 días)

$$\log(\text{gasto})_{it} = \alpha_i + \beta_1 \log(\text{pib})_{it} + \beta_2 \mathbf{1}_{\text{espera}>100} + \beta_3 \text{covid}_{it} + \beta_4 \text{pob65}_{it} + \varepsilon_{it}$$

---
## Modelo 3-U: Dummy umbral + Log Gasto en seguros anterior

$$\log(\text{gasto})_{it} = \alpha_i + \beta_1 \log(\text{pib})_{it} + \beta_2 \mathbf{1}_{\text{espera}>100} + \rho \log(\text{gasto})_{i,t-1} + \beta_3 \text{covid}_{it} + \beta_4 \text{pob65}_{it} + \varepsilon_{it}$$


---
## Tabla Comparativa

| Variable | M1-FE | M1-RE* | M2-FE | M3-FE | M1-U | M3-U |
|----------|-------|--------|-------|-------|------|------|
| Constante | -5.1640* | -9.2143*** | -4.9325* | -5.1925* | -6.0774** | -5.7288* |
| Log PIB pc | +1.0151*** | +1.5414*** | +0.9656*** | +0.9246** | +1.1367*** | +1.0014*** |
| Espera esp. (lag 1) | +0.0002 | +0.0005 | -0.0001 | -0.0000 | — | — |
| Espera esp. (lag 2) | — | — | +0.0003 | — | — | — |
| Dummy espera > 100d (t-1) | — | — | — | — | +0.0926** | +0.0558** |
| Log Gasto seguros (t-1) | — | — | — | +0.2104* | — | +0.2010* |
| Dummy COVID-19 | +0.0906 | +0.1657*** | +0.0888 | +0.0780 | +0.1063* | +0.0880 |
| Pob. > 65 años (%) | +0.0045 | -0.0608*** | +0.0176 | -0.0018 | -0.0114 | -0.0118 |

| **Estadísticos** |  |  |  |  |  |  |
| N | 118 | 118 | 101 | 116 | 118 | 116 |
| R² overall | 0.2816 | 0.5484 | 0.2002 | 0.5841 | 0.3895 | 0.6271 |

*Nota: * indica modelo preferido por test de Hausman. Errores robustos cluster.*

---
## Resumen de Hipótesis

| Hipótesis | Variable | Coef. | p-value | Resultado |
|-----------|----------|-------|---------|-----------|
| H1: Renta | log_pib_pc | +1.0151 | 0.0070*** | Confirmada |
| H2: Espera | espera_lag1 | +0.0002 | 0.7691 | Parcialmente confirmada (signo correcto) |
| H3: COVID | covid | +0.0906 | 0.1269 | No significativo |
| H4: Umbral | espera_alta_lag1 | +0.0926 | 0.0168** | Confirmada |
| H5: Inercia | log_g_seguros_lag1 | +0.2104 | 0.0748* | No confirmada |