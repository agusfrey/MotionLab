from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit


# 1 cargar datos desde el archivo
try:
    datos = cargar_datos(datos/datos.csv)
except ValueError as e:
    print(f"Tipo de error: {e}")
else:
    # 2. validar datos
    try:
        datos_validos = []
        for registro in datos:
            validar_registro(registro)
            datos_validos.append(registro)
    except ValueError as e:
        print(f"Tipo de error: {e}")
    else:
        # 3 seleccionar participante
        seleccionados = None
        while seleccionados is None:
            try:
                opcion = input("Ingrese el ID del participante o 'todos': ")
                if opcion == "todos":
                    seleccionados = datos_validos
                else:
                    id_buscado   = int(opcion)
                    participante = filtrar_por_participante(datos_validos, id_buscado)
                    if participante is None:
                        raise ValueError(f"No se encontró el participante con ID {id_buscado}")
                    seleccionados = [participante]
            except ValueError as e:
                print(f"Tipo de error: {e}")

        # 4 calcular métricas y mostrar resultados
        for registro in seleccionados:
            id_p       = registro["id_participante"]
            condicion  = registro["condicion"][0]
            hits       = calcular_hits_totales(registro)
            primer_hit = calcular_tiempo_primer_hit(registro)
            print(f"\nParticipante {id_p} | Condición: {condicion}")
            print(f"  Hits totales:      {hits}")
            print(f"  Tiempo primer hit: {primer_hit} seg")
