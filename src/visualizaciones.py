from pathlib import Path
import unicodedata

import matplotlib.pyplot as plt
import seaborn as sns


"""Funciones para crear y guardar visualizaciones del análisis exploratorio.

Las funciones de este módulo reciben un DataFrame con la estructura del dataset
de clientes y generan gráficos relacionados con la variable objetivo ``Churn``.
Las figuras se guardan como archivos PNG y también se devuelven para poder
mostrarlas desde el notebook.
"""


def graficar_distribucion_churn(df, ruta_salida="../resultados/plots/distribucion_variable_objetivo.png"):
    """Crea un gráfico de barras con la distribución de clientes según Churn.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene la columna ``Churn`` con los valores ``Yes`` y
        ``No``.
    ruta_salida : str or pathlib.Path, optional
        Ruta del archivo PNG donde se guardará la figura.

    Returns
    -------
    tuple
        La figura de Matplotlib y el eje que contiene el gráfico.
    """
    datos = df.copy()
    datos["Churn"] = datos["Churn"].map({"Yes": "Sí", "No": "No"})

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(
        data=datos,
        x="Churn",
        hue="Churn",
        order=["No", "Sí"],
        palette=["#4C72B0", "#C44E52"],
        width=0.65,
        legend=False,
        ax=ax
    )

    for container in ax.containers:
        ax.bar_label(container, fmt="%d", padding=3)

    ax.set_title("Distribución de la variable objetivo", fontsize=16, fontweight="bold")
    ax.set_xlabel("Abandono del servicio")
    ax.set_ylabel("Cantidad de clientes")
    ax.set_ylim(0, datos["Churn"].value_counts().max() * 1.1)

    ruta = Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, dpi=300, bbox_inches="tight")

    return fig, ax


def graficar_curvas_densidad_churn(
    df,
    ruta_salida="../resultados/plots/curvas_densidad_churn.png"
):
    """Crea y guarda curvas KDE para variables numéricas según Churn.

    La figura contiene las distribuciones de ``tenure``, ``MonthlyCharges`` y
    ``TotalCharges`` organizadas en una cuadrícula de dos columnas. Las curvas
    se diferencian según si el cliente abandonó o no el servicio.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las variables numéricas y la columna ``Churn``.
    ruta_salida : str or pathlib.Path, optional
        Ruta del archivo PNG donde se guardará la figura completa.

    Returns
    -------
    tuple
        La figura de Matplotlib y el arreglo de ejes utilizados.
    """
    datos = df.copy()
    datos["Churn"] = datos["Churn"].map({"Yes": "Sí", "No": "No"})

    variables = {
        "tenure": ("Antiguedad del cliente", "Antiguedad (meses)"),
        "MonthlyCharges": ("Cargos mensuales", "Cargos mensuales ($)"),
        "TotalCharges": ("Cargos totales", "Cargos totales ($)")
    }

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "Distribución de variables numéricas según abandono",
        fontsize=16,
        fontweight="bold"
    )
    axes = axes.ravel()

    for indice, (variable, (titulo, etiqueta_x)) in enumerate(variables.items()):
        sns.kdeplot(
            data=datos,
            x=variable,
            hue="Churn",
            fill=True,
            palette=["#4C72B0", "#C44E52"],
            common_norm=False,
            multiple="layer",
            alpha=0.45,
            ax=axes[indice]
        )
        axes[indice].set_title(titulo)
        axes[indice].set_xlabel(etiqueta_x)
        axes[indice].set_ylabel("Densidad")

        figura_individual, eje_individual = plt.subplots(figsize=(8, 6))
        sns.kdeplot(
            data=datos,
            x=variable,
            hue="Churn",
            fill=True,
            palette=["#4C72B0", "#C44E52"],
            common_norm=False,
            multiple="layer",
            alpha=0.45,
            ax=eje_individual
        )
        eje_individual.set_title(titulo)
        eje_individual.set_xlabel(etiqueta_x)
        eje_individual.set_ylabel("Densidad")
        nombre_individual = f"curva_densidad_{variable}.png"
        figura_individual.savefig(
            Path(ruta_salida).parent / nombre_individual,
            dpi=300,
            bbox_inches="tight"
        )
        plt.close(figura_individual)

    axes[3].set_visible(False)
    fig.subplots_adjust(wspace=0.3, hspace=0.35, top=0.88)

    ruta = Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, dpi=300, bbox_inches="tight")

    return fig, axes


GRUPOS_CATEGORICOS = {
    "Información del cliente": ["gender", "SeniorCitizen", "Partner", "Dependents"],
    "Servicios contratados": ["PhoneService", "MultipleLines", "InternetService", "StreamingTV", "StreamingMovies"],
    "Seguridad y soporte": ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport"],
    "Información de pago": ["Contract", "PaperlessBilling", "PaymentMethod"]
}

