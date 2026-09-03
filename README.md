# Informe técnico en formato Markdown (.md)

# Aquí se deberá documentar de manera estructurada todo el desarrollo del proyecto de Machine Learning.

# Secciones mínimas:

# Descripción del problema de negocio.
Para las empresas de telecomunicaciones, la retención de clientes es un desafío empresarial crítico. En un mercado donde los usuarios dependen de la conectividad diaria y pueden migrar fácilmente hacia la competencia ante la más mínima interrupción o mala experiencia, la tasa de abandono (churn) representa uno de los mayores riesgos financieros del sector. Considerando que adquirir un nuevo usuario cuesta hasta cinco veces más que retener a uno actual, no controlar el churn se traduce en una pérdida directa de ingresos que amenaza la rentabilidad de la compañía.

Para hacer frente a este problema, el principal desafío analítico debe ser comprender los factores que impulsan las cancelaciones y, sobre todo, predecir qué clientes específicos están en riesgo de abandonar el servicio. Mediante el análisis profundo de los datos y la implementación de modelos predictivos de churn, las empresas de telecomunicaciones pueden anticiparse a las bajas, diseñar estrategias de retención segmentadas y mejorar proactivamente la experiencia del usuario, convirtiendo la fidelización en un motor de crecimiento sostenible.

# Objetivos del proyecto.
Análisis de posibles clientes con probabilidad de abandonar el servicio, basado en características numéricas y categóricas para intentar responder preguntas tales como:
- ¿Cuál es el porcentaje de clientes que se dan de baja (churn) frente a los que mantienen sus servicios activos?
- ¿Existe algún patrón o preferencia entre los clientes que se dan de baja según el tipo de servicio proporcionado?

# Definición de KPIs que resolverán el problema de negocio.

# Descripción de las fuentes de datos utilizadas.
El conjunto de datos contiene información sobre los clientes de una empresa de telecomunicaciones y si se dieron de baja (cancelaron su servicio) o no. Cada fila representa a un cliente, cada columna contiene los atributos del cliente descritos en los metadatos de la columna.

El conjunto de datos incluye información sobre:

    - Clientes que se dieron de baja en el último mes – la columna se llama Churn (tasa de abandono).

    - Servicios a los que cada cliente se ha suscrito – teléfono, múltiples líneas, internet, seguridad en línea, respaldo en línea, protección de dispositivos, soporte técnico y streaming de TV y películas.

    - Información de la cuenta del cliente – cuánto tiempo llevan como clientes, contrato, método de pago, facturación electrónica, cargos mensuales y cargos totales.

    - Información demográfica sobre los clientes – género, rango de edad, y si tienen pareja y dependientes.

# Preparación y análisis exploratorio de los datos (EDA).
# Metodología utilizada (CRISP-DM).
