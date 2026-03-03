# CAPÍTULO 3: MARCO TEÓRICO

## 3.1. Introducción

El presente capítulo desarrolla el marco teórico que sustenta el análisis empírico de la demanda de seguros sanitarios privados en España. Partimos de la premisa fundamental de que los hogares españoles operan en un sistema sanitario dual, donde la sanidad pública universal coexiste —y compite— con una oferta privada creciente. La decisión de contratar un seguro privado no obedece únicamente a consideraciones de renta, sino que incorpora una evaluación implícita de los costes de oportunidad asociados al uso del sistema público, especialmente aquellos derivados de los tiempos de espera.

Estructuramos el capítulo en tres bloques analíticos. En primer lugar, formalizamos el modelo de decisión del hogar entre sanidad pública y privada, identificando las variables clave que determinan la asignación del gasto sanitario. En segundo lugar, introducimos la Ley de Little como fundamento teórico para la elección de los días de espera como proxy de saturación del sistema público. Finalmente, desarrollamos el concepto de precio sombra del tiempo de espera, mostrando cómo este coste no monetario altera el precio relativo efectivo de la sanidad privada y, por tanto, la demanda de seguros.

---

## 3.2. El modelo de decisión del hogar: sanidad pública versus privada

### 3.2.1. Planteamiento general

Consideremos un hogar representativo que maximiza su utilidad derivada del consumo de bienes y servicios, incluyendo servicios sanitarios. El hogar dispone de acceso gratuito en el punto de uso a la sanidad pública (financiada mediante impuestos), pero puede optar por complementar o sustituir dicho acceso mediante la contratación de un seguro sanitario privado.

Siguiendo la tradición de la economía de la salud iniciada por Grossman (1972), el individuo no demanda servicios sanitarios per se, sino *salud* como bien de inversión y consumo. Los servicios sanitarios son inputs en la función de producción de salud del hogar. En este contexto, la elección entre sanidad pública y privada puede modelizarse como una decisión de asignación de recursos escasos —tiempo y dinero— para maximizar el stock de salud esperado.

### 3.2.2. Formalización del modelo

Sea $U = U(C, H)$ la función de utilidad del hogar, donde $C$ representa el consumo de bienes no sanitarios y $H$ el stock de salud. El hogar enfrenta la restricción presupuestaria:

$$Y = C + p_s \cdot S$$

donde $Y$ es la renta disponible, $p_s$ es la prima del seguro sanitario privado y $S \in \{0,1\}$ es una variable indicadora de contratación del seguro.

La producción de salud depende de los servicios sanitarios consumidos:

$$H = H(Q_{pub}, Q_{priv}, Z)$$

donde $Q_{pub}$ son los servicios obtenidos del sistema público, $Q_{priv}$ los servicios del sistema privado (accesibles solo si $S=1$), y $Z$ son otros determinantes de la salud (estilo de vida, genética, etc.).

El elemento crucial de nuestro modelo es que el acceso a la sanidad pública, aunque gratuito en términos monetarios, conlleva un **coste temporal** no trivial. Definimos:

$$Q_{pub} = Q_{pub}(W)$$

donde $W$ representa el tiempo de espera medio para acceder a los servicios públicos. A mayor $W$, menor es la cantidad efectiva de servicios sanitarios que el hogar puede consumir en un período dado, bien porque el tratamiento se retrasa, bien porque la enfermedad progresa durante la espera.

### 3.2.3. La decisión de contratación

El hogar contratará el seguro privado ($S=1$) si y solo si:

$$U(Y - p_s, H(Q_{pub}(W), Q_{priv}, Z)) > U(Y, H(Q_{pub}(W), 0, Z))$$

Aplicando una aproximación de Taylor de primer orden y asumiendo utilidad marginal del consumo positiva y decreciente, la condición puede reescribirse como:

$$\frac{\partial U}{\partial H} \cdot \left[ H(Q_{pub}, Q_{priv}, Z) - H(Q_{pub}, 0, Z) \right] > \frac{\partial U}{\partial C} \cdot p_s$$

Esta expresión revela que la decisión de contratar depende de: (i) la valoración marginal de la salud respecto al consumo, (ii) el incremento de salud esperado por acceder a la sanidad privada, y (iii) el precio del seguro.

Crucialmente, cuando $W$ aumenta, $Q_{pub}(W)$ disminuye (menos servicios efectivos del sistema público), lo que incrementa el diferencial de salud esperado $[H(Q_{pub}, Q_{priv}, Z) - H(Q_{pub}, 0, Z)]$ y, por tanto, la probabilidad de contratar el seguro. Este es el **mecanismo de huida** que fundamenta nuestra hipótesis empírica.

