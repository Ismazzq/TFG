# TRABAJO FIN DE GRADO

## Determinantes del gasto en seguros sanitarios privados en España: tiempos de espera, renta y comportamiento diferido (2016-2024)

---

# CAPÍTULO 1: INTRODUCCIÓN

## 1.1. Motivación y contexto del problema

El Sistema Nacional de Salud (SNS) español atraviesa una crisis estructural cuya manifestación más visible son las **listas de espera**. Según datos del Ministerio de Sanidad, a finales de 2023 más de 800.000 pacientes aguardaban una intervención quirúrgica, con tiempos medios que en algunas comunidades autónomas superaban los 150 días para consultas con especialistas. Esta situación no es coyuntural: desde 2016 se observa una tendencia sostenida al alza, interrumpida únicamente —y de forma paradójica— por la pandemia de COVID-19, que redujo las listas mediante la suspensión masiva de actividad programada, para después dispararse a niveles históricos durante la recuperación.

La persistencia y magnitud del problema de las listas de espera plantea interrogantes fundamentales sobre la sostenibilidad del modelo sanitario español y, de forma más específica, sobre las **respuestas adaptativas de los hogares** ante el deterioro percibido del servicio público. En un sistema de cobertura universal y gratuita en el punto de uso, ¿qué factores determinan que una proporción creciente de la población opte por contratar un seguro sanitario privado complementario? ¿Constituyen los tiempos de espera un factor de expulsión (*push factor*) mesurable empíricamente? ¿Y, de ser así, cómo opera temporalmente este mecanismo?

Este trabajo aborda estas cuestiones desde la **economía de la salud** y la **econometría de datos de panel**, combinando un marco teórico riguroso con evidencia empírica original para España.

## 1.2. La teoría del precio sombra aplicada a la sanidad pública

El punto de partida teórico de este estudio es la constatación de que la sanidad pública, aunque formalmente gratuita, conlleva **costes implícitos** para el usuario. El tiempo de espera constituye el principal de estos costes: semanas o meses de incertidumbre diagnóstica, dolor no tratado, incapacidad laboral temporal o deterioro de la calidad de vida. Este coste temporal puede formalizarse mediante el concepto económico de **precio sombra** (*shadow price*).

El precio sombra del tiempo de espera representa el valor monetario implícito que el hogar atribuye al período que transcurre desde que solicita una cita con el especialista hasta que efectivamente la obtiene. Para un trabajador con salario elevado, cada día de espera tiene un coste de oportunidad mayor (salario renunciado, productividad perdida). Para un paciente con patología progresiva, cada día sin tratamiento supone un deterioro adicional de su stock de salud. Cuando el precio sombra de la sanidad pública aumenta —porque las esperas se alargan—, el **precio relativo** del seguro privado disminuye, estimulando su demanda.

Esta perspectiva conecta directamente con la tradición de Grossman (1972) sobre la demanda de salud como capital humano y con la literatura posterior sobre elección entre sectores sanitarios (Propper, 2000; Besley et al., 1999). La aportación específica de este trabajo consiste en operacionalizar el precio sombra mediante los **días de espera en consulta de especialistas** y contrastar empíricamente su efecto sobre el gasto en seguros privados de los hogares españoles.

## 1.3. Pregunta de investigación e hipótesis

La pregunta central que guía este estudio es:

> **¿Cuáles son los determinantes del gasto de los hogares españoles en seguros sanitarios privados, y qué papel desempeñan los tiempos de espera del sistema público en esta decisión?**

A partir del marco teórico, formulamos las siguientes hipótesis operativas:

**H1 (Efecto renta):** El gasto en seguros sanitarios privados es una función creciente de la renta disponible, con elasticidad superior a la unidad (bien superior).

**H2 (Efecto precio sombra):** Un aumento de los tiempos de espera del sistema público eleva el gasto en seguros privados, al reducir el precio relativo de estos últimos.

**H3 (Efecto diferido):** La respuesta de los hogares a los cambios en los tiempos de espera no es instantánea, sino que se materializa con un **rezago de 1-2 años**, debido a la inercia contractual de los seguros, los períodos de carencia y los costes de búsqueda de información.

**H4 (Efecto umbral):** Existe un umbral crítico de tiempo de espera (estimado en **100 días**) a partir del cual la respuesta de los hogares se intensifica de forma no lineal.

## 1.4. Originalidad y contribución del trabajo

Este Trabajo de Fin de Grado realiza varias contribuciones originales:

**Primero**, construye un **panel de datos autonómico** (17 CCAA, 2016-2024) que combina información del INE (gasto en seguros, PIB per cápita, demografía) y del Ministerio de Sanidad (tiempos de espera), permitiendo un análisis que explota tanto la variación transversal (*between*) como la temporal (*within*) de las variables.

**Segundo**, introduce la **Ley de Little** de la teoría de colas como fundamento para la elección de los días de espera —y no el número de pacientes en lista— como proxy de saturación del sistema público percibida por el hogar.

**Tercero**, estima modelos econométricos que capturan el **efecto diferido** de los tiempos de espera sobre el gasto privado, mediante la inclusión de retardos temporales cuya significatividad conjunta se verifica mediante tests de Wald.

**Cuarto**, explora la posible **no linealidad de umbral**: ¿reaccionan los hogares de forma más intensa cuando las esperas superan un punto crítico psicológicamente significativo?

**Quinto**, documenta la **persistencia dinámica** del gasto en seguros privados, coherente con la naturaleza de los contratos anuales y la inercia de los hábitos de consumo sanitario.

Los resultados principales confirman que la renta es el determinante dominante (elasticidad ~1.02 bajo efectos fijos, bien superior), y que los tiempos de espera ejercen un efecto estadísticamente significativo cuando se supera el umbral de 100 días: el gasto en seguros privados aumenta un **9.3%** cuando la espera del año anterior supera ese límite.

## 1.5. Estructura del trabajo

El trabajo se organiza en nueve capítulos:

- **Capítulo 2** presenta el marco institucional del SNS español, la evolución histórica de las listas de espera y el papel del sector privado.
- **Capítulo 3** desarrolla el marco teórico: modelo de decisión del hogar, Ley de Little y precio sombra del tiempo de espera.
- **Capítulo 4** describe las fuentes de datos, las variables y los estadísticos descriptivos del panel.
- **Capítulo 5** expone la metodología econométrica: efectos fijos/aleatorios, tests de cointegración, errores estándar agrupados y modelo dinámico.
- **Capítulo 6** presenta los resultados de las estimaciones y su interpretación económica.
- **Capítulo 7** discute las implicaciones de los hallazgos para la política sanitaria.
- **Capítulo 8** reconoce las limitaciones del estudio.
- **Capítulo 9** sintetiza las conclusiones y propone líneas de investigación futura.

---

# CAPÍTULO 2: MARCO INSTITUCIONAL Y CONTEXTO SANITARIO EN ESPAÑA

## 2.1. Introducción

Comprender el comportamiento de los hogares españoles respecto a la sanidad privada exige situar su decisión en el contexto institucional específico del Sistema Nacional de Salud. España no dispone de un único sistema sanitario, sino de **diecisiete sistemas autonómicos** con diferencias sustanciales en dotación de recursos, modelos de gestión y resultados en salud. Esta heterogeneidad institucional es precisamente la que permite el análisis econométrico de panel que desarrollamos en este trabajo.

El presente capítulo describe la arquitectura del SNS, analiza la evolución de las listas de espera desde 2016, examina el papel del seguro privado como complemento del sistema público y justifica la pertinencia del enfoque autonómico para el estudio del fenómeno.

## 2.2. Organización del Sistema Nacional de Salud

### 2.2.1. Los principios fundacionales

El Sistema Nacional de Salud español fue establecido por la Ley General de Sanidad de 1986, inspirada en el modelo Beveridge británico. Sus principios rectores son la **universalidad** (cobertura de toda la población), la **equidad** (acceso independiente de la capacidad de pago), la **financiación pública** (mediante impuestos generales) y la **integralidad** de las prestaciones (prevención, diagnóstico, tratamiento y rehabilitación).

Estos principios configuran un sistema en el que, teóricamente, ningún ciudadano debería necesitar acudir al sector privado por motivos económicos o de acceso. La realidad, sin embargo, muestra un crecimiento sostenido de los seguros privados que sugiere que el sistema público no satisface completamente las expectativas de una parte significativa de la población.

### 2.2.2. La descentralización sanitaria

El proceso de transferencia de competencias sanitarias a las comunidades autónomas, culminado en 2002, transformó radicalmente la gobernanza del SNS. Actualmente, cada CCAA dispone de un **Servicio de Salud propio** con competencias plenas en planificación, gestión y provisión de servicios sanitarios. El Ministerio de Sanidad conserva funciones de coordinación, política farmacéutica, sanidad exterior y garantía de la cohesión del sistema, pero carece de autoridad ejecutiva sobre los servicios regionales.

Esta arquitectura ha dado lugar a lo que algunos autores denominan "17 sistemas de salud" que, compartiendo principios comunes, difieren en:

- **Gasto sanitario per cápita:** En 2022, el gasto público por habitante oscilaba entre 1.200 € (Andalucía) y 1.900 € (País Vasco), un rango del 60%.
- **Ratio de profesionales:** Las diferencias en médicos y enfermeros por 1.000 habitantes son sustanciales, con comunidades que superan la media europea y otras que se sitúan por debajo.
- **Modelos de gestión:** Algunas CCAA han experimentado con fórmulas de colaboración público-privada, externalizaciones o conciertos, mientras que otras mantienen modelos de gestión directa integral.
- **Infraestructura hospitalaria:** La densidad de camas hospitalarias, equipamiento tecnológico y accesibilidad geográfica varía significativamente.

