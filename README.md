# Informe Técnico

# Problema de negocio
Para las empresas de telecomunicaciones, la retención de clientes es un desafío empresarial crítico. En un mercado donde los usuarios dependen de la conectividad diaria y pueden migrar fácilmente hacia la competencia ante la más mínima interrupción o mala experiencia, la tasa de abandono (churn) representa uno de los mayores riesgos financieros del sector. Considerando que adquirir un nuevo usuario cuesta hasta cinco veces más que retener a uno actual, no controlar el churn se traduce en una pérdida directa de ingresos que amenaza la rentabilidad de la compañía.

Para hacer frente a este problema, el principal desafío analítico debe ser comprender los factores que impulsan las cancelaciones y, sobre todo, predecir qué clientes específicos están en riesgo de abandonar el servicio. Mediante el análisis profundo de los datos y la implementación de modelos predictivos de churn, las empresas de telecomunicaciones pueden anticiparse a las bajas, diseñar estrategias de retención segmentadas y mejorar proactivamente la experiencia del usuario, convirtiendo la fidelización en un motor de crecimiento sostenible.

# Objetivos del proyecto
#### Objetivo general del proyecto:
- Desarrollar un modelo de Machine Learning capaz de predecir la probabilidad de que un cliente abandone la empresa, permitiendo al equipo de marketing y retención intervenir de manera proactiva.

#### Objetivos específicos de esta primera fase de exploración:
- Auditar y limpiar la calidad de los datos.
- Construir el perfil demográfico y de consumo de los clientes que ya hicieron churn frente a los que se mantienen.
- Determinar qué factores tienen mayor correlación estadística con el abandono.
- Preparar el dataset y dejarlo listo para la fase de modelado algorítmico.

# KPIs que resolverán el problema de negocio
Dado que aún no se implementará el modelo predictivo, el éxito de esta primera fase se medirá por la calidad de la información extraída y la calidad del dataset:

- Lograr un data set con 0% de valores nulos ni inconsistencias tras el proceso de limpieza.
- Cuantificar la proporción exacta de la clase objetivo para determinar qué técnica de balanceo se requerirá en la siguiente fase.
- Generar un reportes con al menos 5 variables de alto impacto en churn que estén visualmente demostradas.

# Descripción General y Calidad del Conjunto de Datos
El conjunto de datos contiene información sobre los clientes de una empresa de telecomunicaciones y si se dieron de baja (cancelaron su servicio) o no. Cada fila representa a un cliente, cada columna contiene los atributos del cliente descritos. El conjunto de datos original está compuesto por 7043 registros y 21 características.

#### El conjunto de datos incluye información sobre:

* Clientes que se dieron de baja en el último mes – la columna se llama Churn (tasa de abandono).
* Servicios a los que cada cliente se ha suscrito – teléfono, múltiples líneas, internet, seguridad en línea, respaldo en línea, protección de dispositivos, soporte técnico y streaming de TV y películas.
* Información de la cuenta del cliente – cuánto tiempo llevan como clientes, contrato, método de pago, facturación electrónica, cargos mensuales y cargos totales.
* Información demográfica sobre los clientes – género, rango de edad, y si tienen pareja y dependientes.

#### Calidad de Datos:

* Variables Categóricas: Alta presencia de datos cualitativos estructurados como texto.
* Duplicidad: No se han detectado registros duplicados en el conjunto de datos.
* Completitud: La integridad de los datos es excelente. El único hallazgo de valores nulos se
presentó en la variable TotalCharges (11 registros faltantes), los cuales corresponden
estrictamente a clientes con una antiguedad (tenure) de 0 meses.
* Análisis de Valores Atípicos (Outliers): Se evaluaron las variables numéricas continuas
mediante el método de Rango Intercuartil (IQR). Los resultados indicaron una ausencia
total de valores atípicos en las características tenure, MonthlyCharges y
TotalCharges.

# Análisis exploratorio de los datos (EDA)
## Resultados de Análisis Univariado
#### Perfil del Cliente y Abandono
- Abandono (Churn): El 26,5% de los usuarios (1.869 personas) decide cancelar el servicio (Churn = Yes). Esto nos indica que, en promedio, uno de cada cuatro clientes termina dejando la empresa.
- Género: La distribución por género es muy equilibrada y no muestra diferencias importantes. Contamos con 3.555 hombres y 3.488 mujeres, por lo que la base de clientes está repartida casi a la par.
- Edad: La gran mayoría de los clientes no son adultos mayores. El grupo más joven (SeniorCitizen = 0) representa el 83,8% del total, lo que nos dice que la empresa atrae principalmente a un público de menor edad.

#### Servicios y Contratos
- Contratos: El formato mes a mes es la opción favorita, elegida por 3.875 clientes. Esto equivale al 55% del total, lo que demuestra que la mayoría prefiere mantener flexibilidad a corto plazo en lugar de amarrarse a contratos anuales.
- Telefonía: El servicio telefónico es indispensable para casi todos los usuarios. Cerca del 90,3% cuenta con él, lo que lo convierte en el servicio básico más popular y establecido entre los clientes.

#### Antiguedad y Pagos
- Antigüedad: Los clientes se mantienen en la empresa un promedio de 32,37 meses, con una mediana de 29 meses. Esto muestra que, a pesar de las bajas, existe un grupo importante de personas que permanece fiel por más de dos años.
- Cargos Mensuales: Lo que pagan los clientes cada mes varía desde los $18,25 hasta los $118,75, con una mediana de $70,35. Esta amplia diferencia de precios refleja que los usuarios eligen planes y combinaciones de servicios muy distintos entre sí.
- Cargos Totales: El dinero total que han pagado los clientes tiene una mediana de $1.394,55 y un promedio de $2.279,73. Esta diferencia tan marcada ocurre porque existe un grupo de clientes antiguos que ha acumulado pagos muy altos a lo largo de los años.

