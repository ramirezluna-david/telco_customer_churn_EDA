# Informe técnico en formato Markdown (.md)

# Aquí se deberá documentar de manera estructurada todo el desarrollo del proyecto de Machine Learning.

# Secciones mínimas:

# Descripción del problema de negocio.
La tasa de churn es una métrica que describe el número de clientes que cancelan o no renuevan su suscripción con una compañía.
Según los expertos, el costo de adquirir nuevos clientes es hasta cinco veces mayor que el de mantener a los clientes existentes. Para empresas de telecomunicación, es crucial atraer nuevos clientes y al mismo tiempo poder retenerlos. Cuando un cliente abandona es muy costoso para la compañía. El desafío principal es predecir si un cliente individual va a abandonar o no. El desafío extra es identificar los componentes principales que influencian el abandono. 

Para las empresas de telecomunicaciones, la retención de clientes es un desafío empresarial crítico. En un mercado donde los usuarios dependen de la conectividad diaria y pueden migrar fácilmente hacia la competencia ante la más mínima interrupción o mala experiencia, la tasa de abandono (churn) representa uno de los mayores riesgos financieros del sector. Considerando que adquirir un nuevo usuario cuesta hasta cinco veces más que retener a uno actual, no controlar el churn se traduce en una pérdida directa de ingresos que amenaza la rentabilidad de la compañía.

Para hacer frente a este problema, el principal objetivo analítico de las "telcos" debe ser comprender los factores que impulsan las cancelaciones y, sobre todo, predecir qué clientes específicos están en riesgo de abandonar el servicio. Mediante el análisis profundo de los datos y la implementación de modelos predictivos de churn, las empresas de telecomunicaciones pueden anticiparse a las bajas, diseñar estrategias de retención segmentadas y mejorar proactivamente la experiencia del usuario, convirtiendo la fidelización en un motor de crecimiento sostenible.

# Objetivos del proyecto.
Análisis de posibles clientes con probabilidad de abandonar el servicio, basado en características numéricas y categóricas.
Problema de clasificación binaria para un conjunto de datos desbalanceado.


# Definición de KPIs que resolverán el problema de negocio.

# Descripción de las fuentes de datos utilizadas.
El conjunto de datos de abandono (churn) de telecomunicaciones contiene información sobre los clientes de una empresa de telecomunicaciones y si se dieron de baja (cancelaron su servicio) o no. Cada fila representa a un cliente, cada columna contiene los atributos del cliente descritos en los metadatos de la columna.

El conjunto de datos incluye información sobre:

    - Clientes que se dieron de baja en el último mes – la columna se llama Churn (tasa de abandono).

    - Servicios a los que cada cliente se ha suscrito – teléfono, múltiples líneas, internet, seguridad en línea, respaldo en línea, protección de dispositivos, soporte técnico y streaming de TV y películas.

    - Información de la cuenta del cliente – cuánto tiempo llevan como clientes, contrato, método de pago, facturación electrónica, cargos mensuales y cargos totales.

    - Información demográfica sobre los clientes – género, rango de edad, y si tienen pareja y dependientes.

Atributos del dataset:

customerID (ID del Cliente): Identificador único alfanumérico asignado a cada cuenta.

gender (Género): Sexo del cliente (Masculino o Femenino).

SeniorCitizen (Adulto Mayor / Tercera Edad): Indica si el cliente es una persona de la tercera edad (1 para Sí, 0 para No).

Partner (Pareja / Cónyuge): Indica si el cliente está casado o convive con una pareja (Sí/No).

Dependents (Dependientes): Indica si el cliente tiene personas a su cargo económicamente, como hijos o familiares mayores (Sí/No).

tenure (Antigüedad / Permanencia): La cantidad de meses que el cliente ha mantenido su contrato activo con la empresa.

PhoneService (Servicio Telefónico): Indica si el cliente tiene contratada una línea telefónica básica (Sí/No).

MultipleLines (Múltiples Líneas): Indica si el cliente tiene contratada más de una línea telefónica (Sí, No, o "Sin servicio telefónico").

InternetService (Servicio de Internet): El tipo de tecnología de conexión a internet que usa el cliente (Fibra Óptica, DSL, o "No").

OnlineSecurity (Seguridad en Línea): Indica si el cliente paga por un servicio adicional de ciberseguridad, cortafuegos o antivirus (Sí, No, o "Sin servicio de internet").

OnlineBackup (Respaldo en Línea): Indica si el cliente tiene contratado un servicio de copias de seguridad en la nube (Sí, No, o "Sin servicio de internet").

DeviceProtection (Protección de Dispositivo): Indica si el cliente paga un seguro o garantía extendida para sus equipos físicos (Sí, No, o "Sin servicio de internet").
TechSupport (Soporte Técnico): Indica si el cliente paga por asistencia técnica especializada (Sí, No, o "Sin servicio de internet").

StreamingTV (Transmisión de TV): Indica si el cliente utiliza la red del proveedor para consumir televisión por streaming (Sí, No, o "Sin servicio de internet").

StreamingMovies (Transmisión de Películas): Indica si el cliente utiliza la red del proveedor para ver películas por streaming (Sí, No, o "Sin servicio de internet").

Contract (Tipo de Contrato): La modalidad de pago y compromiso del cliente (Mes a mes, 1 año, o 2 años).

PaperlessBilling (Facturación Electrónica): Indica si el cliente optó por recibir sus estados de cuenta sin papel, generalmente por correo (Sí/No).

PaymentMethod (Método de Pago): La vía utilizada para liquidar la factura (Cheque electrónico, Cheque por correo, Transferencia bancaria, o Tarjeta de crédito).

MonthlyCharges (Cargos Mensuales): El monto exacto que se le cobra al cliente cada mes por la suma de todos sus servicios.

TotalCharges (Cargos Totales): El monto financiero acumulado que el cliente ha pagado a lo largo de toda su historia con la empresa.

Churn (Abandono / Fuga de Clientes): Variable objetivo (Target). Indica si el cliente canceló sus servicios y abandonó la empresa en el último mes (Sí/No).

# Preparación y análisis exploratorio de los datos (EDA).
# Metodología utilizada (CRISP-DM).