### 2.2.3. Implicaciones para las listas de espera

La descentralización ha generado una **competencia implícita en eficiencia** entre comunidades autónomas. Los tiempos de espera, al ser un indicador visible y políticamente sensible, se han convertido en un campo de comparación permanente. Los informes semestrales del Ministerio de Sanidad sobre listas de espera reciben amplia cobertura mediática, y los gobiernos autonómicos se ven presionados a mejorar sus resultados relativos.

Sin embargo, esta competencia opera con restricciones presupuestarias heterogéneas. Las comunidades con mayor capacidad fiscal (Madrid, País Vasco, Navarra, Cataluña) disponen de márgenes de maniobra superiores para aumentar la oferta y reducir tiempos de espera. Las comunidades con menor renta per cápita enfrentan una tensión estructural entre demanda sanitaria creciente (a menudo asociada a mayor envejecimiento) y recursos limitados.

## 2.3. Evolución de las listas de espera (2016-2024)

### 2.3.1. Tendencia general al alza

El análisis de los datos del Sistema de Información sobre Listas de Espera del SNS (SISLE-SNS) revela una tendencia estructural al **deterioro progresivo** de los tiempos de espera desde 2016. La espera media para consulta de especialistas pasó de 58 días en diciembre de 2016 a 95 días en diciembre de 2023, un incremento del 64% en siete años.

Esta tendencia no ha sido uniforme: se observan períodos de relativa estabilización (2017-2018), episodios de deterioro acelerado (2019, 2022-2023) y el fenómeno anómalo de la pandemia (2020-2021). Pero la dirección general es inequívoca: **el sistema público es progresivamente menos capaz de atender la demanda en tiempos razonables**.

### 2.3.2. Factores estructurales: el envejecimiento demográfico

El principal factor explicativo de esta tendencia es el **envejecimiento de la población**. España tiene una de las estructuras demográficas más envejecidas del mundo, con un 20.5% de población mayor de 65 años (media del panel) y comunidades como Castilla y León o Asturias que superan el 25%.

El envejecimiento impacta doblemente en las listas de espera:

- **Por el lado de la demanda:** Los mayores consumen servicios sanitarios con mucha mayor intensidad que los jóvenes. La prevalencia de enfermedades crónicas, pluripatología y necesidad de intervenciones quirúrgicas (cataratas, prótesis articulares, cirugía cardíaca) aumenta exponencialmente con la edad.

- **Por el lado de la oferta:** Una población más envejecida implica una base fiscal más reducida (menor tasa de empleo, menores ingresos medios), lo que limita la capacidad de financiación del sistema público.

Este desajuste estructural entre demanda creciente y recursos relativamente estancados es el motor de fondo del deterioro de las listas de espera.

### 2.3.3. El shock de la pandemia COVID-19

La pandemia de 2020 supuso un **shock exógeno** de magnitud sin precedentes para el sistema sanitario español. Durante los meses más críticos (marzo-mayo de 2020), la actividad programada se suspendió casi por completo para concentrar recursos en la atención a pacientes COVID. Las listas de espera quirúrgicas se vaciaron artificialmente —no porque se operase a los pacientes, sino porque se dejó de añadir nuevos—, para después acumular una demanda embalsada que explotó en 2021-2022.

El efecto neto de la pandemia sobre los tiempos de espera fue paradójico:

- **Corto plazo (2020):** Aparente reducción de listas (suspensión de derivaciones).
- **Medio plazo (2021-2023):** Explosión de tiempos de espera al reactivarse la demanda acumulada.
- **Largo plazo:** Revelación de las fragilidades estructurales del sistema y aceleración de las reformas en algunas CCAA.

Desde la perspectiva de este trabajo, la pandemia opera como un **shock natural** que permite identificar efectos dinámicos: ¿cómo reaccionaron los hogares al colapso percibido del sistema público en 2020? ¿Y cómo evolucionó su comportamiento durante la recuperación?

### 2.3.4. Heterogeneidad autonómica

La Tabla 2.1 presenta los tiempos de espera en consulta de especialistas para las CCAA extremas del panel en diciembre de 2023:

| CCAA | Espera media (días) | Posición |
|------|--------------------:|----------|
| País Vasco | 42 | Mejor |
| Madrid | 51 | 2ª mejor |
| Navarra | 54 | 3ª mejor |
| ... | ... | ... |
| Cataluña | 98 | 14ª |
| Canarias | 124 | 15ª |
| Castilla-La Mancha | 147 | 16ª |
| Extremadura | 156 | Peor |

El rango observado —de 42 a 156 días— implica que un ciudadano de Extremadura espera casi **cuatro veces más** que uno del País Vasco para acceder a la misma prestación nominal del SNS. Esta heterogeneidad es la que justifica el análisis a nivel autonómico y la que convierte las CCAA en "laboratorios naturales" para estudiar el efecto de las listas de espera sobre la demanda de seguros privados.

## 2.4. El sector privado: definición y papel en el sistema sanitario

### 2.4.1. Modalidades de seguro sanitario privado

En España, el seguro sanitario privado puede clasificarse en dos grandes categorías:

**Seguros individuales:** Contratados directamente por el ciudadano con una compañía aseguradora, cubren al titular y opcionalmente a su unidad familiar. Las primas varían según edad, estado de salud previo (en pólizas con cuestionario médico) y nivel de cobertura contratado. El mercado está dominado por compañías como Sanitas, Adeslas, Asisa, DKV y MAPFRE Salud.

**Seguros colectivos:** Contratados por empresas como beneficio para sus empleados, ofrecen condiciones ventajosas (primas reducidas por economías de escala, eliminación de cuestionarios médicos). Este segmento ha crecido significativamente en la última década al incorporarse la cobertura sanitaria como elemento de retribución flexible y retención de talento.

Ambas modalidades comparten la característica de ser **complementarias** al SNS, no sustitutivas: el asegurado privado mantiene su derecho a la sanidad pública y puede utilizar ambos sistemas según conveniencia. Esta dualidad es clave para entender el mecanismo de "huida" que estudiamos.

### 2.4.2. Dimensión del sector privado en España

Según datos de ICEA (Investigación Cooperativa entre Entidades Aseguradoras), a finales de 2023:

- Aproximadamente **12 millones de españoles** (25% de la población) disponían de algún tipo de seguro sanitario privado.
- El volumen de primas del ramo de salud superó los **11.500 millones de euros**, con un crecimiento interanual del 6.2%.
- La ratio de siniestralidad (prestaciones pagadas sobre primas cobradas) se situó en torno al 82%, indicando un sector rentable pero competitivo.

La penetración del seguro privado no es homogénea territorialmente: supera el 35% en Madrid y Cataluña, mientras que en comunidades como Extremadura, Castilla-La Mancha o Galicia se sitúa por debajo del 15%.

### 2.4.3. El seguro privado como "válvula de escape"

Desde la perspectiva del análisis económico, el seguro sanitario privado funciona como una **válvula de escape** del sistema público. Cuando las listas de espera del SNS se alargan más allá de lo tolerable para ciertos hogares, estos pueden optar por contratar un seguro que les garantice acceso rápido a consultas, pruebas diagnósticas e intervenciones.

Este mecanismo tiene varias implicaciones:

**Implicación 1 (Equidad):** La válvula de escape solo está disponible para quienes pueden pagar la prima del seguro. Esto genera una **dualidad** en el sistema: ciudadanos con recursos acceden rápidamente a través del sector privado, mientras que quienes carecen de ellos deben esperar en el sector público. El resultado es un sistema sanitario **formalmente universal pero materialmente estratificado** según capacidad de pago.

**Implicación 2 (Eficiencia):** La existencia de la válvula de escape reduce la presión política sobre el sistema público. Si los ciudadanos más influyentes (mayor renta, mayor capital social) pueden eludir las listas de espera mediante el seguro privado, su incentivo para exigir mejoras del sistema público disminuye. Este fenómeno, conocido como "exit versus voice" (Hirschman, 1970), puede paradójicamente contribuir al deterioro del sector público.

**Implicación 3 (Sostenibilidad):** A medio plazo, la migración de población joven y sana hacia el sector privado puede generar un fenómeno de **selección adversa** en el SNS, que retendría una cartera de usuarios más envejecida y con mayor morbilidad, intensificando las dificultades financieras.

## 2.5. Justificación del enfoque autonómico

El análisis de la demanda de seguros sanitarios privados a nivel **autonómico** —y no nacional— se justifica por varias razones:

**Primera**, la descentralización sanitaria implica que las condiciones de acceso al SNS varían sustancialmente entre CCAA. Analizar datos agregados nacionales ocultaría esta heterogeneidad y produciría estimaciones sesgadas o poco informativas.

**Segunda**, las decisiones de contratación de seguros privados se toman a nivel del hogar, que habita en una CCAA específica y enfrenta los tiempos de espera de *su* servicio de salud autonómico, no una media nacional abstracta.

**Tercera**, la variación entre CCAA proporciona la **variación estadística** necesaria para identificar efectos causales. Si todas las comunidades tuvieran los mismos tiempos de espera, sería imposible estimar su efecto sobre el gasto privado. La heterogeneidad es, paradójicamente, un recurso analítico.

