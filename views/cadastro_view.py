import streamlit as st
from controller.clientes_controller import cadastro_cliente

def cadastro_view():
    if st.session_state.get("tela") != "cadastro":
        return

    st.title("🥷 SofIA >> Cadastre-se")

    with st.form("form_cadastro"):
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        confirm_senha = st.text_input("Confirme sua senha", type="password")

        submit = st.form_submit_button("Cadastrar")
    
    if submit:
        status, msg = cadastro_cliente(nome, email, senha, confirm_senha)
        if status:
            st.success(msg)
        else:
            st.error(msg)
