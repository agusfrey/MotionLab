
import os
import matplotlib.pyplot as plt
from src.carga_datos import cargar_datos
from src.validacion_datos import validar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit

ruta = "datos/MotionLab_mock_data.csv"

# crear carpeta graficos si no existe
if not os.path.exists("graficos"):
    os.mkdir("graficos")

# 1. cargar datos
try:
    df = cargar_datos(ruta)
except (FileNotFoundError, ValueError) as e:
    print(f"Tipo de error: {e}")
else:
    # 2. validar datos
    try:
        validar_datos(df)
    except ValueError as e:
        print(f"Tipo de error: {e}")
    else:
        # 3. seleccionar participante
        seleccionados = None
        while seleccionados is None:
            try:
                opcion = input("Ingrese el ID del participante o 'todos': ")
                if opcion == "todos":
                    seleccionados = df
                else:
                    id_buscado   = int(opcion)
                    participante = filtrar_por_participante(df, id_buscado)
                    if participante is None:
                        raise ValueError(f"No se encontró el participante con ID {id_buscado}")
                    seleccionados = participante
            except ValueError as e:
                print(f"Tipo de error: {e}")

        # 4. calcular métricas y mostrar resultados
        for id_p, df_p in seleccionados.groupby("id_participante"):
            condicion  = df_p["condicion"].iloc[0]
            hits       = calcular_hits_totales(df_p)
            primer_hit = calcular_tiempo_primer_hit(df_p)
            print(f"\nParticipante {id_p} | Condición: {condicion}")
            print(f"  Hits totales:      {hits}")
            print(f"  Tiempo primer hit: {primer_hit} seg")

        # 5. graficos
        # grafico de barras: hits por condicion
        hits_por_condicion = df.groupby("condicion")["hit"].sum()
        plt.figure(figsize=(9, 5))
        hits_por_condicion.plot(kind="bar", color="#1e3a8a", edgecolor="black", alpha=0.8)
        plt.title("Hits totales por condición", fontsize=13, fontweight="bold", pad=15)
        plt.xlabel("Condición", fontsize=11)
        plt.ylabel("Cantidad de hits", fontsize=11)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle="--", alpha=0.5, axis="y")
        plt.tight_layout()
        plt.savefig("graficos/hits_por_condicion.png", dpi=300)
        plt.close()

        # grafico de lineas: posicion x a lo largo del tiempo
        plt.figure(figsize=(11, 5))
        df.plot(kind="line", x="tiempo", y="x", color="#b45309", linewidth=1.5, ax=plt.gca())
        plt.title("Posición X a lo largo del tiempo", fontsize=13, fontweight="bold", pad=15)
        plt.xlabel("Tiempo (segundos)", fontsize=11)
        plt.ylabel("Posición X", fontsize=11)
        plt.grid(True, linestyle=":", alpha=0.6)
        plt.tight_layout()
        plt.savefig("graficos/posicion_x_temporal.png", dpi=300)
        plt.close()

        print("\nGráficos guardados en la carpeta graficos/")
