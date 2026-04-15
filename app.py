import streamlit as st
import sys
from io import StringIO

# Configuración de la página
st.set_page_config(page_title="Certificación Final Python - UTS", page_icon="🎓", layout="wide")

# Estilos personalizados (Toque Nexan)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 Evaluación Final de Certificación: Pensamiento Computacional")
st.write(f"**Docente:** Nelber Andreiv Montaguth Useche | **Institución:** UTS")

# --- SECCIÓN 1: REPASO RÁPIDO Y TEORÍA ---
with st.expander("📚 Haz clic aquí para repasar los conceptos clave antes de iniciar"):
    st.markdown("""
    ### 🏗️ Recordatorio de Ingeniería:
    * **Variables:** Cajas donde guardamos datos (`int`, `float`, `str`).
    * **Condicionales:** El `if` evalúa verdades para tomar decisiones.
    * **Bucles:** El `for` cuenta, el `while` espera una condición.
    * **Matrices:** Tablas de datos organizadas por `[fila][columna]`.
    """)

# --- SECCIÓN 2: RETOS PRÁCTICOS (Interacción Directa) ---
st.header("🛠️ Fase 1: Desafíos de Código en Vivo")
st.info("Completa el código y presiona 'Validar' para avanzar.")

# Reto de Matrices y Acumuladores
st.subheader("Reto: El Liquidador Nexan")
st.write("Calcula la comisión del 15% para el servicio de mayor valor en la matriz.")

codigo_estudiante = st.text_area("Escribe tu código aquí:", value="""servicios = [["Mantenimiento", 50000], ["Redes", 200000]]
# Tu misión: Calcular el 15% del segundo servicio
total = servicios[1][1] * 0.15
print(f"COMISION:{total}")""", height=150)

if st.button("Validar Reto Práctico"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(codigo_estudiante)
        sys.stdout = sys.__stdout__
        if "COMISION:30000.0" in output.getvalue():
            st.success("✅ ¡Excelente! Has dominado la extracción de datos y el cálculo porcentual.")
            st.balloons()
        else:
            st.error("❌ El resultado no es correcto. Revisa el índice de la matriz o el cálculo.")
    except Exception as e:
        st.error(f"⚠️ Error en el código: {e}")

st.divider()

# --- SECCIÓN 3: CUESTIONARIO DE SELECCIÓN (Post-Test) ---
st.header("📝 Fase 2: Examen de Conocimientos")

with st.form("quiz_final"):
    p1 = st.radio("1. En la empresa Nexan, ¿qué tipo de dato usarías para el stock (unidades enteras)?", ["Float", "String", "Int"])
    
    p2 = st.radio("2. ¿Qué instrucción permite romper un bucle infinito de forma segura?", ["continue", "break", "if"])
    
    p3 = st.radio("3. Si una matriz es de 3x3, ¿cuál es el índice de la última celda?", ["[3][3]", "[2][2]", "[0][0]"])
    
    submitted = st.form_submit_button("Finalizar y Enviar Evaluación")
    
    if submitted:
        puntos = 0
        if p1 == "Int": puntos += 1
        if p2 == "break": puntos += 1
        if p3 == "[2][2]": puntos += 1
        
        st.subheader(f"Tu puntaje final es: {puntos}/3")
        if puntos == 3:
            st.success("⭐ ¡Nivel Ingeniero Senior alcanzado!")
        else:
            st.warning("Te recomendamos repasar los conceptos de índices y bucles.")

# Pie de página
st.markdown("---")
st.caption("Recurso Digital diseñado para el fortalecimiento del Pensamiento Computacional - Proyecto de Maestría UDI.")