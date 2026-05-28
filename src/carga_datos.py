
import pandas as pd
import os

def cargar_datos(ruta):
    """
    Lee un archivo CSV usando Pandas y devuelve un DataFrame con los datos de la tarea motora.

    Parámetros:
        ruta (str): ruta al archivo CSV con los datos.

    Retorna:
        DataFrame: datos cargados en un DataFrame de Pandas.

    Lanza:
        FileNotFoundError: si el archivo no existe en la ruta indicada.
        ValueError: si el archivo está vacío o tiene campos nulos.
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {ruta}")

    df = pd.read_csv(ruta)

    if len(df) == 0:
        raise ValueError("El archivo está vacío")

    if df.isna().any().any():
        raise ValueError("El archivo contiene campos vacíos o valores nulos")

    return df