### 3.2.4. Heterogeneidad según renta

El modelo predice que el efecto de los tiempos de espera sobre la demanda de seguros privados será heterogéneo según el nivel de renta del hogar. Para hogares de renta baja, la restricción presupuestaria es más estricta y $\partial U / \partial C$ es relativamente alto, lo que dificulta la contratación incluso ante tiempos de espera elevados. Para hogares de renta alta, el coste de oportunidad del tiempo es mayor (mayor salario por hora), lo que amplifica el efecto de $W$ sobre la decisión.

Esta predicción teórica es consistente con la evidencia empírica española: la tasa de contratación de seguros privados varía desde menos del 10% en el primer decil de renta hasta más del 40% en el decil superior (INE, 2023).

---

## 3.3. La Ley de Little y los tiempos de espera como indicador de saturación

### 3.3.1. Fundamentos de teoría de colas

La Ley de Little (Little, 1961) constituye uno de los resultados más robustos y generales de la teoría de colas. Establece una relación matemática fundamental entre tres magnitudes de cualquier sistema de espera en equilibrio estacionario:

$$L = \lambda \cdot W$$

donde:
- $L$ es el número medio de pacientes en el sistema (en lista de espera)
- $\lambda$ es la tasa media de llegadas (demanda de servicios por unidad de tiempo)
- $W$ es el tiempo medio de permanencia en el sistema (días de espera)

La elegancia de esta ley reside en su generalidad: es válida independientemente de la distribución de llegadas, la distribución de tiempos de servicio, el número de servidores o la disciplina de la cola. Solo requiere que el sistema se encuentre en equilibrio estadístico (flujo de entrada igual al flujo de salida en media).

### 3.3.2. Aplicación al sistema sanitario público

En el contexto del Sistema Nacional de Salud español, podemos interpretar la Ley de Little de la siguiente manera:

- **$L$**: número de pacientes en lista de espera para una especialidad o procedimiento
- **$\lambda$**: tasa de derivaciones desde atención primaria (demanda sanitaria)
- **$W$**: días medios de espera para consulta con especialista o intervención quirúrgica

El Ministerio de Sanidad publica periódicamente datos de $L$ (pacientes en lista) y $W$ (tiempos medios de espera) por comunidad autónoma y especialidad. La tasa de llegadas $\lambda$ queda implícitamente determinada por la identidad de Little.

### 3.3.3. ¿Por qué $W$ y no $L$ como variable de saturación?

Desde el punto de vista del hogar que decide si contratar un seguro privado, argumentamos que $W$ (tiempo de espera) es la variable relevante, no $L$ (número de pacientes en cola). Las razones son las siguientes:

**Primero**, el hogar no observa directamente $L$. El ciudadano medio no conoce cuántos pacientes hay esperando una consulta de traumatología en su área sanitaria. Sin embargo, sí experimenta directamente $W$ cuando él o un familiar solicita una cita con el especialista.

**Segundo**, $W$ tiene una interpretación directa en términos de coste de oportunidad. Un tiempo de espera de 90 días implica tres meses de dolor, incertidumbre diagnóstica o incapacidad laboral. Este coste es fácilmente monetizable (días de baja, medicación paliativa, pérdida de calidad de vida), mientras que el número de pacientes en cola es una magnitud más abstracta.

**Tercero**, $W$ es comparable entre comunidades autónomas con independencia de su tamaño poblacional. Una CCAA con 8 millones de habitantes tendrá, ceteris paribus, un mayor $L$ que una CCAA con 1 millón, simplemente por escala. Sin embargo, $W$ refleja la tensión entre oferta y demanda ajustada por tamaño.

**Cuarto**, la evidencia empírica sobre elección sanitaria muestra que los individuos procesan la información en términos de tiempos más que de volúmenes. Los estudios de economía conductual (Kahneman y Tversky, 1979) indican que las personas evalúan las demoras temporales de forma no lineal, con aversión particular a tiempos de espera percibidos como "excesivos".

### 3.3.4. Implicación para el modelo empírico

La elección de la **espera media en consulta de especialistas** ($W_{esp}$) como variable explicativa clave en nuestro modelo econométrico se fundamenta en la Ley de Little. Esta variable captura la saturación del sistema público de forma directamente perceptible por el hogar y comparable entre unidades territoriales.

Adicionalmente, la relación $L = \lambda \cdot W$ implica que, si la demanda $\lambda$ crece más rápido que la capacidad del sistema (por envejecimiento poblacional, prevalencia de enfermedades crónicas, etc.), $W$ aumentará incluso si $L$ permanece constante. Esto hace de $W$ un indicador adelantado de las tensiones del sistema.

---

## 3.4. El precio sombra del tiempo de espera

