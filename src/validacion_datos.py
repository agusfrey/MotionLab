
def validar_datos(df):
    """
    Verifica que el DataFrame tenga datos válidos usando métodos vectorizados de Pandas.

    Valida tipos, rangos y consistencia de los datos sin usar bucles.

    Parámetros:
        df (DataFrame): datos cargados desde el archivo CSV.

    Retorna:
        bool: True si todos los datos son válidos.

    Lanza:
        ValueError: si algún dato no cumple con el tipo o rango esperado.
    """
    if (df["id_participante"] <= 0).any():
        raise ValueError("id_participante debe ser mayor a 0")

    if (df["tiempo"] < 0).any():
        raise ValueError("tiempo no puede ser negativo")

    if not df["tiempo"].is_monotonic_increasing:
        raise ValueError("tiempo no está ordenado de forma creciente")

    if not df["hit"].isin([True, False]).all():
        raise ValueError("hit debe ser True o False")

    if not df["condicion"].isin(["competencia", "cooperacion"]).all():
        raise ValueError("condicion debe ser competencia o cooperacion")

    return True
