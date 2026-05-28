
def filtrar_por_participante(df, id_participante):
    """
    Filtra el DataFrame para obtener los datos de un participante específico.

    Parámetros:
        df (DataFrame): datos completos de todos los participantes.
        id_participante (int): identificador del participante a buscar.

    Retorna:
        DataFrame: datos del participante, o None si no existe.
    """
    resultado = df[df["id_participante"] == id_participante]
    if len(resultado) == 0:
        return None
    return resultado
