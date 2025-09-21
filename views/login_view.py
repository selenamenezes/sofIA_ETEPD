import streamlit as st
from controller.clientes_controller import login_cliente

def login_view():
    # so mostra a view se st.session_state["tela"] for login
    if st.session_state.get("tela") != "login":
        return

    st.title("🥷 SofIA >> Login")

    log_email = st.text_input("E-mail", key="login_email")
    log_senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Logar", key="btn_logar"):
        status, msg = login_cliente(log_email, log_senha)

        if status:
            st.success(msg)
            # marca como logado e main.py vai renderizar o painel automaticamente
            st.session_state["logado"] = True
        else:
            st.error(msg)

    if st.button("Voltar para cadastro", key="btn_ir_cadastro"):
        st.session_state["tela"] = "cadastro"