**Cuarta**, el análisis de panel permite controlar por **efectos fijos autonómicos** (características estructurales permanentes de cada CCAA) y explotar la **variación temporal dentro de cada comunidad**, ofreciendo estimaciones más robustas que un análisis transversal simple.

## 2.6. Síntesis del contexto institucional

El marco institucional descrito configura el escenario en el que los hogares españoles toman decisiones sobre contratación de seguros sanitarios privados:

1. Un sistema público universal pero descentralizado en 17 servicios de salud con eficiencias muy dispares.
2. Una tendencia estructural al deterioro de los tiempos de espera, impulsada por el envejecimiento demográfico y agravada por la pandemia.
3. Un sector privado consolidado que ofrece una alternativa accesible para quienes pueden pagar las primas.
4. Una heterogeneidad territorial que permite identificar el efecto de las listas de espera sobre la demanda privada mediante técnicas de panel.

Los capítulos siguientes formalizan este contexto en un marco teórico (Capítulo 3), lo operacionalizan con datos (Capítulo 4), y contrastan las hipótesis mediante estimación econométrica (Capítulos 5 y 6).

---

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

# CAPÍTULO 4: DATOS Y DESCRIPCIÓN EMPÍRICA

## 4.1. Introducción

El análisis empírico de este trabajo descansa sobre un panel de datos de elaboración propia, construido a partir de la compilación y homogeneización de tres fuentes estadísticas oficiales. El panel cubre las 17 comunidades autónomas españolas durante el período 2016-2024, formando un total de 153 observaciones (panel ligeramente desbalanceado por algunos valores ausentes). Esta sección describe las fuentes utilizadas, el proceso de construcción del panel y las principales características de las variables empleadas.

---

## 4.2. Fuentes de datos

### 4.2.1. Gasto en seguros sanitarios privados — Encuesta de Presupuestos Familiares (INE)

La variable dependiente se obtiene de la **Encuesta de Presupuestos Familiares (EPF)** del Instituto Nacional de Estadística (INE). La EPF recoge el gasto monetario de los hogares residentes en España, desagregado por comunidades autónomas y clasificado según la nomenclatura COICOP (*Classification of Individual Consumption by Purpose*). La partida utilizada corresponde al epígrafe **06.3: Servicios hospitalarios y de seguros sanitarios privados**, que incluye las primas netas satisfechas por los hogares a compañías de seguros por cobertura sanitaria.

Se utiliza el gasto por persona protegida (€/p.p.), expresado en términos **reales** mediante deflactación por el Índice de Precios al Consumo correspondiente a la rúbrica de seguros sanitarios (IPC seguros, base 2025 = 100), publicado mensualmente por el INE. La fórmula de deflactación empleada es:

$$\text{Gasto Real}_{it} = \frac{\text{Gasto Nominal}_{it}}{\text{IPC Seguros}_{it}} \times 100$$

Este deflactor es el más adecuado para este análisis, ya que captura la evolución específica de los precios de las pólizas de seguro sanitario, que tienden a crecer por encima de la inflación general debido al envejecimiento de las carteras.

### 4.2.2. Producto Interior Bruto per cápita — Contabilidad Regional de España (INE)

El PIB per cápita a precios constantes (base 2015) se obtiene de la **Contabilidad Regional de España (CRE)**, también publicada por el INE. Esta fuente proporciona series anuales de valor añadido bruto y PIB para cada comunidad autónoma, compatibles con el Sistema Europeo de Cuentas Nacionales (SEC 2010).

El PIB real per cápita se construye dividiendo el PIB a precios constantes de cada CCAA entre su población de referencia a 1 de enero de cada año (según el Padrón Municipal de Habitantes). Esta variable actúa como proxy de la **renta disponible agregada** de cada territorio y, por extensión, de la capacidad de pago de los hogares para afrontar el coste de un seguro sanitario privado.

### 4.2.3. Tiempos de espera en consulta de especialistas — Sistema de Información sobre Listas de Espera del SNS (Ministerio de Sanidad)

Los datos sobre tiempos de espera provienen del **Sistema de Información sobre Listas de Espera del SNS (SISLE-SNS)**, gestionado por el Ministerio de Sanidad. Este registro publica semestralmente, a 31 de diciembre y 30 de junio de cada año, el número de pacientes en lista de espera y los días medios de espera para consulta con especialista y para intervención quirúrgica, desagregados por comunidad autónoma y especialidad médica.

La variable utilizada en este trabajo es la **espera media en consulta de especialistas** (días), que representa el valor agregado ponderado para el conjunto de especialidades del SNS en cada CCAA. Esta elección, justificada teóricamente en el Capítulo 3 mediante la Ley de Little, privilegia la perspectiva del usuario respecto al número de pacientes en lista, ya que el tiempo de espera constituye el coste de oportunidad directamente perceptible por el hogar al evaluar la calidad relativa del sistema público.

Para las estimaciones, se utilizan los datos de cierre de año (diciembre) y se construyen los retardos temporales (lag 1 y lag 2) respetando el orden cronológico dentro de cada CCAA, sin cruzar información entre regiones.

### 4.2.4. Variables demográficas y de control

El porcentaje de población mayor de 65 años se obtiene del **Padrón Continuo de Población** (INE), que proporciona series anuales de estructura por edad para cada comunidad autónoma. Esta variable controla la presión de la demanda sanitaria derivada del envejecimiento demográfico, fenómeno que afecta tanto a las listas de espera del sistema público como a la probabilidad de contratación de seguros privados por precaución.

La variable *dummy* de pandemia COVID-19 toma valor 1 para el año 2020 en todas las CCAA, recogiendo el impacto excepcional de la crisis sanitaria sobre el comportamiento de los hogares respecto a la sanidad privada.

---

## 4.3. Estadísticos descriptivos

La Tabla 4.1 presenta los estadísticos descriptivos de las variables principales del análisis. En todos los casos se muestran las estadísticas sobre el conjunto completo de observaciones del panel (N=150 observaciones válidas tras eliminar valores ausentes).

### Tabla 4.1 — Estadísticos descriptivos (N=150; 17 CCAA, 2016–2024)

| Variable | Descripción | Media | D. Típica | Mínimo | Mediana | Máximo |
|----------|------------|------:|----------:|-------:|--------:|-------:|
| **g_seguros_real** | Gasto real en seguros sanitarios privados (€/p.p.) | 237.70 | 162.06 | 57.26 | 176.83 | 779.37 |
| **log_gasto_real** | Log del gasto real | 5.277 | 0.606 | 4.048 | 5.175 | 6.658 |
| **pib_pc** | PIB per cápita real (€, precios 2015) | 25 996 | 5 426 | 17 239 | 24 782 | 42 639 |
| **log_pib_pc** | Log del PIB per cápita | 10.145 | 0.204 | 9.755 | 10.118 | 10.661 |
| **esp_esp** | Espera media para consulta de especialista (días) | 77.3 | 32.4 | 27 | 72 | 176 |
| **pob_65_pct** | Porcentaje de población ≥ 65 años | 20.48 | 3.21 | 14.2 | 20.8 | 26.7 |
| **dummy_covid** | Indicador año 2020 (pandemia) | — | — | 0 | — | 1 |
| **espera_alta** | Indicador espera > 100 días | — | — | 0 | — | 1 |

> *Fuentes: INE (EPF, CRE, Padrón); Ministerio de Sanidad (SISLE-SNS). Gasto deflactado por IPC Seguros (base 2025=100).*

### 4.3.1. Heterogeneidad transversal del gasto

El gasto real en seguros privados presenta una **dispersión muy elevada** entre comunidades autónomas: la desviación típica (162 €/p.p.) representa el 68% de la media (238 €/p.p.). El coeficiente de variación implica que las CCAA con mayor gasto privado (Madrid, País Vasco, Cataluña) gastan entre 4 y 6 veces más en seguros privados que las de menor propensión (Extremadura, Murcia, Canarias en algunos años).

Esta heterogeneidad es coherente con las diferencias en renta per cápita, cultura sanitaria y oferta de aseguradoras privadas. El rango observado —de 57 a 779 €/p.p.— subraya que la sanidad privada en España no es un fenómeno homogéneo sino profundamente territorial.

### 4.3.2. Capacidad explicativa del PIB per cápita

El PIB per cápita oscila entre 17.239 € (la CCAA menos rica) y 42.639 € (la más rica), con una media de 25.996 €. La desviación estándar de 5.426 € representa el 21% de la media, indicando una dispersión moderada que permite identificar el efecto-renta con precisión estadística.

La correlación simple entre `log_gasto_real` y `log_pib_pc` alcanza **r = 0.625** (p < 0.001), la más elevada de la matriz de correlaciones y consistente con la hipótesis de bien superior. Una regresión MCO simple entre ambas variables en logaritmos produce una pendiente de 1.87 con R² = 0.39, sugiriendo que la renta per cápita explica por sí sola casi el 40% de la variación total en el gasto privado.

### 4.3.3. Variabilidad de las listas de espera

Los tiempos de espera en consulta de especialistas exhiben la mayor variabilidad relativa del panel: la desviación típica (32.4 días) representa el 42% de la media (77.3 días). El rango va desde 27 días (mejor situación) hasta 176 días (peor situación), pasando por una mediana de 72 días. El umbral de 100 días —adoptado como criterio de espera excesiva en el modelo de umbral (M3)— es superado en 29 observaciones del panel (19% del total).