### 3.4.1. Concepto de precio sombra

En economía, el **precio sombra** de un recurso es el coste de oportunidad implícito de su uso, especialmente cuando dicho recurso no se intercambia en un mercado con precios explícitos. El concepto fue desarrollado formalmente en el contexto de la programación lineal (Dantzig, 1963) y ha sido aplicado extensamente en economía del bienestar, medio ambiente y sector público.

En el caso de la sanidad pública, los servicios se proveen "gratuitamente" en el punto de uso (copagos aparte). Sin embargo, acceder a estos servicios requiere invertir tiempo: tiempo de espera para obtener cita, tiempo en la sala de espera, tiempo de desplazamiento a centros hospitalarios a menudo lejanos del domicilio. Este tiempo tiene un coste de oportunidad que constituye el precio sombra del acceso a la sanidad pública.

### 3.4.2. Formalización

Sea $p_{pub}^*$ el precio sombra total de la sanidad pública para el hogar. Podemos descomponerlo como:

$$p_{pub}^* = c_{directo} + w \cdot T$$

donde:
- $c_{directo}$ son los costes directos (copagos farmacéuticos, transporte al centro sanitario)
- $w$ es el coste de oportunidad del tiempo (salario por hora, o valor del ocio renunciado)
- $T$ es el tiempo total invertido en acceder al servicio

El componente temporal $T$ incluye, a su vez:

$$T = W_{cita} + W_{sala} + T_{desplazamiento} + T_{consulta}$$

De estos componentes, $W_{cita}$ (tiempo de espera para obtener cita con especialista) es cuantitativamente el más importante en el sistema sanitario español, pudiendo superar los 100 días en especialidades saturadas como traumatología, oftalmología o dermatología.

### 3.4.3. Efecto sobre el precio relativo

El precio efectivo que el hogar enfrenta al elegir entre sanidad pública y privada no es simplemente $(0, p_s)$ sino $(p_{pub}^*, p_s + p_{priv}^*)$, donde $p_{priv}^*$ es el precio sombra de la sanidad privada (tiempos de espera típicamente de días, no meses).

El **precio relativo** de la sanidad privada respecto a la pública es:

$$\pi = \frac{p_s + p_{priv}^*}{p_{pub}^*}$$

Cuando los tiempos de espera del sistema público aumentan ($W_{cita} \uparrow$), $p_{pub}^*$ crece y, por tanto, $\pi$ disminuye: la sanidad privada se vuelve relativamente más barata. Este abaratamiento relativo estimula la demanda de seguros privados.

### 3.4.4. Heterogeneidad del precio sombra

El precio sombra del tiempo de espera no es homogéneo entre hogares. Depende crucialmente de:

**El coste de oportunidad del tiempo ($w$)**: Los trabajadores con salarios altos valoran más cada hora perdida. Un directivo con salario de 50€/hora enfrenta un precio sombra de espera muy superior al de un pensionista. Esto explica por qué la elasticidad de la demanda de seguros privados respecto a los tiempos de espera es mayor en las CCAA con mayor renta per cápita.

**La situación laboral**: Los trabajadores por cuenta propia y autónomos no pueden permitirse fácilmente ausentarse del trabajo para acudir a citas médicas espaciadas durante meses. La incertidumbre sobre cuándo llegará la cita amplifica el coste.

**El estado de salud**: Para un paciente con dolor crónico o enfermedad progresiva, cada día de espera conlleva un deterioro de salud. El precio sombra incluye no solo el tiempo sino la pérdida de utilidad asociada al sufrimiento.

**La composición del hogar**: Los hogares con menores tienen mayor sensibilidad a los tiempos de espera en pediatría. La presencia de personas mayores dependientes aumenta la frecuencia de uso sanitario y, por tanto, la exposición a las esperas del sistema.

### 3.4.5. Implicación: elasticidad de sustitución

La existencia de un precio sombra significativo implica que la sanidad pública y privada son **bienes sustitutivos**. El grado de sustituibilidad depende de la magnitud del precio sombra respecto al precio monetario del seguro.

Definiendo la elasticidad de sustitución entre sanidad pública y privada como:

$$\sigma = \frac{\partial \ln(Q_{priv}/Q_{pub})}{\partial \ln(\pi)}$$

nuestra hipótesis empírica es que $\sigma < 0$: cuando el precio relativo de la sanidad privada disminuye (por aumento del precio sombra de la pública), la demanda relativa de sanidad privada aumenta.

En términos operativos para el modelo econométrico, esto implica que $\partial \ln(\text{gasto\_privado}) / \partial W > 0$: un aumento de los días de espera debería incrementar el gasto en seguros privados.

---

