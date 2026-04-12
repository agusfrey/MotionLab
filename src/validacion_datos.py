def validar_registro(registro):
    """
    Verifica que los datos de un participante sean correctos y válidos.

    Comprueba que hit sea True o False, que condicion sea
    'competencia' o 'cooperacion', y que el tiempo no sea negativo.

    Parámetros:
        registro (dict): diccionario de un participante con sus listas de datos.

    Retorna:
        bool: True si los datos son válidos, False si hay algún error.
    """
    try:
        for i in range(len(registro["tiempo"])):
            if registro["hit"][i] not in [True, False]:
                return False
            if registro["condicion"][i] not in ["competencia", "cooperacion"]:
                return False
            if registro["tiempo"][i] < 0:
                return False
        return True
    except:
        return False


def validar_linea(id_p, tiempo, x, y, hit, condicion):
    
    try:
        int(id_p)
    except:
        raise ValueError("ID inválido")

    try:
        float(tiempo)
    except:
        raise ValueError("Tiempo inválido")

    try:
        float(x)
        float(y)
    except:
        raise ValueError("Coordenadas inválidas")

    if hit != True and hit != False:
        raise ValueError("Hit inválido")

    if condicion == "":
        raise ValueError("Condición vacía")

    if tiempo < 0:
        raise ValueError("Tiempo negativo")

    return True