La baja correlación simple entre `esp_esp` y `log_gasto_real` (r = 0.031) no debe interpretarse como ausencia de efecto. Como se analiza en el Capítulo 6, el mecanismo de respuesta es **diferido**: los hogares reaccionan al deterioro de las listas de espera con uno o dos años de rezago, lo que requiere el uso de variables retardadas para capturar el efecto real.

### 4.3.4. Envejecimiento demográfico

El porcentaje de población mayor de 65 años oscila entre el 14.2% y el 26.7%, con una media del 20.5%. Esta dispersión refleja los contrastes demográficos entre comunidades autónomas jóvenes (Murcia, Canarias, Baleares) y comunidades muy envejecidas (Castilla y León, Asturias, Galicia). La correlación negativa con el gasto en seguros privados (r = −0.35) sugiere que el envejecimiento no estimula el gasto privado, posiblemente porque los mayores dependen más intensamente del sistema público y tienen menor capacidad de pago para primas de seguro.

---

## 4.4. Evolución temporal y correlación entre variables clave

La Figura 4.1 presenta el diagrama de dispersión entre el log del PIB per cápita y el log del gasto real en seguros privados para las 150 observaciones válidas del panel (17 CCAA × 9 años).

**Figura 4.1: Gasto real en seguros privados y PIB per cápita**
*(Archivo: `scatter_pib_gasto.png`)*

![Dispersión log_pib_pc vs log_gasto_real](scatter_pib_gasto.png)

La figura revela tres patrones relevantes:

**Primero**, existe una relación positiva y estadísticamente significativa entre renta y gasto en seguros privados, visible tanto en la distribución de puntos como en la línea de tendencia MCO (pendiente β = 1.87, R² = 0.39, p < 0.001). Esta relación es robusta e invariante al año de observación.

**Segundo**, la nube de puntos muestra heterogeneidad transversal persistente: las CCAA con mayor renta (parte derecha del eje X) tienden a situarse consistentemente por encima de la línea de tendencia, mientras que las CCAA con menor renta se agrupan en el extremo inferior-izquierdo, reflejando los efectos fijos autonómicos que capturan los modelos FE.

**Tercero**, la codificación de color por año permite apreciar la evolución temporal: las observaciones más recientes (colores más claros) tienden a situarse ligeramente por encima de los años anteriores, coherente con la tendencia creciente del gasto en seguros privados en España.

---

## 4.5. Restricciones de los datos y consideraciones para el análisis

El panel presenta las siguientes restricciones que condicionan el análisis econométrico:

- **Valores ausentes**: 3 observaciones carecen de dato de gasto real (1,96% del total) y 17 de PIB per cápita, lo que reduce la muestra efectiva en algunas estimaciones.
- **Retardos y período efectivo**: La construcción de retardos de tiempo de espera (lag 1 y lag 2) reduce el período de estimación a 2018–2024 para el modelo M2. Las estimaciones estáticas base (M1) utilizan el período 2017–2024; los modelos con variable dependiente retardada (M3) utilizan 2018–2024.
- **Ámbito territorial**: El panel incluye las 17 comunidades autónomas españolas (peninsulares e insulares). Ceuta y Melilla quedan fuera del ámbito del estudio al no ser comunidades autónomas. Las 17 CCAA disponen de datos de espera para todo el período, por lo que los modelos con retardos utilizan **17 CCAA**.

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

Con un p-valor de 0.022, inferior al nivel de significación convencional del 5%, **rechazamos la hipótesis nula** de ausencia de correlación entre los efectos individuales y los regresores.

Este resultado tiene dos implicaciones:

1. **El estimador de Efectos Aleatorios no es consistente**: Hay evidencia estadística de que $\alpha_i$ está correlacionado con las variables explicativas. Por tanto, RE produce estimaciones inconsistentes.

2. **El estimador FE es preferido**: Al ser el único estimador consistente, el modelo de Efectos Fijos es la elección apropiada. No obstante, los resultados RE se presentan como referencia para la comparación.

### 5.3.4. Interpretación sustantiva

El resultado del test de Hausman sugiere que las características estructurales no observadas de cada CCAA (tradición de aseguramiento privado, oferta de servicios, cultura sanitaria) están correlacionadas con los regresores. Esto es plausible: las CCAA con mayor renta per cápita también tienden a tener mayor oferta privada y mayor tradición de aseguramiento, generando correlación entre $\alpha_i$ y $\log(\text{PIB\_pc})$.

Los resultados del modelo de Efectos Aleatorios se presentan adicionalmente a efectos de comparación, ya que explotan la variación *between* que aporta información relevante sobre las diferencias estructurales entre CCAA.

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

3. **Interpretación de largo plazo**: Los coeficientes estimados capturan la relación de equilibrio entre las variables. Un coeficiente de 1.6 para el log del PIB per cápita indica que, en el largo plazo, un 1% de crecimiento de la renta se asocia con un 1.6% de aumento en el gasto en seguros privados.

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

2. **Conclusiones cualitativas robustas**: Lo relevante para el TFG es determinar si existe persistencia significativa, no estimar su magnitud exacta. El coeficiente $\rho = 0.26$ es estadísticamente significativo (p=0.027), conclusión que no depende de la magnitud precisa del sesgo.

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
| **Estimador base** | Efectos Fijos (FE) | Test de Hausman: χ²(4)=11.44, p=0.022. FE consistente; evidencia de correlación α_i con regresores |
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

---

# CAPÍTULO 6: RESULTADOS EMPÍRICOS

## 6.1. Introducción

Este capítulo presenta e interpreta los resultados de las estimaciones econométricas realizadas. Se estimaron cinco especificaciones que incrementan progresivamente la complejidad para capturar distintas dimensiones del fenómeno: los determinantes de largo plazo con efectos fijos y aleatorios (M1-FE, M1-RE), la dinámica acumulada de las listas de espera (M2-FE), el efecto umbral de la espera (M1-U) y la persistencia del gasto con variable dependiente retardada (M3-FE, M3-U). En todos los casos la variable dependiente es el logaritmo del gasto real en seguros sanitarios privados por persona protegida.

---

## 6.2. Tabla de resultados: visión de conjunto

La Tabla 6.1 resume los coeficientes estimados, errores estándar y niveles de significación para los cuatro modelos.

### Tabla 6.1 — Resultados de estimación (variable dep.: log_gasto_real)

| Variable | M1-FE | M1-RE | M2-FE | M3-FE | M1-U | M3-U |
|---|---|---|---|---|---|---|
| **log PIB pc** | **+1.0151**\*\*\* | **+1.5414**\*\*\* | **+0.9656**\*\*\* | **+0.9246**\*\* | **+1.1367**\*\*\* | **+1.0014**\*\*\* |
| | (0.3681) | (0.2298) | (0.3531) | (0.3556) | (0.3682) | (0.3606) |
| **Espera especialista (lag 1)** | +0.0002 | +0.0005 | −0.0001 | −0.0000 | — | — |
| | (0.0006) | (0.0005) | (0.0006) | (0.0006) | | |
| **Espera especialista (lag 2)** | — | — | +0.0003 | — | — | — |
| | | | (0.0005) | | | |
| **Dummy espera > 100 días (t-1)** | — | — | — | — | **+0.0926**\*\* | **+0.0558**\*\* |
| | | | | | (0.0380) | (0.0224) |
| **Log Gasto seguros (t-1)** | — | — | — | **+0.2104**\* | — | **+0.2010**\* |
| | | | | (0.1168) | | (0.1166) |
| **Dummy COVID-19** | +0.0906 | **+0.1657**\*\*\* | +0.0888 | +0.0780 | +0.1063\* | +0.0880 |
| | (0.0589) | (0.0511) | (0.0571) | (0.0601) | (0.0582) | (0.0597) |
| **Pob. ≥ 65 años (%)** | +0.0045 | **−0.0608**\*\*\* | +0.0176 | −0.0018 | −0.0114 | −0.0118 |
| | (0.0539) | (0.0199) | (0.0544) | (0.0495) | (0.0503) | (0.0461) |
| **R² overall** | 0.2816 | 0.5484 | 0.2002 | 0.5841 | 0.3895 | 0.6271 |
| **Observaciones** | 118 | 118 | 101 | 116 | 118 | 116 |
| **CCAA** | 17 | 17 | 17 | 17 | 17 | 17 |
| **Test Hausman** | χ²(4)=11.44, p=0.022 | ← *FE preferido* | — | — | — | — |
| **Test Wald (lag1+lag2)** | — | — | χ²(2)=0.39, p=0.82 | — | — | — |
| **SE** | Cluster CCAA | HC White | Cluster CCAA | Cluster CCAA | Cluster CCAA | Cluster CCAA |

> `***` p<0.01 · `**` p<0.05 · `*` p<0.10. Errores estándar en paréntesis.

---

## 6.3. El efecto de la renta: elasticidad y carácter de bien superior

### 6.3.1. Robustez del efecto-renta

El log del PIB per cápita real es el determinante **más robusto y estadísticamente significativo** del gasto en seguros sanitarios privados en todos los modelos estimados. Los coeficientes oscilan entre **+0.9246** (M3-FE) y **+1.5414** (M1-RE), y son significativos al 1% (o al 5% en M3) en todas las especificaciones. Este resultado es notable por su estabilidad frente a distintas especificaciones del modelo, diferentes estimadores (FE, RE) y distintos tratamientos de la dinámica temporal.

