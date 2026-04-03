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


# OPCIONAL
def calcular_hits_por_bloques(datos, ventana):
    """
    Cuenta los hits ocurridos en cada bloque de tiempo de duración fija.

    Divide la serie temporal en bloques de tamaño igual a ventana (en segundos)
    y cuenta cuántos hits ocurren dentro de cada bloque.

    Parámetros:
        datos (dict): diccionario de un participante con las claves "hit" 
                      y "tiempo", ambas listas del mismo largo.
        ventana (float): duración en segundos de cada bloque de tiempo.

    Retorna:
        list: lista de enteros, donde cada elemento representa 
              la cantidad de hits en ese bloque de tiempo.
    """
    bloques = []
    tiempo  = datos["tiempo"]
    hits    = datos["hit"]
    tiempo_inicio = tiempo[0]
    hits_bloque   = 0
    for i in range(len(tiempo)):
        if tiempo[i] - tiempo_inicio < ventana:
            if hits[i] == True:
                hits_bloque = hits_bloque + 1
        else:
            bloques.append(hits_bloque)
            tiempo_inicio = tiempo[i]
            hits_bloque   = 1 if hits[i] == True else 0
    bloques.append(hits_bloque)  # agrega el último bloque
    return bloques