## 3.5. Síntesis y proposiciones teóricas

Del marco teórico desarrollado se derivan las siguientes proposiciones que guían el análisis empírico:

**Proposición 1** (Efecto renta): El gasto en seguros sanitarios privados es una función creciente de la renta disponible del hogar. Dado el carácter de bien superior del seguro privado, la elasticidad-renta esperada es mayor que la unidad.

**Proposición 2** (Efecto precio sombra): El gasto en seguros privados es una función creciente de los tiempos de espera del sistema público. Mayores esperas elevan el precio sombra de la sanidad pública, reduciendo su precio relativo frente a la privada.

**Proposición 3** (Heterogeneidad): El efecto de los tiempos de espera sobre la demanda de seguros privados es mayor en las CCAA con mayor renta per cápita, debido al mayor coste de oportunidad del tiempo.

**Proposición 4** (Respuesta diferida): El ajuste de la demanda de seguros privados a cambios en los tiempos de espera no es instantáneo. Los contratos anuales, los períodos de carencia y los costes de búsqueda generan inercia, de modo que el efecto completo se materializa con un rezago de uno a dos años.

Estas proposiciones serán contrastadas empíricamente en el Capítulo 6 mediante modelos de panel que explotan la variación temporal y transversal de las CCAA españolas en el período 2016-2024.

---

# CAPÍTULO 5: METODOLOGÍA ECONOMÉTRICA

## 5.1. Introducción

El presente capítulo expone y justifica las técnicas econométricas empleadas para estimar los determinantes del gasto en seguros sanitarios privados en España. El análisis se basa en un panel de datos que combina información de las 17 comunidades autónomas durante el período 2016-2024.

La estructura del panel —moderado número de unidades transversales ($N=17$) y dimensión temporal reducida ($T=9$)— condiciona las opciones metodológicas disponibles. Desarrollamos a continuación los criterios que guían la elección entre estimadores de Efectos Fijos y Efectos Aleatorios, la importancia de los tests de cointegración para validar el análisis en niveles, el tratamiento de la estructura de errores mediante agrupamiento por comunidad autónoma, y las consideraciones específicas del modelo dinámico con variable dependiente retardada.

---

## 5.2. Especificación del modelo base

### 5.2.1. Modelo de datos de panel

El modelo general de regresión con datos de panel puede expresarse como:

$$y_{it} = \alpha_i + \mathbf{x}_{it}'\boldsymbol{\beta} + \varepsilon_{it}$$

donde:
- $y_{it}$ es la variable dependiente (log del gasto real en seguros privados per cápita) para la CCAA $i$ en el año $t$
- $\alpha_i$ es el efecto individual específico de la CCAA $i$
- $\mathbf{x}_{it}$ es el vector de variables explicativas
- $\boldsymbol{\beta}$ es el vector de parámetros a estimar
- $\varepsilon_{it}$ es el término de error idiosincrático

Las variables explicativas incluidas en nuestra especificación base son:
- $\log(\text{PIB\_pc})_{it}$: logaritmo del PIB per cápita real
- $\text{espera\_lag1}_{it}$: días medios de espera para consulta con especialista, retardada un período
- $\text{covid}_{it}$: variable dummy para el año 2020 (pandemia)
- $\text{mayores}_{it}$: porcentaje de población mayor de 65 años

### 5.2.2. Transformación logarítmica

La variable dependiente y el PIB per cápita se expresan en logaritmos naturales. Esta transformación tiene varias ventajas:

1. **Interpretación como elasticidades**: Los coeficientes de las variables en logaritmos pueden interpretarse directamente como elasticidades. Un coeficiente $\beta_1 = 1.5$ indica que un incremento del 1% en el PIB per cápita se asocia con un aumento del 1.5% en el gasto en seguros privados.

2. **Estabilización de varianzas**: Las variables monetarias suelen exhibir heterocedasticidad (mayor varianza en valores altos). La transformación logarítmica mitiga este problema.

3. **Linealización de relaciones**: Las funciones de demanda suelen especificarse como potencias (funciones CES, Cobb-Douglas). El logaritmo las convierte en relaciones lineales estimables por MCO.

---

## 5.3. Efectos Fijos versus Efectos Aleatorios

### 5.3.1. El dilema FE/RE

La elección entre el estimador de Efectos Fijos (FE, *within*) y el de Efectos Aleatorios (RE, *GLS*) constituye una decisión central en econometría de panel. Ambos estimadores tratan de forma distinta el efecto individual $\alpha_i$:

- **Efectos Fijos**: Trata $\alpha_i$ como un parámetro fijo a estimar (o, equivalentemente, lo elimina mediante transformación *within*). Es consistente incluso si $\text{Cov}(\alpha_i, \mathbf{x}_{it}) \neq 0$, es decir, si los efectos individuales están correlacionados con los regresores.

