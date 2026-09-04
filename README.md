# Informe técnico en formato Markdown (.md)

# Aquí se deberá documentar de manera estructurada todo el desarrollo del proyecto de Machine Learning.

# Descripción del problema de negocio.
Para las empresas de telecomunicaciones, la retención de clientes es un desafío empresarial crítico. En un mercado donde los usuarios dependen de la conectividad diaria y pueden migrar fácilmente hacia la competencia ante la más mínima interrupción o mala experiencia, la tasa de abandono (churn) representa uno de los mayores riesgos financieros del sector. Considerando que adquirir un nuevo usuario cuesta hasta cinco veces más que retener a uno actual, no controlar el churn se traduce en una pérdida directa de ingresos que amenaza la rentabilidad de la compañía.

Para hacer frente a este problema, el principal desafío analítico debe ser comprender los factores que impulsan las cancelaciones y, sobre todo, predecir qué clientes específicos están en riesgo de abandonar el servicio. Mediante el análisis profundo de los datos y la implementación de modelos predictivos de churn, las empresas de telecomunicaciones pueden anticiparse a las bajas, diseñar estrategias de retención segmentadas y mejorar proactivamente la experiencia del usuario, convirtiendo la fidelización en un motor de crecimiento sostenible.

# Objetivos del proyecto.
Objetivo general del proyecto:
    
- Desarrollar un modelo de Machine Learning capaz de predecir la probabilidad de que un cliente abandone la empresa, permitiendo al equipo de marketing y retención intervenir de manera proactiva.

Objetivos específicos de esta primera fase de exploración:

- Auditar y limpiar la calidad de los datos.
- Construir el perfil demográfico y de consumo de los clientes que ya hicieron churn frente a los que se mantienen.
- Determinar qué factores tienen mayor correlación estadística con el abandono.
- Preparar el dataset y dejarlo listo para la fase de modelado algorítmico.

# Definición de KPIs que resolverán el problema de negocio.
Dado que aún no se implementará el modelo predictivo, el éxito de esta primera fase se medirá por la calidad de la información extraída y la calidad del dataset:

- Lograr un data set con 0% de valores nulos ni inconsistencias tras el proceso de limpieza.
- Cuantificar la proporción exacta de la clase objetivo para determinar qué técnica de balanceo se requerirá en la siguiente fase.
- Generar un reportes con al menos 5 variables de alto impacto en churn que estén visualmente demostradas.

# Descripción de las fuentes de datos utilizadas.
El conjunto de datos contiene información sobre los clientes de una empresa de telecomunicaciones y si se dieron de baja (cancelaron su servicio) o no. Cada fila representa a un cliente, cada columna contiene los atributos del cliente descritos.

El conjunto de datos incluye información sobre:

- Clientes que se dieron de baja en el último mes – la columna se llama Churn (tasa de abandono).
- Servicios a los que cada cliente se ha suscrito – teléfono, múltiples líneas, internet, seguridad en línea, respaldo en línea, protección de dispositivos, soporte técnico y streaming de TV y películas.
- Información de la cuenta del cliente – cuánto tiempo llevan como clientes, contrato, método de pago, facturación electrónica, cargos mensuales y cargos totales.
- Información demográfica sobre los clientes – género, rango de edad, y si tienen pareja y dependientes.

# Análisis exploratorio de los datos (EDA).
# Preparación para modelado

## Criterios de selección de variables predictoras


* Validación Matemática (V de Cramér - Pearson): Se priorizaron las variables categóricas con un puntaje superior a 0.3, un umbral estadístico robusto en el sector de telecomunicaciones para asegurar que la característica tenga un peso predictivo real sobre el abandono.

* Validación Visual: Los cortes estadísticos no fueron absolutos. Variables con baja correlación (como PaperlessBilling, con 0.191) se conservaron porque los gráficos de distribución evidenciaron empíricamente una separación clara en las tendencias de retención, justificando su influencia en el modelo.


## Transformación de datos en el Pipeline (Imputación y codificación)