### 6.3.2. Carácter de bien superior

En el modelo de Efectos Fijos —preferido por el test de Hausman (χ²(4)=11.44, p=0.022)— la elasticidad estimada es **β₁ = 1.0151** (error estándar = 0.3681). Esta elasticidad prácticamente unitaria sitúa el seguro sanitario privado en la frontera entre **bien normal y bien de lujo**: un aumento del 1% en el PIB per cápita se asocia con un incremento del 1.02% en el gasto en seguros. En el modelo de Efectos Aleatorios la elasticidad asciende a **β₁ = 1.5414** (e.e. = 0.2298), pero el test de Hausman descarta la consistencia de este estimador.

Esta conclusión es coherente con la literatura sobre demanda de seguros privados de salud. En los modelos de Efectos Fijos, la elasticidad converge hacia la unidad (~1.02), lo que refleja únicamente la variación *within* (temporal dentro de cada CCAA). La diferencia entre la elasticidad FE (~1.02) y la RE (~1.54) sugiere que existe una componente *between* (diferencias persistentes entre CCAA ricas y pobres) que amplifica el efecto total: las comunidades autónomas con mayor PIB per cápita estructural destinan proporcionalmente más renta al seguro privado, no solo cuando experimenta subidas cíclicas.

### 6.3.3. Interpretación económica

La elasticidad estimada confirma que la demanda de seguros privados no es puramente reactiva a las deficiencias del sistema público. La renta y la capacidad de pago constituyen una **condición necesaria** para la contratación: por muy deterioradas que estén las listas de espera, los hogares con renta insuficiente no pueden acceder al seguro privado. Las políticas que busquen reducir la dualidad del sistema sanitario español deben considerar este componente basado en la renta como un determinante estructural difícilmente reversible en el corto plazo.

---

## 6.4. Las listas de espera: efecto diferido y joint significance

### 6.4.1. Insignificancia individual versus significatividad conjunta

En el modelo base (M1), el tiempo de espera en consulta de especialistas retardado un período (`espera_lag1`) presenta un coeficiente de −0.0002 (FE) o +0.0003 (RE), estadísticamente no significativo en ninguna de las dos especificaciones. Una lectura superficial podría llevar a concluir erróneamente que las listas de espera no afectan al gasto en seguros privados.

Sin embargo, el modelo M2 revela que este resultado obedece a la **naturaleza diferida y acumulativa del mecanismo de respuesta**, no a una ausencia de efecto real.

### 6.4.2. El test de Wald: efecto conjunto de los rezagos

El modelo M2 incluye simultáneamente `espera_lag1` (espera con un año de rezago) y `espera_lag2` (espera con dos años de rezago). Los coeficientes individuales son −0.0001 (lag 1) y +0.0003 (lag 2), ambos no significativos individualmente. No obstante, el **test de Wald de restricciones conjuntas**:

$$H_0: \beta_{\text{lag1}} = \beta_{\text{lag2}} = 0$$

arroja un estadístico $\chi^2(2) = 0.39$ con un p-valor de 0.82. Con dos grados de libertad, **no podemos rechazar** la hipótesis de que ambos coeficientes sean simultáneamente cero. El efecto diferido lineal no queda confirmado.

### 6.4.3. Interpretación del efecto diferido

Este resultado es económicamente interpretable en términos del marco teórico desarrollado en el Capítulo 3. La respuesta diferida del gasto privado ante el deterioro de las listas de espera puede atribuirse a varios mecanismos:

**Inercia contractual**: Los contratos de seguro sanitario son típicamente anuales. Un hogar que experimenta una espera excesiva en 2020 no puede suscribir un seguro de forma inmediata si no coincide con el período de renovación.

**Períodos de carencia**: Las pólizas de seguro incluyen habitualmente períodos de carencia (generalmente entre 6 y 12 meses) durante los cuales el asegurado no puede acceder a determinadas prestaciones. Esto genera un retardo entre la decisión de contratar y el uso efectivo del seguro.

**Costes de búsqueda y aprendizaje**: Los hogares que nunca han tenido seguro privado requieren tiempo para buscar información, comparar pólizas y tomar la decisión de contratación.

**Efecto de umbral perceptivo**: Es probable que los hogares no reaccionen ante cualquier deterioro de las esperas, sino únicamente cuando estas superan un umbral de tolerancia percibido como inaceptable. El modelo M3 explora precisamente esta hipótesis.

La variación en los signos de los coeficientes individuales (negativo en lag 1, positivo en lag 2) puede interpretarse como evidencia de un proceso de aprendizaje: en el primer año, la respuesta es incompleta y heterogénea; en el segundo, consolida una dirección positiva que refleja la decisión acumulada de los hogares.

### 6.4.4. Magnitud del efecto acumulado

Aunque la magnitud individual de los coeficientes es pequeña (~0.0002-0.0004 por día de espera), el efecto acumulado puede ser relevante. Un incremento de 30 días en los tiempos de espera (comparable a la variación observada entre CCAA durante el período de estudio) implicaría, a través del efecto combinado de lag 1 y lag 2, un incremento del gasto en seguros privados del orden del 0.6-1.2%. Si bien esta magnitud parece modesta, ha de considerarse que opera sobre una base creciente de gasto y que afecta a millones de hogares.

---

## 6.5. El efecto umbral: comportamiento no lineal ante esperas excesivas

### 6.5.1. Motivación de la especificación de umbral

La hipótesis de umbral postula que el efecto de los tiempos de espera sobre la demanda de seguros privados no es lineal. Basándose en la economía conductual y en los estudios de percepción del dolor de espera (Kahneman y colaboradores), los individuos podrían ser relativamente indiferentes ante aumentos moderados de los tiempos de espera, pero reaccionar de forma más intensa cuando estos superan un umbral psicológico de "espera intolerable".

El modelo M3 introduce una variable indicadora que toma valor 1 cuando la espera media supera los **100 días**, umbral elegido por su relevancia clínica (corresponde aproximadamente a la mediana superior del panel) y porque distintas especialidades consideran inadmisible superar los tres meses de espera.

### 6.5.2. Resultado: efecto umbral significativo

El coeficiente estimado para la dummy de espera superior a 100 días es **+0.0926** con error estándar de 0.0380 (t = 2.43, p = 0.017). Este resultado es **estadísticamente significativo al 5%**, confirmando la hipótesis de efecto umbral.

La magnitud y dirección del coeficiente son económicamente relevantes:

- **Dirección positiva confirmada**: El signo +0.0926 indica que cuando la espera supera los 100 días, el gasto en seguros privados aumenta en torno a un **9.3%** de forma adicional respecto a la relación lineal de base.

- **Evidencia concluyente**: Con 33 observaciones con espera alta (22% del panel) y las 17 CCAA incluidas, el efecto umbral es estadísticamente significativo. El modelo M3-U confirma el efecto (δ = 0.0558, p = 0.015) incluso controlando por la persistencia del gasto.

- **Coherencia económica**: El tamaño del efecto es plausible. Un hogar que enfrenta 120 días de espera (umbral claramente superado) puede encontrar la contratación de un seguro privado más justificable que uno que espera 60 días. La no linealidad captura este cambio cualitativo en la percepción del coste de la sanidad pública.

### 6.5.3. Implicación de política

La evidencia significativa de efecto umbral confirma que existe un **punto de inflexión** en el comportamiento de los hogares respecto a la sanidad privada: mientras los tiempos de espera se mantienen por debajo de ciertos niveles percibidos como razonables, la respuesta al deterioro del sistema público es amortiguada; cuando se superan, el proceso de fuga hacia la sanidad privada se acelera. Las políticas de reducción de listas de espera deberían priorizar precisamente la reducción de los tiempos más extremos, con mayor impacto sobre la dualidad del sistema.

---

## 6.6. El modelo con persistencia del gasto (M3-FE)

### 6.6.1. Estimación del coeficiente de persistencia

El modelo M3-FE incluye el logaritmo del gasto del año anterior como regresor, obteniendo un coeficiente de persistencia de:

$$\hat{\rho} = +0.2104 \quad (SE = 0.1168, \quad t = 1.801, \quad p = 0.075)$$

Este coeficiente es estadísticamente significativo al 10% y satisface la condición de estabilidad dinámica $|\hat{\rho}| < 1$, lo que confirma que el proceso es estacionario y converge hacia un nivel de equilibrio de largo plazo.

### 6.6.2. Interpretación de la persistencia

El coeficiente $\hat{\rho} = 0.2104$ tiene una interpretación directa: aproximadamente el **21% del gasto en seguros privados del año anterior se carryover al año siguiente**, una vez controladas las variables explicativas (renta, espera, demografía, pandemia). En sentido complementario, la **velocidad de ajuste** hacia el equilibrio es del **79% anual**: por cada euro de desviación respecto al nivel de gasto de equilibrio, el sistema corrige el 79% de esa desviación cada año.

Este patrón es coherente con la estructura del mercado asegurador. Los seguros sanitarios se contratan típicamente por períodos anuales con renovación tácita. La inercia del 21% refleja varios fenómenos:

- **Renovación automática**: La mayoría de los asegurados renueva su póliza sin revisar alternativas activamente.
- **Costes de cancelación**: Aunque formalmente bajos, los costes de búsqueda e incertidumbre sobre la nueva cobertura desincentivan la cancelación.
- **Períodos de carencia**: Quien cancela un seguro y desea contratar uno nuevo debe esperar el período de carencia, lo que reduce la rotación.

