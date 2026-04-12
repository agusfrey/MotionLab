def parsear_linea(linea):
    """
    Parsea una línea del archivo CSV y devuelve sus valores convertidos al tipo correspondiente.

    Parámetros:
        linea (str): línea del archivo CSV con los campos separados por comas.

    Retorna:
        list: lista con los valores [id_participante, tiempo, x, y, hit, condicion]
              donde id_participante es int, tiempo/x/y son float, hit es bool y condicion es str.
    """
    campos = linea.strip().split(",")
    id_participante = int(campos[0])
    tiempo          = float(campos[1])
    x               = float(campos[2])
    y               = float(campos[3])
    hit             = campos[4].strip() == "true"
    condicion       = campos[5].strip()
    return [id_participante, tiempo, x, y, hit, condicion]


def cargar_datos(ruta):
    """
    Lee un archivo CSV y organiza los datos por participante.

    Abre el archivo indicado, omite el encabezado y recorre cada línea
    aplicando parsear_linea. Agrupa los registros por id_participante,
    acumulando los valores en listas dentro de un diccionario por participante.

    Parámetros:
        ruta (str): ruta al archivo CSV con los datos de la tarea motora.

    Retorna:
        list: lista de diccionarios, uno por participante, con la estructura:
              {
                  "id_participante": int,
                  "tiempo":    [float, ...],
                  "x":         [float, ...],
                  "y":         [float, ...],
                  "hit":       [bool, ...],
                  "condicion": [str, ...]
              }
    """
    datos = []
    archivo = open(ruta, "r")
    archivo.readline()  
    for linea in archivo:
        valores = parsear_linea(linea)
        id_participante = valores[0]
        tiempo          = valores[1]
        x               = valores[2]
        y               = valores[3]
        hit             = valores[4]
        condicion       = valores[5]

      
        registro_existente = None
        for registro in datos:
            if registro["id_participante"] == id_participante:
                registro_existente = registro
                break

        if registro_existente is not None:
            # si ye existe, agrega los valores a sus listas
            registro_existente["tiempo"].append(tiempo)
            registro_existente["x"].append(x)
            registro_existente["y"].append(y)
            registro_existente["hit"].append(hit)
            registro_existente["condicion"].append(condicion)
        else:
            # si no existe, crea un diccionario nuevo
            nuevo_registro = {
                "id_participante": id_participante,
                "tiempo":    [tiempo],
                "x":         [x],
                "y":         [y],
                "hit":       [hit],
                "condicion": [condicion]
            }
            datos.append(nuevo_registro)

    archivo.close()
    return datos


from src.validacion_datos import validar_linea

def cargar_datos(ruta):
    datos = {}

    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()

        for linea in lineas[1:]:
            try:
                id_p, tiempo, x, y, hit, condicion = parsear_linea(linea)

                validar_linea(id_p, tiempo, x, y, hit, condicion)

                if id_p not in datos:
                    datos[id_p] = {
                        "id_participante": id_p,
                        "tiempo": [],
                        "x": [],
                        "y": [],
                        "hit": [],
                        "condicion": []
                    }

                datos[id_p]["tiempo"].append(tiempo)
                datos[id_p]["x"].append(x)
                datos[id_p]["y"].append(y)
                datos[id_p]["hit"].append(hit)
                datos[id_p]["condicion"].append(condicion)

            except Exception as e:
                print("Error en línea:", linea)
                print("Detalle:", e)
                return None  # corta ejecución

        return list(datos.values())

    except FileNotFoundError:
        print("Archivo no encontrado")
        return None
