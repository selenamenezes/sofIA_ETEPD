import streamlit as st
import time
from controller.clientes_controller import cadastro_cliente

def cadastro_view():
    # so renderiza se a tela ativa for cadastro
    if st.session_state.get("tela") != "cadastro":
        return

    st.title("🥷 SofIA >> Cadastre-se")

    nome = st.text_input("Nome", key="cad_nome")
    email = st.text_input("E-mail", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")
    confirm_senha = st.text_input("Confirme sua senha", type="password", key="cad_confirm_senha")

    if st.button("Cadastrar", key="btn_cadastrar"):
        status, msg = cadastro_cliente(nome, email, senha, confirm_senha)

        if status:
            st.success(msg)
        else:
            st.error(msg)

    if st.button("Já tenho login", key="btn_ir_login"):
        st.session_state["tela"] = "login"