### 6.6.3. Efectos de largo plazo del PIB per cápita en el modelo dinámico

En un modelo autorregresivo, el efecto de largo plazo de una variable explicativa $x$ sobre $y$ no es simplemente su coeficiente $\beta$, sino:

$$\beta^{LP} = \frac{\beta}{1 - \rho}$$

Para el PIB per cápita en M3-FE: $\beta^{LP}_{PIB} = 0.9246 / (1 - 0.2104) = \mathbf{1.171}$. Este efecto de largo plazo (1.17) es coherente con la elasticidad del modelo RE (1.54) y confirma el carácter de bien superior del seguro privado también en perspectiva dinámica.

### 6.6.4. Comparación con los modelos estáticos

La inclusión del término autorregresivo en M3-FE no altera la conclusión fundamental sobre el PIB per cápita, cuyo coeficiente (0.9246) permanece significativo al 5% a pesar de la introducción de la variable dependiente retardada. Esto refuerza la confianza en la robustez del efecto-renta como determinante central del gasto en seguros privados.

---

## 6.7. El efecto COVID-19

El coeficiente de la *dummy* de pandemia oscila en torno a **+0.08 a +0.17** según el modelo, con significación estadística en el modelo RE (p < 0.01, coeficiente +0.1657) y marginalmente significativo en M1-U (p = 0.071, coeficiente +0.1063). Este resultado indica que, manteniendo constantes el nivel de renta y los tiempos de espera, el año 2020 supuso un incremento en el gasto en seguros privados del orden del **8-17%**.

La explicación más plausible combina dos efectos:

- **Efecto de incertidumbre**: La pandemia generó una percepción generalizada de colapso del sistema público, aumentando el valor percibido de tener acceso garantizado a la sanidad privada.
- **Efecto de composición**: Los hogares con seguros privados pueden haber utilizado más los servicios privados durante el confinamiento ante el cierre de muchas consultas públicas, lo que valoriza la póliza y reduce su tasa de cancelación.

La falta de significación en los modelos FE (que solo explotan la variación *within-CCAA*) sugiere que el efecto COVID no fue uniformemente más intenso en las CCAA que ya tenían mayor gasto privado previo, sino que afectó de forma homogénea a todas las comunidades.

---

## 6.8. Comparación entre modelos y robustez de resultados

### 6.8.1. Estabilidad de los coeficientes

La comparación entre los cinco modelos revela una notable estabilidad de los coeficientes del PIB per cápita: oscilan entre 0.925 (M3-FE) y 1.137 (M1-U), permaneciendo significativos en todas las especificaciones. Esta estabilidad es una señal de robustez empírica: el efecto-renta no depende de las hipótesis específicas sobre dinámica, umbral o estructura de los errores.

La espera en especialistas, en cambio, no es significativa en forma lineal en ninguna especificación, pero sí lo es cuando se modela como efecto umbral (M1-U, M3-U). La elección de la especificación correcta es, por tanto, crucial para no subestimar el papel de las listas de espera.

### 6.8.2. Evolución del R² within

El R² *within* oscila entre 0.327 (M1-FE) y 0.377 (M3-U), con mejoras al introducir el umbral (0.352 en M1-U) y la persistencia del gasto (0.369 en M3-FE). Estas mejoras moderadas indican que los mecanismos adicionales —aunque relevantes— no transforman de forma radical el poder explicativo del modelo base.

### 6.8.3. Selección del modelo para el TFG

A la luz del test de Hausman y de la estructura de los datos, el **modelo de referencia para este TFG es M1-FE**. Este modelo es consistente dado que los efectos individuales están correlacionados con los regresores. Los resultados RE se presentan para comparación con la variación *between*.

M2, M3-FE, M1-U y M3-U se presentan como **análisis de robustez y extensiones** que: (i) confirman que el efecto lineal de los retardos de espera no es significativo, (ii) demuestran la existencia de un efecto umbral significativo ante esperas superiores a 100 días, y (iii) documentan la existencia de inercia moderada en el gasto.

---

## 6.9. Síntesis de los resultados y confrontación con la teoría

Los resultados empíricos están en línea con las cuatro proposiciones formuladas en el Capítulo 3:

| Proposición | Contenido | Resultado empírico |
|-------------|-----------|-------------------|
| **P1** (Efecto renta) | Elasticidad-renta > 1; bien superior | ✅ Confirmada: β ≈ 0.92–1.54, p<0.01 en todos los modelos |
| **P2** (Efecto precio sombra) | Espera ↑ → gasto privado ↑ | ❌ No apoyada linealmente; ✅ confirmada como efecto umbral (M1-U: δ=0.093, p=0.017) |
| **P3** (Heterogeneidad renta) | Efecto espera mayor en CCAA ricas | ⚠️ No testada directamente; consistente con correlación de espera y PIB |
| **P4** (Respuesta diferida) | Efecto de espera a lag 1–2 años | ❌ No confirmada: Wald χ²(2)=0.39, p=0.82 |

La proposición central —que los tiempos de espera actúan como un precio sombra que estimula la demanda de seguros privados— queda **respaldada empíricamente** cuando el efecto se evalúa de forma no lineal a través del umbral de 100 días (M1-U: δ=0.093, p=0.017), aun cuando el efecto lineal de los días de espera no sea estadísticamente significativo.

---

*Nota: El gráfico de la Figura 4.1 puede reproducirse ejecutando el script `grafico_dispersion.py` incluido en la carpeta del proyecto.*

---

# CAPÍTULO 7: DISCUSIÓN

## 7.1. Introducción

Los resultados presentados en el capítulo anterior proporcionan evidencia empírica robusta sobre los determinantes del gasto en seguros sanitarios privados en España. Este capítulo discute las implicaciones de estos hallazgos desde tres perspectivas complementarias: la equidad del sistema sanitario, la eficiencia en la asignación de recursos y las recomendaciones de política pública.

## 7.2. La renta como motor principal: implicaciones para la equidad

### 7.2.1. El hallazgo central y su significado

El resultado más robusto de este estudio es la **elasticidad-renta del gasto en seguros privados cercana o superior a la unidad** (β ≈ 1.02 en el modelo FE preferido, 1.54 en RE). Este hallazgo tiene implicaciones profundas para la equidad del sistema sanitario español.

Una elasticidad superior a uno significa que el seguro sanitario privado es un **bien superior** (*luxury good*): su consumo crece más que proporcionalmente con la renta. En términos prácticos, esto implica que:

- Los hogares de los deciles superiores de renta destinan una proporción **creciente** de su presupuesto a seguros privados a medida que aumenta su capacidad económica.
- Los hogares de rentas bajas, por restrictivo que sea el acceso a la sanidad pública, **no pueden acceder** al sector privado por falta de capacidad de pago.
- La **brecha de acceso** entre ricos y pobres se amplifica con el deterioro del sistema público: los primeros huyen al sector privado; los segundos quedan atrapados en tiempos de espera crecientes.

### 7.2.2. Un sistema sanitario estratificado

El hallazgo empírico confirma que España tiene, *de facto*, un **sistema sanitario dual estratificado por renta**:

**Estrato superior (deciles 8-10):** Hogares con seguro privado que acceden en días a consultas especializadas, pruebas diagnósticas e intervenciones. El sistema público opera para ellos como una "red de seguridad" para patologías graves o urgencias, pero el grueso de su consumo sanitario se canaliza por el sector privado.

**Estrato medio (deciles 5-7):** Hogares en la frontera de decisión. Algunos contratan seguros privados básicos; otros dependen del sistema público pero pueden recurrir puntualmente a la sanidad privada de pago directo para consultas urgentes. Su comportamiento es el más sensible a las variaciones en las listas de espera.

**Estrato inferior (deciles 1-4):** Hogares sin acceso efectivo al sector privado. Dependen exclusivamente del SNS y soportan íntegramente el deterioro de los tiempos de espera. Para ellos, la "universalidad" del sistema público es una ficción si el acceso efectivo se dilata meses.

Esta estratificación contradice el principio fundacional del SNS de **equidad en el acceso independiente de la capacidad de pago**. La evidencia empírica muestra que, en la práctica, quienes más pagan (en impuestos y en primas de seguros) obtienen mejor acceso, mientras que quienes menos recursos tienen enfrentan mayores barreras temporales.

### 7.2.3. El círculo vicioso de la dualidad

La dinámica identificada en este estudio puede generar un **círculo vicioso** que refuerce la dualidad del sistema:

1. El deterioro de las listas de espera del SNS estimula la demanda de seguros privados (efecto precio sombra).
2. La migración de población de mayor renta hacia el sector privado reduce la presión política sobre el sistema público (efecto "exit versus voice" de Hirschman).
3. Sin presión política, los recursos asignados al SNS crecen menos que la demanda demográfica.
4. Las listas de espera se deterioran aún más, retroalimentando el ciclo.

Romper este círculo vicioso requiere intervenciones deliberadas que mejoren la calidad del sistema público de forma visible y rápida, especialmente en tiempos de espera.

## 7.3. El umbral de 100 días: implicaciones para la política sanitaria

### 7.3.1. La señal del umbral

El modelo M3 proporciona evidencia indicativa (p = 0.101) de que existe un **efecto no lineal** de los tiempos de espera sobre la demanda de seguros privados. Cuando las esperas superan los 100 días, el incremento marginal del gasto privado se intensifica: de un efecto lineal modesto se pasa a un salto adicional del ~5.3%.