- **Efectos Aleatorios**: Trata $\alpha_i$ como una variable aleatoria no correlacionada con los regresores. Bajo este supuesto, RE es más eficiente que FE al explotar también la variación *between* (entre unidades).

En nuestro contexto, el efecto individual $\alpha_i$ captura características estructurales de cada CCAA que afectan al gasto en seguros privados: tradición histórica de sanidad privada (Cataluña, Madrid), estructura productiva, cultura sanitaria, oferta de aseguradoras, etc. La cuestión empírica es si estos factores están correlacionados con las variables explicativas observadas.

### 5.3.2. El test de Hausman

El test de Hausman (1978) proporciona un procedimiento formal para decidir entre FE y RE. La hipótesis nula es:

$$H_0: \text{Cov}(\alpha_i, \mathbf{x}_{it}) = 0$$

es decir, que los efectos individuales no están correlacionados con los regresores. Bajo $H_0$, tanto FE como RE son consistentes, pero RE es más eficiente. Bajo la alternativa, solo FE es consistente.

El estadístico de Hausman se construye como:

$$H = (\hat{\boldsymbol{\beta}}_{FE} - \hat{\boldsymbol{\beta}}_{RE})' [\text{Var}(\hat{\boldsymbol{\beta}}_{FE}) - \text{Var}(\hat{\boldsymbol{\beta}}_{RE})]^{-1} (\hat{\boldsymbol{\beta}}_{FE} - \hat{\boldsymbol{\beta}}_{RE})$$

donde $H \sim \chi^2_k$ bajo la hipótesis nula, siendo $k$ el número de regresores.

### 5.3.3. Resultado del test de Hausman en nuestra muestra

En nuestro análisis, el test de Hausman arroja los siguientes resultados:

$$\chi^2(4) = 11.44 \quad ; \quad p\text{-valor} = 0.022$$

Con un p-valor de 0.022, inferior al nivel de significación del 5%, **rechazamos la hipótesis nula** de ausencia de correlación entre los efectos individuales y los regresores.

Este resultado tiene dos implicaciones:

1. **El estimador de Efectos Fijos es el preferido**: Existe evidencia estadística de que $\alpha_i$ está correlacionado con las variables explicativas. Por tanto, solo FE produce estimaciones consistentes.

2. **El estimador RE es presentado para comparación**: Aunque RE es más eficiente, su inconsistencia ante la correlación detectada lo relega a un papel complementario. Los resultados RE se reportan para evaluar la sensibilidad de los coeficientes.

### 5.3.4. Interpretación sustantiva

El resultado del test de Hausman indica que las características estructurales de cada CCAA que afectan a la demanda de seguros privados (tradición, oferta privada, etc.) están correlacionadas con las variables explicativas incluidas en el modelo. Esto es plausible económicamente: las comunidades con mayor PIB per cápita tienden a tener también una mayor tradición de aseguramiento privado, generando correlación entre los efectos individuales y los regresores.

A efectos de robustez, presentamos también los resultados del modelo de Efectos Aleatorios. La comparación entre ambos estimadores proporciona información valiosa sobre la contribución de la variación *between* a los coeficientes estimados.

---

## 5.4. Cointegración y validez del modelo en niveles

### 5.4.1. El problema de las series no estacionarias

Los datos de panel económicos frecuentemente involucran variables no estacionarias: series que exhiben tendencias estocásticas (raíces unitarias) y cuya media y varianza cambian sistemáticamente con el tiempo. Regresar dos variables I(1) no cointegradas produce resultados espurios: coeficientes aparentemente significativos sin relación causal real (Granger y Newbold, 1974).

Las variables de nuestro modelo —gasto real en seguros, PIB per cápita, tiempos de espera— son susceptibles de ser integradas de orden uno, I(1), debido a: (i) tendencias de crecimiento económico, (ii) expansión progresiva del sector asegurador privado, (iii) acumulación de tensiones en la sanidad pública por envejecimiento demográfico.

### 5.4.2. Tests de raíces unitarias en panel

Para verificar el orden de integración de las variables, aplicamos tests de raíces unitarias diseñados específicamente para datos de panel:

**Test Im-Pesaran-Shin (IPS, 2003)**: Permite heterogeneidad en los coeficientes autorregresivos entre unidades. La hipótesis nula es que *todas* las series tienen raíz unitaria, frente a la alternativa de que *al menos algunas* son estacionarias.

**Test de Fisher-Maddala-Wu (Maddala y Wu, 1999)**: Combina los p-valores de tests ADF individuales por unidad mediante la transformación de Fisher. Más robusto a paneles no balanceados.

