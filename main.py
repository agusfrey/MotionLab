from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit


# 1. cargar datos desde el archivo
try:
    datos = cargar_datos("datos/datos.csv")
    if len(datos) == 0:
        raise ValueError('No se pueden cargar los datos del archivo')
except ValueError as e:
    print("Error":e)


# 2. filtrar datos válidos
try: 
    datos_validos = []

    for registro in datos:
    if validar_registro(registro):
        datos_validos.append(registro)
    if len(datos_validos) == 0:
         raise ValueError("no pasó la validación")
except ValueError as e:
    print("Error:" e")


try:
    id_buscado   = int(input("Ingrese el ID del participante: "))
    participante = filtrar_por_participante(datos_validos, id_buscado)
    if participante is None:
        raise ValueError('No se encontró el participante con ID')
except ValueError as e:
    print("Error:" e)

# 3. calcular métricas y mostrar resultados
for registro in datos_validos:
    id_p       = registro["id_participante"]
    condicion  = registro["condicion"][0]
    hits       = calcular_hits_totales(registro)
    primer_hit = calcular_tiempo_primer_hit(registro)

    print(f"Participante {id_p} | Condición: {condicion}")
    print(f"  Hits totales:      {hits}")
    print(f"  Tiempo primer hit: {primer_hit} seg")

datos = cargar_datos(ruta)

if datos is None:
    print("El programa se detuvo por errores.")
else:
    print("Hits:", calcular_hits_totales(datos))