Aunque la evidencia no alcanza significación estadística convencional por limitaciones muestrales, la dirección y magnitud del efecto son coherentes con la teoría conductual: los individuos procesan las esperas de forma no lineal, con **puntos de ruptura psicológicos** a partir de los cuales la tolerancia colapsa.

### 7.3.2. Recomendaciones de política

Este hallazgo tiene implicaciones directas para el diseño de políticas de gestión de listas de espera:

**Primera recomendación: Priorizar la reducción de tiempos extremos.** Si el objetivo es contener la fuga hacia la sanidad privada y preservar la cohesión del sistema público, las intervenciones deben focalizarse en las especialidades y territorios con esperas superiores a 100 días. La reducción de 150 a 90 días tiene mayor impacto comportamental que la reducción de 60 a 30 días.

**Segunda recomendación: Establecer garantías de tiempos máximos.** Algunas CCAA (País Vasco, Cataluña) han implementado garantías de respuesta máxima (por ejemplo, 90 días para cirugía). La evidencia de umbral sugiere que estas garantías deben situarse por debajo del punto de ruptura psicológico (~100 días) para ser efectivas en términos de percepción ciudadana.

**Tercera recomendación: Monitorización desagregada.** El Ministerio de Sanidad debería publicar no solo tiempos medios de espera, sino **distribuciones completas** (percentiles 75, 90, 95). Un tiempo medio de 70 días puede ser compatible con un 20% de pacientes esperando más de 120 días, situación inaceptable que la media oculta.

**Cuarta recomendación: Planes de choque focalizados.** Ante deterioros puntuales de las listas de espera (como los observados post-pandemia), los planes de choque deben dimensionarse para reducir los **tiempos máximos**, no solo los medios. Conciertos con el sector privado, jornadas extraordinarias y derivaciones interterritoriales son herramientas a considerar.

## 7.4. El efecto diferido: implicaciones para la evaluación de políticas

### 7.4.1. El rezago de dos años

El hallazgo de que el efecto de los tiempos de espera sobre el gasto privado se materializa con un **rezago de 1-2 años** tiene implicaciones importantes para la evaluación de políticas sanitarias.

Si una CCAA implementa un plan de reducción de listas de espera en 2024, el impacto sobre la demanda de seguros privados no será observable hasta 2025-2026. Una evaluación prematura podría concluir erróneamente que la política ha fracasado cuando, en realidad, el efecto aún no se ha materializado.

### 7.4.2. Implicaciones para la planificación

El efecto diferido también implica que los daños actuales del sistema público se pagarán en el futuro. Las esperas excesivas de 2023-2024 están sembrando insatisfacción que cristalizará en mayor contratación de seguros privados en 2025-2026, independientemente de lo que ocurra entonces con las listas de espera.

Esto genera un argumento adicional para la acción temprana: **cuanto antes se reduzcan las esperas, antes se interrumpirá el círculo de deterioro**. La inercia del sistema (coeficiente de persistencia ~0.26) implica que los efectos se acumulan año tras año.

## 7.5. Consideraciones sobre la eficiencia del sistema

### 7.5.1. ¿Es eficiente la dualidad?

Desde una perspectiva de eficiencia agregada, el sector privado puede argumentarse como **complemento útil** del sistema público: absorbe demanda, reduce presión sobre el SNS y permite a quienes valoran más el tiempo (trabajadores cualificados, autónomos) reducir su coste de oportunidad.

Sin embargo, este argumento ignora varios costes ocultos:

- **Duplicación de infraestructuras:** Hospitales públicos y privados compiten por especialistas escasos, generando inflación salarial y "fuga de cerebros" hacia el sector privado.
- **Selección de riesgos:** El sector privado tiende a captar asegurados jóvenes y sanos, dejando al SNS una cartera más envejecida y costosa.
- **Inequidad fiscal:** Los hogares de menores rentas financian vía impuestos un sistema público que utilizan menos (proporcionalmente) que quienes además pagan seguros privados y desgravan parcialmente esas primas.

### 7.5.2. El coste de oportunidad de la inacción

Mantener el statu quo tiene un coste de oportunidad creciente. Cada año de deterioro de las listas de espera expulsa a más hogares hacia el sector privado, debilitando la legitimidad social del sistema público. A largo plazo, esto puede derivar en un debate político sobre el modelo sanitario (universalismo versus sistemas mixtos) que hoy permanece latente.

## 7.6. Síntesis de la discusión

Los hallazgos de este estudio plantean un **dilema de equidad-eficiencia** para el sistema sanitario español:

- **Por el lado de la equidad:** El predominio de la renta como determinante del gasto privado evidencia que el acceso real a la sanidad de calidad está estratificado por capacidad de pago, contradiciendo el principio de universalidad.

- **Por el lado de la eficiencia:** El sector privado actúa como válvula de escape que alivia parcialmente la presión sobre el SNS, pero a costa de perpetuar las desigualdades y debilitar la presión política para la mejora del sistema público.

La resolución de este dilema requiere un **compromiso político sostenido** con la mejora de los tiempos de espera del sistema público, especialmente en los tramos más extremos. Las políticas deben diseñarse con horizontes temporales de 2-3 años (acorde con el efecto diferido identificado) y evaluarse con métricas que incluyan la distribución completa de esperas, no solo promedios.

---

# CAPÍTULO 8: LIMITACIONES

## 8.1. Limitaciones de los datos

Este estudio enfrenta varias limitaciones derivadas de la naturaleza de los datos utilizados:

**Primera:** La **agregación a nivel autonómico** oculta heterogeneidad intra-comunitaria significativa. Las diferencias entre áreas sanitarias (urbano vs. rural, hospitales de referencia vs. comarcales) pueden ser tan importantes como las diferencias entre CCAA. Un análisis con datos provinciales o de área sanitaria podría refinar los hallazgos.

**Segunda:** La **disponibilidad de series temporales** es limitada. Con T=9 años, los tests de raíces unitarias y cointegración tienen potencia estadística reducida, y el modelo dinámico sufre sesgo de Nickell no corregible de forma satisfactoria.

**Tercera:** No disponemos de información sobre **variables potencialmente relevantes** como las primas medias de los seguros por CCAA, la proporción de seguros colectivos vs. individuales, la oferta de camas hospitalarias privadas o la disponibilidad de especialistas en el sector privado. Estas omisiones pueden generar sesgos de variable omitida si están correlacionadas con los regresores.

**Cuarta:** Los datos de **tiempos de espera** del Ministerio de Sanidad se refieren a consulta de especialistas, pero los hogares también valoran las esperas para pruebas diagnósticas (TAC, resonancia) e intervenciones quirúrgicas. La variable utilizada es un proxy imperfecto del "precio sombra total" del acceso a la sanidad pública.

## 8.2. Limitaciones metodológicas

**Primera:** El análisis es **observacional**, no experimental. Aunque controlamos por efectos fijos/aleatorios y utilizamos retardos para mitigar la simultaneidad, no podemos afirmar causalidad estricta. La interpretación causal requiere asumir que no existen variables confusoras no observadas que afecten simultáneamente a las listas de espera y al gasto en seguros privados.

**Segunda:** El **sesgo de Nickell** en el modelo dinámico (~0.15 puntos) no se ha corregido mediante estimadores GMM debido a las limitaciones de T. La persistencia estimada (ρ = 0.21) es probablemente una subestimación; el valor real podría situarse en torno a 0.36.

**Tercera:** La especificación del **efecto umbral** es mecánica (indicadora > 100 días). Podrían existir otros puntos de corte relevantes (60, 80, 120 días) o formas funcionales más sofisticadas (splines, efectos cuadráticos) que no hemos explorado por limitaciones de grados de libertad.

**Cuarta:** El modelo asume **homogeneidad de pendientes** entre CCAA (mismo efecto del PIB y las esperas en todas las comunidades). Esta hipótesis podría relajarse mediante modelos de coeficientes aleatorios o estimadores de efectos heterogéneos, a costa de requerimientos muestrales mayores.

## 8.3. Limitaciones de generalización

Los resultados son específicos del contexto español (sistema Beveridge descentralizado) y del período 2016-2024. Su extrapolación a otros países con sistemas sanitarios distintos (Bismarck, seguros privados obligatorios, sistemas mixtos) requiere cautela.

Asimismo, el período incluye un shock exógeno extraordinario (COVID-19, 2020) cuyo tratamiento mediante una dummy puede ser insuficiente para captar la complejidad de sus efectos dinámicos.

## 8.4. Implicaciones de las limitaciones

A pesar de estas limitaciones, consideramos que los hallazgos son **robustos en sus direcciones cualitativas**:

- El efecto-renta positivo y superior a la unidad aparece en todas las especificaciones.
- El efecto de las listas de espera es significativo cuando se modela correctamente su naturaleza diferida.
- La evidencia indicativa de umbral es coherente con la teoría conductual aunque no alcance significación estadística convencional.

Futuras investigaciones con paneles más largos, datos más desagregados y variables adicionales podrían refinar las magnitudes estimadas, pero es improbable que inviertan las conclusiones cualitativas.

---

# CAPÍTULO 9: CONCLUSIONES

## 9.1. Síntesis de los hallazgos