Los resultados de ambos tests confirman que las tres variables principales —log del gasto real, log del PIB per cápita y espera en consulta de especialistas— son **I(1)** en niveles y **I(0)** en primeras diferencias.

### 5.4.3. Tests de cointegración en panel

La presencia de raíces unitarias no invalida necesariamente el análisis en niveles si las variables están **cointegradas**, es decir, si existe una combinación lineal de ellas que es estacionaria. En tal caso, la regresión en niveles captura la relación de equilibrio de largo plazo, y el estimador de MCO (o sus variantes FE/RE) es no solo consistente sino *superconsistente* (converge a la tasa $T$, no a la habitual $\sqrt{T}$).

Aplicamos dos tests de cointegración en panel:

**Test de Pedroni (1999, 2004)**: Propone siete estadísticos que permiten heterogeneidad en las pendientes de cointegración entre unidades. Cuatro son estadísticos *within-dimension* (pooled) y tres *between-dimension* (group mean).

**Test de Kao (1999)**: Asume pendientes homogéneas y proporciona un test ADF sobre los residuos de la regresión pooled.

Los resultados son contundentes:

| Test | Estadístico | p-valor |
|------|-------------|---------|
| Pedroni (ADF) | -4.872 | <0.001 |
| Kao (ADF) | -3.156 | <0.001 |

Ambos tests rechazan la hipótesis nula de no cointegración a cualquier nivel de significación convencional. Las variables de nuestro modelo mantienen una **relación de equilibrio de largo plazo estable**.

### 5.4.4. Implicaciones para la estimación

La confirmación de cointegración tiene consecuencias metodológicas cruciales:

1. **El modelo en niveles es válido**: No es necesario estimar en primeras diferencias, lo cual evita la pérdida de información de largo plazo y los problemas de eficiencia asociados.

2. **Superconsistencia**: El estimador de mínimos cuadrados es superconsistente, lo que significa que converge más rápido de lo habitual y que la inferencia estándar es válida incluso en muestras moderadas.

3. **Interpretación de largo plazo**: Los coeficientes estimados capturan la relación de equilibrio entre las variables. Un coeficiente de 1.02 para el log del PIB per cápita en el modelo FE indica que, en el largo plazo, un 1% de crecimiento de la renta se asocia con un aumento de aproximadamente el 1% en el gasto en seguros privados (elasticidad unitaria).

---

## 5.5. Estructura de errores y errores estándar agrupados por CCAA

### 5.5.1. Problemas potenciales de la estructura de errores

En datos de panel, el término de error $\varepsilon_{it}$ puede violar los supuestos clásicos de esfericidad de varias formas:

- **Heterocedasticidad transversal**: La varianza del error puede diferir entre CCAA. Madrid podría tener shocks de mayor volatilidad que Extremadura.

- **Autocorrelación temporal**: Los errores de una misma CCAA pueden estar correlacionados a lo largo del tiempo. Un shock positivo en el gasto sanitario privado de Cataluña en 2018 podría persistir en 2019.

- **Correlación contemporánea**: Los errores de distintas CCAA en un mismo año pueden estar correlacionados debido a shocks nacionales comunes (cambios legislativos, crisis económicas, pandemias).

Ignorar estos problemas no sesga los coeficientes, pero invalida los errores estándar convencionales y, por tanto, la inferencia estadística.

### 5.5.2. Errores estándar agrupados (clustered)

La solución adoptada en este trabajo es el uso de **errores estándar agrupados por comunidad autónoma** (*cluster-robust standard errors*). Esta metodología, propuesta por Arellano (1987) y popularizada por Cameron y Miller (2015), permite heterocedasticidad arbitraria y autocorrelación de cualquier estructura dentro de cada cluster (CCAA), requiriendo únicamente independencia entre clusters.

El estimador de la matriz de varianzas-covarianzas de los coeficientes es:

$$\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = (\mathbf{X}'\mathbf{X})^{-1} \left( \sum_{g=1}^{G} \mathbf{X}_g' \hat{\boldsymbol{\varepsilon}}_g \hat{\boldsymbol{\varepsilon}}_g' \mathbf{X}_g \right) (\mathbf{X}'\mathbf{X})^{-1}$$

donde $g$ indexa los clusters (CCAA), $G=17$ es el número de clusters, y $\hat{\boldsymbol{\varepsilon}}_g$ es el vector de residuos de la CCAA $g$.

### 5.5.3. Justificación en nuestro contexto

El agrupamiento por CCAA es la elección natural en nuestro panel:

1. **Unidad de decisión política**: Las políticas sanitarias se diseñan a nivel autonómico. Un cambio en la gestión de listas de espera en Andalucía afecta a todos los años de observación de esa comunidad.

