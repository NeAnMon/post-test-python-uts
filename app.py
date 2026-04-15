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