NOMBRES_VARIABLES = {
    "gender": "Género",
    "SeniorCitizen": "Adulto mayor",
    "Partner": "Pareja",
    "Dependents": "Personas dependientes",
    "PhoneService": "Servicio telefónico",
    "MultipleLines": "Líneas múltiples",
    "InternetService": "Servicio de internet",
    "StreamingTV": "Televisión por streaming",
    "StreamingMovies": "Películas por streaming",
    "OnlineSecurity": "Seguridad en línea",
    "OnlineBackup": "Respaldo en línea",
    "DeviceProtection": "Protección del dispositivo",
    "TechSupport": "Soporte técnico",
    "Contract": "Tipo de contrato",
    "PaperlessBilling": "Facturación electrónica",
    "PaymentMethod": "Método de pago"
}

TRADUCCIONES_CATEGORIAS = {
    "Female": "Mujer",
    "Male": "Hombre",
    "Yes": "Sí",
    "No": "No",
    "No phone service": "Sin servicio telefónico",
    "Fiber optic": "Fibra óptica",
    "No internet service": "Sin servicio de internet",
    "Month-to-month": "Mes a mes",
    "One year": "Un año",
    "Two year": "Dos años",
    "Electronic check": "Cheque electrónico",
    "Mailed check": "Cheque enviado por correo",
    "Bank transfer (automatic)": "Transferencia bancaria (automática)",
    "Credit card (automatic)": "Tarjeta de crédito (automática)"
}


def _nombre_archivo(texto):
    """Convierte un texto en un nombre de archivo simple y portable."""
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return texto.lower().replace(" ", "_")


def _crear_countplot(datos, variable, ax):
    """Dibuja un countplot categórico con formato y etiquetas consistentes.

    Parameters
    ----------
    datos : pandas.DataFrame
        DataFrame preparado con las etiquetas de ``Churn`` traducidas.
    variable : str
        Nombre de la variable categórica que se representará en el eje X.
    ax : matplotlib.axes.Axes
        Eje donde se dibujará el gráfico.
    """
    sns.countplot(
        data=datos,
        x=variable,
        hue="Churn",
        hue_order=["No", "Sí"],
        palette=["#4C72B0", "#C44E52"],
        width=0.65,
        ax=ax
    )

    etiquetas = [
        TRADUCCIONES_CATEGORIAS.get(etiqueta.get_text(), etiqueta.get_text())
        for etiqueta in ax.get_xticklabels()
    ]
    ax.set_xticks(range(len(etiquetas)))
    ax.set_xticklabels(etiquetas, rotation=15 if variable == "PaymentMethod" else 0)
    ax.set_title(NOMBRES_VARIABLES[variable])
    ax.set_xlabel("")
    ax.set_ylabel("Cantidad de clientes")
    ax.margins(y=0.12)

    for container in ax.containers:
        ax.bar_label(container, fmt="%d", padding=3, fontsize=9)


def graficar_grupos_categoricos_churn(
    df,
    ruta_salida="../resultados/plots"
):
    """Genera visualizaciones categóricas agrupadas según el abandono.

    Para cada grupo de variables se crea una sábana con dos gráficos por fila.
    Además, se guarda un PNG individual por variable. Los títulos y categorías
    se traducen al español, se muestran los conteos sobre las barras y solo el
    gráfico de ``PaymentMethod`` se presenta sin leyenda.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contiene las variables categóricas y la columna ``Churn``.
    ruta_salida : str or pathlib.Path, optional
        Directorio donde se guardarán las sábanas y los gráficos individuales.

    Returns
    -------
    list
        Lista con las figuras agrupadas generadas por cada grupo.
    """
    datos = df.copy()
    datos["Churn"] = datos["Churn"].map({"Yes": "Sí", "No": "No"})
    ruta = Path(ruta_salida)
    ruta.mkdir(parents=True, exist_ok=True)
    figuras = []

    for nombre_grupo, variables in GRUPOS_CATEGORICOS.items():
        cantidad_filas = (len(variables) + 1) // 2
        figura_grupo, ejes = plt.subplots(
            cantidad_filas,
            2,
            figsize=(15, 5.2 * cantidad_filas)
        )
        ejes = ejes.reshape(-1)
        figura_grupo.suptitle(
            f"Distribución de {nombre_grupo} según abandono",
            fontsize=16,
            fontweight="bold"
        )

        for indice, variable in enumerate(variables):
            _crear_countplot(datos, variable, ejes[indice])
            if variable == "PaymentMethod":
                ejes[indice].get_legend().remove()
            else:
                ejes[indice].legend(title="Abandono")

            figura_individual, eje_individual = plt.subplots(figsize=(9, 7))
            _crear_countplot(datos, variable, eje_individual)
            if variable == "PaymentMethod":
                eje_individual.get_legend().remove()
            else:
                eje_individual.legend(title="Abandono")

            nombre_individual = f"{_nombre_archivo(nombre_grupo)}_{variable}.png"
            figura_individual.savefig(
                ruta / nombre_individual,
                dpi=300,
                bbox_inches="tight"
            )
            plt.close(figura_individual)

        for eje in ejes[len(variables):]:
            eje.set_visible(False)

        figura_grupo.subplots_adjust(
            wspace=0.3,
            hspace=0.4,
            top=0.88,
            bottom=0.1
        )
        nombre_grupo_archivo = f"grupo_{_nombre_archivo(nombre_grupo)}.png"
        figura_grupo.savefig(
            ruta / nombre_grupo_archivo,
            dpi=300,
            bbox_inches="tight"
        )
        figuras.append(figura_grupo)

    return figuras
