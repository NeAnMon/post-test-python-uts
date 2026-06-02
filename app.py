import streamlit as st
import sys
from io import StringIO

# 1. Configuración inicial de la página
st.set_page_config(page_title="Certificación Práctica - Nexan", page_icon="💻")

# 2. Inicializar el sistema de puntos en el estado de la sesión (Persistencia)
if 'puntos_reto1' not in st.session_state:
    st.session_state.puntos_reto1 = 0.0
if 'puntos_reto2' not in st.session_state:
    st.session_state.puntos_reto2 = 0.0

st.title("🏆 Evaluación de Desempeño Práctico")
st.markdown("---")

# ==========================================
# --- RETO 1: ANÁLISIS DE INFRAESTRUCTURA ---
# ==========================================
st.header("🚀 Reto 1: Filtro de Alerta (Valor: 2.5)")

# 💡 bloque Explicativo Pedagógico
st.info("""
**Guía de Resolución - Pensamiento Computacional:**
Para resolver este reto debes aplicar la **Descomposición**. Sigue estos pasos lógicos:
1. **Iterar:** Recorre la matriz `servidores` usando un bucle `for`.
2. **Evaluar:** Dentro del bucle, extrae los valores de Temperatura (índice 2) y Carga (índice 3).
3. **Condición:** Usa una estructura condicional `if` acompañada del operador lógico `or` para evaluar si se cumple alguna de las dos alertas.
4. **Salida:** Imprime el nombre del servidor (índice 1) si la condición es verdadera.
""")

with st.expander("📝 Ver Ejemplo de Estructura Lógica para el Reto 1"):
    st.code("""
# Ejemplo guía (No es la solución exacta, adáptalo a tus datos):
for elemento in lista:
    nombre = elemento[1]
    valor1 = elemento[2]
    valor2 = elemento[3]
    if valor1 > LIMITE1 or valor2 > LIMITE2:
        print(nombre)
    """, language="python")

st.write("**Misión:** Imprime los nombres de los servidores con **Temperatura > 75** o **Carga > 90**.")

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
            st.error("❌ El resultado no es correcto. Asegúrate de usar 'or' y de imprimir los nombres.")
            st.write("**Tu salida fue:**", res)
    except Exception as e:
        sys.stdout = sys.__stdout__
        st.error(f"⚠️ Error en el código: {e}")

st.markdown("---")

# ==========================================
# --- RETO 2: LIQUIDADOR DE NÓMINA ---
# ==========================================
st.header("🏆 Reto 2: Sistema de Comisiones (Valor: 2.5)")

# 💡 bloque Explicativo Pedagógico
st.info("""
**Guía de Resolución - Pensamiento Computacional:**
Este reto requiere **Reconocimiento de Patrones** y **Acumulación de Datos**. Sigue este orden de subtareas:
1. **Inicializar:** Crea dos variables acumuladoras en cero (ej. `total_A = 0` y `total_B = 0`) **antes** del bucle.
2. **Filtrar:** Recorre la matriz `datos` con un bucle `for` y extrae el tipo de zona (índice 0) y el monto de venta (índice 1).
3. **Calcular:** Usa un condicional `if-elif`. Si la zona es "A", calcula el 15% (`monto * 0.15`) y súmalo a su acumulador. Si es "B", calcula el 5% (`monto * 0.05`) y súmalo al suyo.
4. **Imprimir:** Al salir del bucle, imprime los totales usando el formato exacto requerido: `print(f"A: {total_A}")` y `print(f"B: {total_B}")`.
""")

with st.expander("📝 Ver Ejemplo de Estructura Lógica para el Reto 2"):
    st.code("""
# Ejemplo guía (No es la solución exacta, adáptalo a tus datos):
acumulador_A = 0
acumulador_B = 0

for zona, valor in datos:
    if zona == "A":
        acumulador_A += valor * PORCENTAJE_A
    elif zona == "B":
        acumulador_B += valor * PORCENTAJE_B

print("A:", acumulador_A)
print("B:", acumulador_B)
    """, language="python")

st.write("**Misión:** Calcula comisiones (**A: 15%**, **B: 5%**) sobre la matriz `datos` e imprime `A: [valor]` y `B: [valor]`.")

code_2 = st.text_area("Editor de Código - Reto 2:", value="""datos = [
    ["A", 1000000], 
    ["B", 500000],
    ["A", 2000000],
    ["B", 800000]
]
# Escribe tu lógica aquí:
""", height=250, key="editor2")

if st.button("Validar Reto Final"):
    output = StringIO()
    sys.stdout = output
    try:
        exec(code_2)
        sys.stdout = sys.__stdout__
        res = output.getvalue()
        
        if "450000" in res and "65000" in res:
            st.session_state.puntos_reto2 = 2.5
            st.success("⭐ ¡RETO 2 COMPLETADO! Puntos obtenidos: 2.5")
            st.balloons()
        else:
            st.session_state.puntos_reto2 = 0.0
            st.error("❌ Los totales no coinciden. Revisa los porcentajes (0.15 y 0.05) y los acumuladores.")
            st.write("**Tu salida fue:**", res)
    except Exception as e:
        sys.stdout = sys.__stdout__
        st.error(f"⚠️ Error en el código: {e}")

# ==========================================
# --- SECCIÓN DE RESULTADO TOTAL ---
# ==========================================
st.markdown("---")
st.header("📊 Resultado Final de la Prueba Práctica")

total_practica = st.session_state.puntos_reto1 + st.session_state.puntos_reto2

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Nota Final Acumulada", value=f"{total_practica} / 5.0")

with col2:
    if total_practica >= 3.0:
        st.success("🎉 ESTADO: APROBADO")
    else:
        st.error("❌ ESTADO: REPROBADO")

st.info("💡 **Ingeniero:** Copia este puntaje total y repórtalo en la plataforma de IA Studio para promediar tu nota final con la teoría.")
st.caption("Desarrollado para el Proyecto de Fortalecimiento en Pensamiento Computacional | UTS - UDI")
