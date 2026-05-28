
def calcular_hits_totales(df):
    """
    Calcula la cantidad total de hits de un participante.

    Parámetros:
        df (DataFrame): datos de un participante.

    Retorna:
        int: cantidad total de hits.
    """
    return df["hit"].sum()


def calcular_tiempo_primer_hit(df):
    """
    Devuelve el tiempo en que ocurrió el primer hit del participante.

    Parámetros:
        df (DataFrame): datos de un participante.

    Retorna:
        float: tiempo del primer hit en segundos.
        None: si no se registró ningún hit.
    """
    hits = df[df["hit"] == True]
    if len(hits) == 0:
        return None
    return hits["tiempo"].iloc[0]