## Resultados Análisis Bivariado
#### **Antigüedad y Costos**
* **Tiempo en la empresa:** Los clientes que se quedan llevan un promedio de 37,57 meses, mientras que quienes se van lo hacen a los 17,98 meses. Esto nos indica que los primeros meses son críticos, ya que a mayor tiempo de permanencia, la lealtad aumenta y la probabilidad de perderlos disminuye.
* **Pagos Mensuales:** Las personas que cancelan el servicio pagan en promedio $74,44 al mes, una cifra superior a los $61,27 de los usuarios activos. Queda en evidencia que las tarifas más altas son un factor de peso que empuja a los clientes a buscar otras opciones.
* **Gastos Acumulados:** Los usuarios que mantienen su suscripción han acumulado un pago promedio de $2.554,77, frente a los $1.531,80 de quienes se dan de baja. Esto es un reflejo del tiempo en la empresa, demostrando que quienes tienen un historial de pagos más largo son también los más fieles.

#### **Perfil del Cliente**
* **Género y Familia:** Ser hombre o mujer no influye en la decisión de cancelar, pero la situación familiar sí marca una diferencia. Los clientes que viven solos, sin pareja ni personas a cargo, tienen más probabilidades de dejar la compañía, quizás porque tienen mayor facilidad para cambiar de proveedor.
* **Edad:** El grupo de adultos mayores presenta una tasa de abandono muy alta, al punto que la gran mayoría termina cancelando el servicio. Esto sugiere fuertemente que la oferta actual podría no estar ajustándose bien a las necesidades o al presupuesto de este grupo de edad.

#### **Servicios de Internet y Complementos**
* **Tipo de Conexión:** Aunque muchos clientes eligen la fibra óptica, este grupo presenta una gran cantidad de cancelaciones, lo que apunta a una posible insatisfacción con la calidad o el precio del servicio. Por el contrario, los usuarios con conexión tradicional (DSL) o sin internet son mucho más estables y rara vez abandonan la empresa.
* **Servicios de Protección:** Agregar seguridad en línea y soporte técnico es la mejor defensa para la empresa, ya que reduce las cancelaciones del 42% a solo un 15%. Del mismo modo, ofrecer respaldo y protección de equipos baja las salidas del 40% al 22%, por lo que resulta indispensable crear promociones que incluyan estos complementos.

#### **Contratos, Facturación y Planes de Acción**
* **Duración del Contrato:** El formato de mes a mes es altamente inestable (42,7% de abandono), mientras que los contratos de uno y dos años casi no presentan salidas (11,2% y 2,8%). Es prioritario crear beneficios atractivos que motiven a los clientes a dar el salto hacia compromisos a largo plazo.
* **Facturación Digital:** Quienes reciben facturación electrónica cancelan el doble (33,5%) que los que usan la factura tradicional (16,3%). Como el entorno digital facilita la cancelación rápida, es necesario buscar nuevas formas de recordarle a este grupo los beneficios del servicio para convencerlos de quedarse.
* **Método de Pago:** El "cheque electrónico" representa un riesgo crítico, con un 45,2% de abandonos frente al 15-19% de otras alternativas. Se recomienda investigar urgentemente qué fricciones genera este método y hacer campañas para que los usuarios se cambien al pago automático.

# Preparación para modelado

# Evaluación de sesgos, aspectos éticos y estándares de privacidad
- Impacto de los errores de predicción: Los Falsos Negativos (FN) resultan en la pérdida inevitable de clientes, mientras que los Falsos Positivos (FP) provocan gastos ineficientes en estrategias de retención y marketing.
- Sesgo por desbalance de datos: El modelo está desbalanceado. Para hacerlo equitativo con la clase minoritaria (Churn), se requiere aplicar técnicas de re-muestreo exclusivamente sobre el conjunto de entrenamiento.
- Solución propuesta (SMOTE): Se recomienda implementar SMOTE para generar datos sintéticos de la clase minoritaria basándose en vecinos cercanos. Esto evita la duplicidad exacta de datos y ayuda al algoritmo a definir mejores fronteras de decisión.

#### Aspectos eticos y de privacidad:
- Exigencias normativas y sanciones regulatorias: Las legislaciones actuales de privacidad (GDPR y Ley 21.719) exigen el consentimiento explícito, protegen el uso de datos sensibles y regulan las decisiones algorítmicas (otorgando derecho a explicación humana). Su incumplimiento conlleva multas severas de hasta el 4% de la facturación anual.
- Vulnerabilidad del conjunto de datos: Actualmente, el dataset infringe la normativa al carecer de protección sobre la Información de Identificación Personal (PII), exponiendo directamente el identificador del cliente (CustomerID) junto a su comportamiento financiero y personal.

#### Medidas de protección y mitigación propuestas
Para cumplir con la ley y garantizar la privacidad, se aplicarán las siguientes estrategias:
- Seudonimización (Hashing): Transformar identificadores directos en códigos irreversibles.
- Minimización de datos: Utilizar estrictamente las variables necesarias para el modelo, descartando información sensible o redundante.
- Gobernanza y seguridad: Implementar Control de Acceso Basado en Roles (RBAC) para restringir el manejo de los datos solo al personal autorizado.
- Transparencia: Habilitar canales formales para que los usuarios puedan ejercer sus derechos ARCO (Acceso, Rectificación, Cancelación, Oposición y Portabilidad).

# Metodología utilizada (CRISP-DM).
