import streamlit as st
import sys
from io import StringIO

st.subheader("🚀 Reto 1: Filtro de Alerta Temprana")
st.markdown("""
Escribe el código para recorrer la matriz `servidores` e imprimir el nombre de aquellos que cumplan: **Temperatura > 75** O **Carga > 90**.
""")

# Código inicial para el estudiante
code_1 = st.text_area("Editor de Código - Reto 1:", value="""servidores = [
    [101, "DB-Principal", 78, 85],
    [102, "Web-Mirror", 60, 95],
    [103, "Backup-SRV", 65, 40]
]

# Escribe tu ciclo y condicional aquí abajo:
""", height=200)

if st.button("Validar Reto 1"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(code_1)
        sys.stdout = sys.__stdout__
        res = output.getvalue()
        if "DB-Principal" in res and "Web-Mirror" in res:
            st.success("✅ ¡Filtro lógico correcto! Has manejado operadores compuestos.")
        else:
            st.error("❌ El resultado no coincide. Revisa el operador 'or' y los índices.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")


st.subheader("🏆 Reto Final: Sistema Integrado de Comisiones Nexan")
st.markdown("""
**Instrucciones:** Escribe un código completo que:
1. Recorra la matriz `datos`.
2. Identifique si el técnico es **'A'** o **'B'**.
3. Sume la comisión correspondiente en dos variables diferentes (`total_a` y `total_b`).
4. Al final, imprime exactamente: `A: [valor]` y `B: [valor]`.
""")

# Dejamos el área de texto CASI vacía para que él construya todo
code_final = st.text_area("Editor de Código - Reto Final (Escritura Total):", value="""datos = [
    ["A", 1000000],
    ["B", 500000],
    ["A", 2000000],
    ["B", 800000]
]

# Inicializa tus acumuladores:

# Escribe el ciclo for:

# Escribe la lógica condicional y cálculos:

# Imprime los resultados con el formato A: valor y B: valor
""", height=350)

if st.button("Finalizar Certificación"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(code_final)
        sys.stdout = sys.__stdout__
        res = output.getvalue()
        
        # Validación: A=(1M+2M)*0.15 = 450.000 | B=(0.5M+0.8M)*0.05 = 65.000
        if "A: 450000.0" in res and "B: 65000.0" in res:
            st.success("⭐ ¡CERTIFICACIÓN COMPLETA! Has demostrado dominio total de estructuras y lógica.")
            st.balloons()
        else:
            st.warning("⚠️ El código ejecutó, pero los totales no son correctos. Revisa los acumuladores.")
    except Exception as e:
        st.error(f"⚠️ Error Crítico en la estructura: {e}")
