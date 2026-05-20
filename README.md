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

- Se valido que (x) e (y) sean números
- En caso de error, el programa se detiene mostrando el problema
- Se validó que el ID sea entero y mayor a 0
- Se validó que el tiempo sea positivo y creciente
- Se validó que hit sea True o False
- Se validó que condicion sea competencia o cooperacion
- Se validó que el archivo exista y no esté vacío.
- Las funciones detectan errores con raise y el main los maneja con try/except
- En caso de error , el programa se detiene mostrando el problema
- En el main, si el ID ingresado no existe, se muestra un mensaje de error y se vuelve a pedir

#  Objetos
Si el sistema se modelara con objetos, se definirían las siguientes clases:

Clase Participante 
- Atributos: id_participante, tiempo, x, y, hit, condicion
- Métodos: calcular_hits_totales(), calcular_tiempo_primer_hit()

Clase MotionLab**
- Atributos: participantes (lista de objetos Participante)
- Métodos: cargar_datos(), validar_registro(), filtrar_por_participante()

## Implementación con Pandas

Si se utilizara la librería Pandas para la lectura del dataset, se importaría de la siguiente forma:

import pandas as pd
df = pd.read_csv("datos/MotionLab_mock_data.csv")

La función que se debería modificar es cargar_datos() en carga_datos.py, ya que actualmente abre y recorre el archivo línea por línea con open(). Con Pandas, el archivo se cargaría directamente en un DataFrame con pd.read_csv(), simplificando la lectura y conversión de tipos de datos.

Además, parsear_linea() podría eliminarse ya que Pandas convierte automáticamente los tipos de datos al leer el archivo.

#USO IA
Se uso Chatgpt para identificar mejor los errores y no equivocarse acoplando todo.

