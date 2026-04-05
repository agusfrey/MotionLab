from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit

# 1. cargar datos desde el archivo
datos = cargar_datos("datos/datos.csv")

# 2. filtrar datos válidos
datos_validos = []

for registro in datos:
    if validar_registro(registro):
        datos_validos.append(registro)

# 3. calcular métricas y mostrar resultados
for registro in datos_validos:
    id_p       = registro["id_participante"]
    condicion  = registro["condicion"][0]
    hits       = calcular_hits_totales(registro)
    primer_hit = calcular_tiempo_primer_hit(registro)

    print(f"Participante {id_p} | Condición: {condicion}")
    print(f"  Hits totales:      {hits}")
    print(f"  Tiempo primer hit: {primer_hit} seg")
