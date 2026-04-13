#INTEGRANTES
Agustin Frey, Santiago Devoto y Wenceslao Grosse Garros. 
#MOTIONLAB
Proyecto para analizar cómo se mueve la gente cuando tiene que tocar una
zona objetivo lo más rápido posible. Lo hacemos bajo dos condiciones:
compitiendo o cooperando, y vemos si eso cambia cuántos hits meten.

El sistema tiene 4 archivos con 7 funciones en total:
- `carga_datos` = carga y parsea el archivo CSV
- `validacion_datos` = valida que los datos estén bien
- `procesamiento_datos` = filtra los datos por participante
- `metricas` = calcula hits totales, tiempo del primer hit y hits por bloques

#Errores y Validaciones

- Se validó que el ID sea entero
- Se valido que el tiempo sea positivo
- Se valido que (x) e (y) sean números
- Se utilizo try-except para que salten errores
- En caso de error, el programa se detiene mostrando el problema

#USO IA
Se uso Chatgpt para identificar mejor los errores y no equivocarse acoplando todo.

