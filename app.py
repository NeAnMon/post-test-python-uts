import streamlit as st
import sys
from io import StringIO

st.header("🛠️ Fase Práctica: Laboratorios de Desempeño Nexan")
st.info("Instrucciones: Completa los espacios vacíos en el código para resolver los problemas de ingeniería. Al finalizar, presiona el botón de validación.")

# --- RETO 1: FILTRADO DE MATRICES ---
st.subheader("Reto 1: Monitor de Seguridad Crítica")
st.markdown("""
**Escenario:** Debes filtrar una matriz de servidores y mostrar solo aquellos con **Temperatura > 70** y **Carga > 80**.
""")

codigo_reto_1 = st.text_area("Editor de Código - Reto 1:", value="""servidores = [[101, "WEB", 65, 85], [102, "DB", 75, 90], [103, "APP", 80, 82]]

print("Servidores Críticos:")
for s in servidores:
    temp = s[2]
    carga = s[3]
    
    # COMPLETA LA CONDICIÓN LÓGICA AQUÍ:
    if temp > 70 and carga > 80:
        print(f"- {s[1]}")
""", height=200)

if st.button("Validar Reto 1"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(codigo_reto_1)
        sys.stdout = sys.__stdout__
        resultado = output.getvalue()
        if "- DB" in resultado and "- APP" in resultado:
            st.success("✅ ¡Excelente! Filtro lógico aplicado correctamente.")
        else:
            st.error("❌ El filtro no muestra los servidores correctos. Revisa los operadores > y el conector 'and'.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

st.divider()

# --- RETO 2: INTEGRACIÓN TOTAL (ACUMULADORES) ---
st.subheader("Reto 2: Liquidador de Comisiones")
st.markdown("""
**Escenario:** Calcula la comisión total para técnicos categoría 'A' (15%). 
Debes usar un **acumulador** dentro del ciclo.
""")

codigo_reto_2 = st.text_area("Editor de Código - Reto 2:", value="""servicios = [[1, "A", 500000], [2, "B", 200000], [3, "A", 300000]]
total_comision = 0

for reg in servicios:
    cat = reg[1]
    valor = reg[2]
    
    if cat == "A":
        # COMPLETA EL ACUMULADOR (Suma el 15% del valor):
        total_comision += valor * 0.15

print(f"TOTAL: {total_comision}")
""", height=220)

if st.button("Validar Reto Final"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(codigo_reto_2)
        sys.stdout = sys.__stdout__
        resultado = output.getvalue()
        # El resultado esperado es (500000*0.15) + (300000*0.15) = 75000 + 45000 = 120000
        if "TOTAL: 120000.0" in resultado:
            st.success("✅ ¡BRONCE, PLATA Y ORO! Has completado la certificación práctica de Nexan.")
            st.balloons()
        else:
            st.error("❌ El cálculo de la comisión es incorrecto. Revisa la fórmula del acumulador.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