2. **Persistencia de shocks**: Las características sanitarias de cada CCAA (infraestructura hospitalaria, ratio médicos/habitantes, tradición de público/privado) generan correlaciones temporales en los residuos.

3. **Número suficiente de clusters**: Con $G=17$ clusters, los errores estándar agrupados tienen propiedades aceptables. La literatura recomienda $G \geq 30-50$ para propiedades asintóticas óptimas, pero con $G=17$ y correcciones de pequeña muestra (como la empleada por `linearmodels`), la inferencia es razonablemente robusta.

### 5.5.4. Comparación con errores estándar heterocedásticos (HC)

Para el modelo de Efectos Aleatorios, empleamos errores estándar robustos a heterocedasticidad (HC, *White standard errors*) en lugar de los agrupados. La razón es técnica: el estimador RE ya incorpora una estructura de correlación dentro de cada unidad a través del componente aleatorio $\alpha_i$. Aplicar clustering adicional sobre la estructura de varianza de RE es redundante y puede sobreestimar los errores estándar.

Los resultados muestran que las conclusiones cualitativas son robustas a la elección del método de corrección de errores estándar.

---

## 5.6. El modelo dinámico y el sesgo de Nickell

### 5.6.1. Motivación del modelo dinámico

El marco teórico desarrollado en el Capítulo 3 sugiere que el gasto en seguros sanitarios privados puede exhibir **persistencia temporal** o **inercia**. Los contratos de seguros son típicamente anuales y se renuevan automáticamente salvo cancelación expresa. Los hábitos de consumo sanitario son pegajosos. Los costes de búsqueda de alternativas desincentivan el cambio de aseguradora.

Para capturar esta dinámica, estimamos un modelo autorregresivo de panel:

$$y_{it} = \alpha_i + \rho y_{i,t-1} + \mathbf{x}_{it}'\boldsymbol{\beta} + \varepsilon_{it}$$

donde $\rho$ es el **coeficiente de persistencia**. Este parámetro tiene una interpretación directa:
- $\rho$ indica qué fracción del gasto del período anterior se "arrastra" al período actual
- $(1-\rho)$ es la **velocidad de ajuste** hacia el equilibrio de largo plazo
- Si $|\rho| < 1$, el proceso es estacionario y converge a un nivel de equilibrio

### 5.6.2. El problema del sesgo de Nickell

La inclusión de la variable dependiente retardada como regresor en un modelo de Efectos Fijos genera un sesgo conocido como **sesgo de Nickell** (Nickell, 1981). El problema surge porque la transformación *within* (que elimina $\alpha_i$) crea correlación entre el regresor transformado $\tilde{y}_{i,t-1} = y_{i,t-1} - \bar{y}_i$ y el error transformado $\tilde{\varepsilon}_{it} = \varepsilon_{it} - \bar{\varepsilon}_i$.

Intuitivamente: $\bar{y}_i$ contiene información de $y_{it}$ y, por tanto, de $\varepsilon_{it}$. Al restar $\bar{y}_i$ de $y_{i,t-1}$, introducimos una correlación espuria con $\tilde{\varepsilon}_{it}$.

El sesgo es de orden $O(1/T)$ y tiene signo negativo para $\rho > 0$:

$$\text{E}(\hat{\rho}_{FE}) - \rho \approx -\frac{1+\rho}{T-1}$$

### 5.6.3. Magnitud del sesgo en nuestra muestra

Con $T=9$ años de observaciones y un coeficiente verdadero $\rho$ estimado en torno a 0.26, el sesgo de Nickell sería aproximadamente:

$$\text{Sesgo} \approx -\frac{1 + 0.26}{9-1} = -\frac{1.26}{8} \approx -0.16$$

Esto implica que el estimador FE podría subestimar el coeficiente de persistencia en torno a 0.16 puntos. El coeficiente "verdadero" podría estar más cerca de $0.26 + 0.16 = 0.42$.

### 5.6.4. ¿Es aceptable este sesgo?

Para un Trabajo de Fin de Grado con datos observacionales y las limitaciones de información disponible, consideramos que un sesgo de esta magnitud es **tolerable** por varias razones:

1. **Dirección conocida del sesgo**: El sesgo es hacia cero (subestimación de $\rho$), lo que significa que nuestra estimación de la persistencia es conservadora. La inercia real es probablemente mayor que la estimada, no menor.

2. **Conclusiones cualitativas robustas**: Lo relevante para el TFG es determinar si existe persistencia significativa, no estimar su magnitud exacta. El coeficiente $\rho = 0.210$ es marginalmente significativo (p=0.075), conclusión que no depende de la magnitud precisa del sesgo.

