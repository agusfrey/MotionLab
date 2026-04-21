def parsear_linea(linea):
    """
    Parsea una línea del archivo CSV y devuelve sus valores convertidos al tipo correspondiente.

    Parámetros:
        linea (str): línea del archivo CSV con los campos separados por comas.

    Retorna:
        list: lista con los valores [id_participante, tiempo, x, y, hit, condicion]
              donde id_participante es int, tiempo/x/y son float, hit es bool y condicion es str.

    Raises:
        ValueError: si algún campo no tiene el tipo o valor correcto.
    """
    if linea.strip() == "":
        raise ValueError("La línea está vacía")

    campos = linea.strip().split(",")

    if len(campos) != 6:
        raise ValueError(f"La línea debe tener 6 campos, tiene {len(campos)}")

    try:
        id_participante = int(campos[0])
    except ValueError:
        raise ValueError("id_participante debe ser un entero")

    if id_participante <= 0:
        raise ValueError("id_participante debe ser mayor a 0")

    try:
        tiempo = float(campos[1])
    except ValueError:
        raise ValueError("tiempo debe ser un número")

    if tiempo < 0:
        raise ValueError("tiempo no puede ser negativo")

    try:
        x = float(campos[2])
    except ValueError:
        raise ValueError("x debe ser un número")

    try:
        y = float(campos[3])
    except ValueError:
        raise ValueError("y debe ser un número")

    hit_str = campos[4].strip()
    if hit_str not in ["True", "False"]:
        raise ValueError(f"hit debe ser True o False, se recibió '{hit_str}'")
    hit = hit_str == "True"

    condicion = campos[5].strip()
    if condicion not in ["competencia", "cooperacion"]:
        raise ValueError(f"condicion inválida: '{condicion}'. Debe ser 'competencia' o 'cooperacion'")

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
       Lanza:
            ValueError: si alguna línea tiene datos inválidos, propagado desde parsear_linea.
            FileNotFoundError: si el archivo no existe en la ruta indicada.

    """
   try:
        archivo = open(ruta, "r")
    except FileNotFoundError:
        raise ValueError(f"No se encontró el archivo en la ruta '{ruta}'")

    encabezado = archivo.readline()
    if encabezado.strip() == "":
        raise ValueError("El archivo está vacío")
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
           


