import streamlit as st
import sys
from io import StringIO

# 1. Configuración inicial de la página
st.set_page_config(page_title="Certificación Práctica - Nexan", page_icon="💻")

# 2. Inicializar el sistema de puntos en el estado de la sesión
if 'puntos_reto1' not in st.session_state:
    st.session_state.puntos_reto1 = 0.0
if 'puntos_reto2' not in st.session_state:
    st.session_state.puntos_reto2 = 0.0

st.title("🏆 Evaluación de Desempeño Práctico")
st.markdown("---")

# --- RETO 1: ANÁLISIS DE INFRAESTRUCTURA ---
st.header("🚀 Reto 1: Filtro de Alerta (Valor: 2.5)")
st.write("Misión: Imprime los nombres de los servidores con Temperatura > 75 o Carga > 90.")

code_1 = st.text_area("Editor de Código - Reto 1:", value="""servidores = [
    [101, "DB-Principal", 78, 85],
    [102, "Web-Mirror", 60, 95],
    [103, "Backup-SRV", 65, 40]
]
# Escribe tu lógica aquí:
""", height=200, key="editor1")

if st.button("Validar Reto 1"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(code_1)
        sys.stdout = sys.__stdout__
        res = output.getvalue()
        if "DB-Principal" in res and "Web-Mirror" in res:
            st.session_state.puntos_reto1 = 2.5
            st.success("✅ Reto 1 superado. Puntos obtenidos: 2.5")
        else:
            st.session_state.puntos_reto1 = 0.0
            st.error("❌ El resultado no es correcto. Revisa la lógica.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

st.markdown("---")

# --- RETO 2: LIQUIDADOR DE NÓMINA ---
st.header("🏆 Reto 2: Sistema de Comisiones (Valor: 2.5)")
st.write("Misión: Calcula comisiones (A: 15%, B: 5%) e imprime A: [valor] y B: [valor].")

code_2 = st.text_area("Editor de Código - Reto 2:", value="""datos = [["A", 1000000], ["B", 500000]]
# Escribe tu lógica aquí:
""", height=250, key="editor2")

if st.button("Validar Reto Final"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(code_2)
        sys.stdout = sys.__stdout__
        res = output.getvalue()
        if "A: 150000.0" in res and "B: 25000.0" in res:
            st.session_state.puntos_reto2 = 2.5
            st.success("✅ Reto 2 superado. Puntos obtenidos: 2.5")
            st.balloons()
        else:
            st.session_state.puntos_reto2 = 0.0
            st.error("❌ Los totales no coinciden. Revisa los cálculos.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# --- SECCIÓN DE RESULTADO TOTAL ---
st.markdown("---")
st.header("📊 Resultado Final de la Prueba Práctica")

# Calcular el total
total_practica = st.session_state.puntos_reto1 + st.session_state.puntos_reto2

# Mostrar el puntaje con un diseño llamativo
st.metric(label="Puntaje Total Práctico", value=f"{total_practica} / 5.0")

if total_practica >= 3.0:
    st.success("🎉 ¡Felicidades! Has aprobado la sección práctica.")
else:
    st.warning("Te recomendamos revisar los temas de ciclos y matrices antes de intentar nuevamente.")

st.info("💡 Ingeniero: Toma una captura de pantalla de este resultado para reportar tu nota final.")
