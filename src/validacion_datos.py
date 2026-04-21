
def validar_registro(registro):
    """
    Verifica que los datos de un participante sean correctos y válidos.

    Comprueba que el tiempo sea creciente, que hit sea True o False,
    que condicion sea 'competencia' o 'cooperacion', y que el tiempo no sea negativo.

    Parámetros:
        registro (dict): diccionario de un participante con sus listas de datos.

    Retorna:
        bool: True si los datos son válidos.

    Lanza:
        ValueError: si algún valor no cumple con el tipo o rango esperado.
    """
    if len(registro["tiempo"]) == 0:
        raise ValueError("El registro no tiene datos para calcular las metricas" )

    for i in range(len(registro["tiempo"])):
        if registro["hit"][i] not in [True, False]:
            raise ValueError('hit inválido: debe ser True o False")
      if registro["condicion"][i] not in ["competencia", "cooperacion"]:
            raise ValueError("condicion inválida: debe ser competencia o cooperacion")
        if registro["tiempo"][i] < 0:
            raise ValueError("tiempo negativo, debe ser mayor a cero ")

    for i in range(1, len(registro["tiempo"])):
        if registro["tiempo"][i] <= registro["tiempo"][i - 1]:
            raise ValueError("tiempo no es creciente")

    return True