Para asegurar un flujo de datos limpio, escalable y libre de fugas de información, el preprocesamiento se automatizó mediante pipelines, destacando las siguientes etapas:

* Imputación de Valores Faltantes: Se implementaron transformadores (como SimpleImputer) para manejar de forma automatizada las inconsistencias y valores nulos descubiertos durante la estandarización de formatos.Y KNN para preservar mejor la distribución original de los datos numericos en comparativa con los métodos univariados simples, teniendo en cuenta la reducida cantidad de valores nulos detectados.

* Codificación de Variables Categóricas: Se aplicó One-Hot Encoding para las variables nominales para no generar jerarquías matemáticas falsa. Y StandarScaler para la estandarización simple teniendo en cuenta la ausencia de valores atipico y la diferencia de magnitudes de las variables numericas.

### Tabla de correlaciones con la variable objetivo:


* Variables Categóricas


| Variable | Correlación (V de Cramér) |
| :--- | :---: |
| **Contract** | 0.410 |
| **OnlineSecurity** | 0.347 |
| **TechSupport** | 0.343 |
| **InternetService** | 0.322 |
| **PaymentMethod** | 0.303 |
| **OnlineBackup** | 0.292 |
| **DeviceProtection** | 0.281 |
| **StreamingMovies** | 0.230 |
| **StreamingTV** | 0.230 |
| **PaperlessBilling** | 0.191 |
| **Dependents** | 0.163 |
| **SeniorCitizen** | 0.150 |
| **Partner** | 0.150 |
| **MultipleLines** | 0.036 |
| **PhoneService** | 0.000 |
| **gender** | 0.000 |


* Variables Numéricas


| Variable | Correlación (Pearson) |
| :--- | :---: |
| **tenure** | -0.350 |
| **TotalCharges** | -0.200 |
| **MonthlyCharges** | 0.190 |

# Evaluación de sesgos, aspectos éticos y estándares de privacidad

Impacto de los errores de predicción: Los Falsos Negativos (FN) resultan en la pérdida inevitable de clientes, mientras que los Falsos Positivos (FP) provocan gastos ineficientes en estrategias de retención y marketing.

Sesgo por desbalance de datos: El modelo está desbalanceado. Para hacerlo equitativo con la clase minoritaria (Churn), se requiere aplicar técnicas de re-muestreo exclusivamente sobre el conjunto de entrenamiento.

Solución propuesta (SMOTE): Se recomienda implementar SMOTE para generar datos sintéticos de la clase minoritaria basándose en vecinos cercanos. Esto evita la duplicidad exacta de datos y ayuda al algoritmo a definir mejores fronteras de decisión.

Aspectos eticos y de privacidad:

Exigencias normativas y sanciones regulatorias: Las legislaciones actuales de privacidad (GDPR y Ley 21.719) exigen el consentimiento explícito, protegen el uso de datos sensibles y regulan las decisiones algorítmicas (otorgando derecho a explicación humana). Su incumplimiento conlleva multas severas de hasta el 4% de la facturación anual.

Vulnerabilidad del conjunto de datos: Actualmente, el dataset infringe la normativa al carecer de protección sobre la Información de Identificación Personal (PII), exponiendo directamente el identificador del cliente (CustomerID) junto a su comportamiento financiero y personal.

Medidas de protección y mitigación propuestas: Para cumplir con la ley y garantizar la privacidad, se aplicarán las siguientes estrategias:

Seudonimización (Hashing): Transformar identificadores directos en códigos irreversibles.

Minimización de datos: Utilizar estrictamente las variables necesarias para el modelo, descartando información sensible o redundante.

Gobernanza y seguridad: Implementar Control de Acceso Basado en Roles (RBAC) para restringir el manejo de los datos solo al personal autorizado.

Transparencia: Habilitar canales formales para que los usuarios puedan ejercer sus derechos ARCO+ (Acceso, Rectificación, Cancelación, Oposición y Portabilidad).

# Metodología utilizada (CRISP-DM).
