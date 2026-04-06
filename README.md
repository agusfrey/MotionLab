# Agustin Frey, Santiago Devoto y Wenceslao Grosse Garros. 

Proyecto para analizar cómo se mueve la gente cuando tiene que tocar una
zona objetivo lo más rápido posible. Lo hacemos bajo dos condiciones:
compitiendo o cooperando, y vemos si eso cambia cuántos hits meten.

El sistema tiene 4 archivos con 7 funciones en total:
- `carga_datos.py` = carga y parsea el archivo CSV
- `validacion_datos.py` = valida que los datos estén bien
- `procesamiento_datos.py` = filtra los datos por participante
- `metricas.py` = calcula hits totales, tiempo del primer hit y hits por bloques