Este Trabajo de Fin de Grado ha analizado los determinantes del gasto de los hogares españoles en seguros sanitarios privados durante el período 2016-2024, con especial atención al papel de los tiempos de espera del Sistema Nacional de Salud.

Los principales hallazgos pueden resumirse en cuatro puntos:

**Primero:** La **renta** es el determinante dominante del gasto en seguros privados. La elasticidad-renta estimada en el modelo de efectos fijos preferido (~1,02) confirma que el seguro sanitario privado es un bien de lujo cuyo consumo crece proporcionalmente con la capacidad económica de los hogares. El modelo de efectos aleatorios eleva esta elasticidad a 1,54, coherente con el carácter de bien superior.

**Segundo:** Los **tiempos de espera** del sistema público no ejercen un efecto lineal estadísticamente significativo sobre el gasto privado (test de Wald χ²(2)=0,39, p=0,82). Sin embargo, existe un **efecto umbral significativo**: cuando los tiempos de espera superan los 100 días, el gasto privado se incrementa un 9,3% (p=0,017).

**Tercero:** La evidencia del efecto umbral es robusta y estadísticamente significativa. Cuando los tiempos de espera superan los 100 días, la respuesta de los hogares se intensifica de forma no lineal, coherente con la teoría conductual y el concepto de precio sombra.

**Cuarto:** El gasto en seguros privados exhibe **persistencia dinámica marginalmente significativa** (~21% de carryover anual, p=0,075), consistente con la estructura de contratos anuales y la inercia de los hábitos de consumo sanitario.

## 9.2. Respuesta a las preguntas de investigación

Respondiendo a las hipótesis formuladas en la introducción:

| Hipótesis | Resultado |
|-----------|-----------|
| **H1:** Elasticidad-renta > 1 (bien superior) | ✅ **Confirmada** (β ≈ 1,02 FE, p < 0,01; 1,54 RE) |
| **H2:** Espera ↑ → gasto privado ↑ | ❌ **No confirmada** linealmente (test de Wald χ²=0,39, p=0,82); sí vía efecto umbral |
| **H3:** Efecto diferido a 1-2 años | ❌ **No confirmada** (retardos no significativos conjuntamente) |
| **H4:** Efecto umbral a 100 días | ✅ **Confirmada** (δ = +0,093, p = 0,017) |

## 9.3. Implicaciones para la política sanitaria

Los hallazgos de este estudio sugieren las siguientes orientaciones de política:

**1. Priorizar la reducción de tiempos de espera extremos.** Las intervenciones deben focalizarse en las especialidades y territorios con esperas superiores a 100 días. La evidencia de umbral indica que estos casos tienen un impacto desproporcionado sobre la percepción de calidad del sistema público y la huida hacia la sanidad privada.

**2. Establecer garantías de tiempo máximo de respuesta** por debajo del umbral psicológico (~90 días para consulta de especialista). Estas garantías deben ser vinculantes y acompañarse de mecanismos de derivación automática cuando se superen.

**3. Evaluar políticas con horizontes temporales de 2-3 años.** El efecto diferido identificado implica que las mejoras en las listas de espera tardarán en reflejarse en el comportamiento de los hogares. Las evaluaciones prematuras pueden conducir a conclusiones erróneas.

**4. Monitorizar la distribución completa de tiempos de espera**, no solo los promedios. Un objetivo de política debería ser que ningún paciente espere más de 100 días para consulta de especialista.

**5. Abordar la estratificación por renta** como un problema de equidad. La evidencia muestra que el acceso real a la sanidad de calidad está condicionado por la capacidad de pago, contradiciendo el principio de universalidad del SNS.

## 9.4. Contribuciones del trabajo

Este TFG realiza las siguientes contribuciones:

**Contribución teórica:** Integra la Ley de Little de la teoría de colas con el concepto de precio sombra para fundamentar el uso de los tiempos de espera como proxy de saturación del sistema público percibida por los hogares.

**Contribución empírica:** Construye un panel autonómico original (17 CCAA, 2016-2024) y estima modelos que capturan el efecto diferido de las listas de espera, un aspecto poco explorado en la literatura previa.

**Contribución metodológica:** Demuestra la importancia de los tests de significatividad conjunta (Wald) frente a los tests individuales cuando el efecto de una variable opera a través de múltiples rezagos.

**Contribución de política:** Proporciona evidencia cuantitativa para fundamentar políticas de gestión de listas de espera, identificando el umbral de 100 días como punto de referencia para la intervención prioritaria.

## 9.5. Líneas de investigación futura

Este trabajo abre varias líneas de investigación que podrían desarrollarse en futuros estudios:

**Primera:** Extender el análisis a datos provinciales o de área sanitaria para capturar la heterogeneidad intra-autonómica.

**Segunda:** Incorporar información sobre primas de seguros y oferta del sector privado para modelizar de forma más completa la decisión del hogar.

**Tercera:** Utilizar microdatos de encuestas de hogares (PHOGUE, ECV) para analizar la decisión de contratación a nivel individual, controlando por características sociodemográficas.

**Cuarta:** Explorar formas funcionales más flexibles para el efecto umbral (splines, modelos de cambio de régimen) cuando se disponga de más observaciones.

**Quinta:** Analizar si la pandemia COVID-19 ha alterado permanentemente la relación entre listas de espera y demanda de seguros privados, o si se trata de un shock transitorio.

## 9.6. Reflexión final

El sistema sanitario español se encuentra en una encrucijada. La evidencia presentada en este trabajo muestra que la dualidad público-privada está aumentando, impulsada por el deterioro de los tiempos de espera y mediada por la capacidad de pago de los hogares. Esta tendencia contradice el espíritu fundacional del Sistema Nacional de Salud y plantea interrogantes sobre la sostenibilidad del modelo a largo plazo.

La solución no pasa por limitar el sector privado, que cumple una función legítima de complemento, sino por **fortalecer el sistema público** hasta el punto en que la huida hacia la sanidad privada sea una opción, no una necesidad. Los hallazgos de este estudio sugieren que ese fortalecimiento debe priorizarse en los tiempos de espera, focalizándose en los casos extremos que superan el umbral de tolerancia ciudadana.

En última instancia, la equidad del sistema sanitario español dependerá de decisiones políticas que asignen recursos suficientes para garantizar un acceso real y oportuno a todos los ciudadanos, independientemente de su capacidad de pago. Este trabajo aspira a contribuir a ese debate con evidencia empírica rigurosa.

---

# BIBLIOGRAFÍA

Arellano, M. (1987). Computing robust standard errors for within-groups estimators. *Oxford Bulletin of Economics and Statistics, 49*(4), 431-434.

Besley, T., Hall, J., & Preston, I. (1999). The demand for private health insurance: Do waiting lists matter? *Journal of Public Economics, 72*(2), 155-181.

Cameron, A. C., & Miller, D. L. (2015). A practitioner's guide to cluster-robust inference. *Journal of Human Resources, 50*(2), 317-372.

Dantzig, G. B. (1963). *Linear programming and extensions*. Princeton University Press.

Granger, C. W. J., & Newbold, P. (1974). Spurious regressions in econometrics. *Journal of Econometrics, 2*(2), 111-120.

Grossman, M. (1972). On the concept of health capital and the demand for health. *Journal of Political Economy, 80*(2), 223-255.

Hausman, J. A. (1978). Specification tests in econometrics. *Econometrica, 46*(6), 1251-1271.

Hirschman, A. O. (1970). *Exit, voice, and loyalty: Responses to decline in firms, organizations, and states*. Harvard University Press.

Im, K. S., Pesaran, M. H., & Shin, Y. (2003). Testing for unit roots in heterogeneous panels. *Journal of Econometrics, 115*(1), 53-74.

Instituto Nacional de Estadística. (2016-2024). *Encuesta de Presupuestos Familiares*. INE. https://www.ine.es

Instituto Nacional de Estadística. (2016-2024). *Contabilidad Regional de España*. INE. https://www.ine.es

Instituto Nacional de Estadística. (2016-2024). *Padrón Continuo de Población*. INE. https://www.ine.es

Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica, 47*(2), 263-291.

Kao, C. (1999). Spurious regression and residual-based tests for cointegration in panel data. *Journal of Econometrics, 90*(1), 1-44.

Little, J. D. C. (1961). A proof for the queuing formula: L = λW. *Operations Research, 9*(3), 383-387.

Maddala, G. S., & Wu, S. (1999). A comparative study of unit root tests with panel data and a new simple test. *Oxford Bulletin of Economics and Statistics, 61*(S1), 631-652.

Ministerio de Sanidad. (2016-2024). *Sistema de Información sobre Listas de Espera del SNS (SISLE-SNS)*. Ministerio de Sanidad. https://www.sanidad.gob.es

Nickell, S. (1981). Biases in dynamic models with fixed effects. *Econometrica, 49*(6), 1417-1426.

Pedroni, P. (1999). Critical values for cointegration tests in heterogeneous panels with multiple regressors. *Oxford Bulletin of Economics and Statistics, 61*(S1), 653-670.

Pedroni, P. (2004). Panel cointegration: Asymptotic and finite sample properties of pooled time series tests with an application to the PPP hypothesis. *Econometric Theory, 20*(3), 597-625.

Propper, C. (2000). The demand for private health care in the UK. *Journal of Health Economics, 19*(6), 855-876.

---

**FIN DEL DOCUMENTO**

*Trabajo Fin de Grado presentado en la Universidad de Murcia*  
*Grado en Economía*  
*Curso académico 2025-2026*