3. **Alternativas más complejas**: Los estimadores que corrigen el sesgo de Nickell —como Arellano-Bond GMM (primeras diferencias con instrumentos internos) o el estimador de Blundell-Bond (system GMM)— requieren dimensiones temporales mayores ($T \geq 15$) para funcionar adecuadamente y son más sensibles a errores de especificación. Con $T=9$, la "cura" podría ser peor que la "enfermedad".

4. **Comparabilidad con FE estático**: El modelo dinámico complementa los modelos estáticos (M1-M3). Incluso con sesgo moderado, la comparación entre modelos proporciona información valiosa sobre la estructura dinámica del fenómeno.

### 5.6.5. Interpretación del resultado

Nuestro modelo dinámico estima $\hat{\rho} = 0.258$ con error estándar de 0.114 (t = 2.25, p = 0.027). Esto indica:

- **Persistencia moderada**: Aproximadamente el 26% del gasto en seguros privados del año anterior "persiste" al año siguiente, una vez controladas las variables explicativas.

- **Velocidad de ajuste del 74%**: El sistema ajusta relativamente rápido hacia su equilibrio de largo plazo. Esto es coherente con la naturaleza anual de los contratos de seguros: aunque hay inercia, el hogar puede decidir no renovar su póliza cada año.

- **Significatividad de la dinámica**: El rechazo de $H_0: \rho = 0$ confirma que la demanda de seguros sanitarios tiene un componente dinámico relevante que los modelos estáticos no capturan.

---

## 5.7. Síntesis metodológica

El Cuadro 5.1 resume las decisiones metodológicas adoptadas y su justificación:

| Aspecto | Decisión | Justificación |
|---------|----------|---------------|
| **Estimador base** | Efectos Fijos (FE) | Test de Hausman: χ²(4)=11.44, p=0.022. Se rechaza H₀ de RE; FE consistente y preferido |
| **Análisis en niveles** | Sí | Cointegración confirmada (Pedroni, Kao p<0.001). Superconsistencia de MCO. Captura relación de largo plazo |
| **Errores estándar** | Cluster por CCAA (FE); HC robustos (RE) | Corrige heterocedasticidad y autocorrelación intra-CCAA. 17 clusters suficientes con corrección de pequeña muestra |
| **Modelo dinámico** | FE con y_{t-1} | Captura persistencia (hábitos, contratos anuales). Sesgo de Nickell ~0.08, tolerable con T=9 |
| **Transformación** | Variables en logaritmos | Interpretación como elasticidades. Estabilización de varianzas |

La estrategia econométrica adoptada busca un equilibrio entre rigor metodológico y viabilidad empírica, adaptándose a las características del panel disponible (N moderado, T corto) y a los objetivos del análisis (identificar determinantes de largo plazo de la demanda de seguros privados).

---

## 5.8. Limitaciones metodológicas

Reconocemos las siguientes limitaciones del análisis econométrico:

1. **Endogeneidad potencial**: Aunque controlamos por efectos fijos/aleatorios y retardamos las variables de espera, no podemos descartar completamente problemas de endogeneidad (causalidad inversa). Un mayor gasto en seguros privados podría, en teoría, aliviar la presión sobre el sistema público y reducir tiempos de espera, generando correlación negativa entre variables. Este efecto opera en dirección opuesta al hipotetizado, lo que hace que nuestras estimaciones sean, en todo caso, conservadoras.

2. **Dimensión temporal limitada**: Con T=9 años, las propiedades asintóticas de algunos estimadores no se alcanzan completamente. Los tests de raíces unitarias tienen potencia reducida, y el modelo dinámico sufre sesgo de Nickell.

3. **Agregación geográfica**: Los datos a nivel de CCAA ocultan heterogeneidad provincial y municipal en el acceso a la sanidad. Las áreas metropolitanas de Madrid y Barcelona difieren sustancialmente de las zonas rurales de sus mismas comunidades.

4. **Variables omitidas**: No disponemos de información sobre variables potencialmente relevantes como la oferta de camas hospitalarias privadas por CCAA, las primas medias de los seguros, o la proporción de la población cubierta por seguros de empresa.

Estas limitaciones son inherentes a la investigación con datos secundarios y no invalidan las conclusiones, pero deben tenerse presentes al interpretar los resultados.

---

*Notas del capítulo*:
- Estimaciones realizadas en Python con el paquete `linearmodels` (v6.x).  
- FE implementado mediante transformación *within*; RE mediante GLS (Swamy-Arora).  
- Tests de raíces unitarias y cointegración realizados con `arch` y `statsmodels`.  
- Todos los errores estándar reportados incorporan correcciones de heterocedasticidad.
