def filtrar_por_participante(datos, id_participante):
    """
    Busca y devuelve el registro correspondiente a un participante específico.

    Recorre la lista de registros y retorna el diccionario cuyo
    id_participante coincida con el valor indicado.

    Parámetros:
        datos (list): lista de diccionarios, uno por participante.
        id_participante (int): identificador del participante a buscar.

    Retorna:
        dict: diccionario del participante con sus datos completos.
        None: si no se encontró ningún participante con ese id.
    """
    for registro in datos:
        if registro["id_participante"] == id_participante:
            return registro
    return None  # si no se encontró el participante