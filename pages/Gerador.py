import streamlit as st
import random

st.set_page_config(page_title="Gerador de Senhas", page_icon=":key:", layout="wide")

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '&', '*', '?']


st.header("Gerador de Senhas")
st.write("Este aplicativo gera senhas seguras com baseado em uma lista de caracteres.")

length = st.number_input("Digite o comprimento desejado da senha:", min_value=1, max_value=100, value=16, step=1)
col1, col2, col3 = st.columns([3, 4, 0.83])
with col3:
    st.button("Gerar")


def generate_password(length):
    password = ''
    for i in range(length):
        password += random.choice(list)
    return password

with col1:
    st.write(":red[Senha Gerada:]", generate_password(length))
