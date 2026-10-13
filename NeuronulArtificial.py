import streamlit as st
import math

st.title("Neuronul Artificial")

numar_intrari = st.number_input("Numarul de intrari:", min_value=1, step=1)

intrari_valori = []
intrari_tarieSin = []
for i in range(numar_intrari):
    st.write(f"Intrarea {i + 1}:")

    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input(f"Valoarea intrarii {i + 1}:", key=f"valoare_{i}")
        intrari_valori.append(x)

    with col2:
        w = st.number_input(f"Valoarea tariei sinaptice {i + 1}:", key=f"tarie_{i}")
        intrari_tarieSin.append(w)

    st.divider()


operatie = st.selectbox("Selecteaza operatia:", ["Suma", "Prod", "Min", "Max"])

stare_iesire = st.selectbox("Selecteaza starea iesirii:", ["Binar", "Real"])

functie_activare = st.selectbox("Selecteaza functia de activare:", ["Liniara", "Sigmoidala", "Semn", "Tanh", "Treapta"])

teta = st.number_input("Valoarea pragului:", value=0.0)


if functie_activare in ["Liniara", "Sigmoidala", "Tanh"]:
    g = st.number_input("Valoarea constantei g:", value=1.0)

if st.button("Calculeaza GIN"):
    termeni = []

    for i in range(numar_intrari):
        termeni.append(intrari_valori[i] * intrari_tarieSin[i])

    if operatie == "Suma":
        GIN = sum(termeni)
    elif operatie == "Prod":
        GIN = math.prod(termeni)
    elif operatie == "Min":
        GIN = min(termeni)
    elif operatie == "Max":
        GIN = max(termeni)

    st.write(f"Rezultatul GIN este: {GIN}")

    if functie_activare == "Treapta":
        if GIN >= teta:
            iesire = 1
        else:
            iesire = 0
    elif functie_activare == "Semn":
        if GIN >= teta:
            iesire = 1
        else:
            iesire = -1
    elif functie_activare == "Liniara":
        iesire = g * (GIN - teta)
    elif functie_activare == "Sigmoidala":
        iesire = 1 / (1 + math.exp(-g * (GIN - teta))) 
    elif functie_activare == "Tanh":
        iesire = math.tanh(g * (GIN - teta))

    
    if stare_iesire == "Binar":
        if iesire >= 0.5:
            iesire = 1
        else:
            iesire = 0

    
    st.write(f"Rezultatul iesirii este: {iesire}")