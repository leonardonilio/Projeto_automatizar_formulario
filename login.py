import streamlit as st
import time

st.set_page_config(page_title="Login", page_icon="🔒", layout="centered")#Configuração da pagina
# Ocultar sidebar
hide_pages_style = """
<style>
/* Oculta o menu lateral inteiro */
section[data-testid="stSidebar"] {
    display: none;
}
</style>
"""
st.markdown(hide_pages_style, unsafe_allow_html=True)
# estilo
st.markdown("""
<style>
    .big-title {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: -10px;
    }
    .sub {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)
# Conteúdo da página
st.markdown('<p class="big-title">Sistema de cadastro de formulario</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Faça seu login para continuar</p>', unsafe_allow_html=True)
# Campos
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

# Botão
if st.button("Entrar"):
    if email and senha:
        st.success("Login efetuado")
        st.switch_page("pages/formulario.py")
    else:
        st.error("Informe nos campos obritório")

