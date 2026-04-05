def calcular_hits_totales(datos):
    """
    Calcula la cantidad total de hits de un participante.

    Recorre la lista de hits del participante y cuenta cuántos valores son True.

    Parámetros:
        datos (dict): diccionario de un participante con la clave "hit" 
                      que contiene una lista de booleanos.

    Retorna:
        int: cantidad total de hits registrados.
    """
    total = 0
    for valor in datos["hit"]:
        if valor == True:
            total = total + 1
    return total


def calcular_tiempo_primer_hit(datos):
    """
    Devuelve el tiempo en que ocurrió el primer hit del participante.

    Recorre la lista de hits y retorna el tiempo correspondiente
    al primer valor True que encuentre.

    Parámetros:
        datos (dict): diccionario de un participante con las claves "hit" 
                      y "tiempo", ambas listas del mismo largo.

    Retorna:
        float: tiempo del primer hit en segundos.
        None: si no se registró ningún hit.
    """
    for i in range(len(datos["hit"])):
        if datos["hit"][i] == True:
            return datos["tiempo"][i]
    return None  # si no hubo ningún hit



