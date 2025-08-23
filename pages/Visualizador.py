import streamlit as st

st.set_page_config(page_title="Visualizador de Senhas", page_icon=":mag:", layout="wide")

registros = []

register = {
    "Site": "",
    "Username": "",
    "Senha": ""
}

st.header("Armazenamento de Senhas")
st.write("Armazene suas senhas com segurança.")

register["Site"] = st.text_input("Digite o nome do site:")
register["Username"] = st.text_input("Digite o nome/email do usuário:")
register["Senha"] = st.text_input("Digite a senha:", type="password")

if st.button("Salvar"):
    registros.append(register.copy())
    st.success("Registro salvo com sucesso!")


st.dataframe(registros)