import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.validacion_datos import validar_datos
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit
from src.graficos import grafico_sensacion_por_wing, grafico_viento_vs_sensacion

st.title("MotionLab Dashboard")
st.write("Sistema de análisis de datos de tarea motora")

# 1. CARGA DINÁMICA DE DATOS
archivo = st.file_uploader("Subí el archivo CSV de datos", type="csv")

if archivo is not None:

    df = pd.read_csv(archivo)

    # 2. VALIDACIÓN DEFENSIVA
    try:
        validar_datos(df)
    except ValueError as e:
        st.error(f"Error crítico en los datos: {e}")
        st.stop()

    st.success("Datos cargados y validados correctamente")

    # 3. KPIs
    total_hits        = df["hit"].sum()
    total_participantes = df["id_participante"].nunique()
    total_registros   = len(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de hits", total_hits)
    col2.metric("Participantes", total_participantes)
    col3.metric("Registros totales", total_registros)

    # KPIs por condición
    st.subheader("Hits por condición")
    hits_competencia = df[df["condicion"] == "competencia"]["hit"].sum()
    hits_cooperacion = df[df["condicion"] == "cooperacion"]["hit"].sum()
    col4, col5 = st.columns(2)
    col4.metric("Hits en competencia", hits_competencia)
    col5.metric("Hits en cooperación", hits_cooperacion)

    # 4. VISUALIZACIONES
    st.subheader("Hits totales por condición")
    hits_por_condicion = df.groupby("condicion")["hit"].sum()
    fig1, ax1 = plt.subplots(figsize=(9, 5))
    hits_por_condicion.plot(kind="bar", color="#1e3a8a", edgecolor="black", alpha=0.8, ax=ax1)
    ax1.set_title("Hits totales por condición", fontsize=13, fontweight="bold")
    ax1.set_xlabel("Condición", fontsize=11)
    ax1.set_ylabel("Cantidad de hits", fontsize=11)
    ax1.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()
    st.pyplot(fig1)

    st.subheader("Posición X a lo largo del tiempo")
    fig2, ax2 = plt.subplots(figsize=(11, 5))
    df.plot(kind="line", x="tiempo", y="x", color="#b45309", linewidth=1.5, ax=ax2)
    ax2.set_title("Posición X a lo largo del tiempo", fontsize=13, fontweight="bold")
    ax2.set_xlabel("Tiempo (segundos)", fontsize=11)
    ax2.set_ylabel("Posición X", fontsize=11)
    ax2.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    st.pyplot(fig2)

    # Vista previa de datos
    st.subheader("Vista previa de datos")
    st.dataframe(df.head(10))
