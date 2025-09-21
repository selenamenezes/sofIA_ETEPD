import streamlit as st
from views.cadastro_view import cadastro_view
from views.login_view import login_view
from views.dashboard_view import dash_view 
from controller.produtos_controller import listar_produtos, adicionar_produtos, remover_produtos, alterar_produtos
from database.db import init_db
from views import documentos_view, sofia 

def main():
    if "tela" not in st.session_state:
        st.session_state["tela"] = "cadastro"
    if "logado" not in st.session_state:
        st.session_state["logado"] = False

    if st.session_state["logado"]:
        st.title("🥷 SofIA")

        menu = st.sidebar.radio(
            "📌 Menu",
            ["SofIA", "Dashboard", "Adicionar Produto", "Editar Produto", "Listar Produtos", "Remover Produto", "Documentos"]
        )

        if menu == "Dashboard":
            st.title("Dashboard")
            dash_view()
        
        elif menu == "Adicionar Produto":
            st.subheader("Adicionar Produto")

            categorias = [
                "Vinho", "Refrigerante", "Suco", "Cerveja", "Destilado",
                "Energético", "Gelo", "Água", "Sem Álcool", "Isotônico", 
                "Cigarro", "Sem Categoria"
            ]

            with st.form("form_adicionar_produto", clear_on_submit=True):
                cod_barras = st.text_input("Código de Barras")
                produto = st.text_input("Nome do Produto")
                preco_unit = st.number_input("Preço", min_value=0.0, format="%.2f")
                quantidade = st.number_input("Quantidade", min_value=0, step=1)
                categoria = st.selectbox("Categoria", categorias)
                marca = st.text_input("Marca")
                
                submitted = st.form_submit_button("Adicionar Produto")
                if submitted:
                    sucesso, msg = adicionar_produtos(cod_barras, produto, preco_unit, quantidade, categoria, marca)
                    if sucesso:
                        st.success(msg)
                    else:
                        st.error(msg)

        elif menu == "Editar Produto":
            st.subheader("Editar Produto")

            categorias = [
                "Vinho", "Refrigerante", "Suco", "Cerveja", "Destilado",
                "Energético", "Gelo", "Água", "Sem Álcool", "Isotônico",
                "Cigarro", "Sem Categoria"
            ]

            with st.form("form_editar_produto", clear_on_submit=True):
                cod_barras = st.text_input("Código de Barras do Produto a Alterar")
                n_produto = st.text_input("Novo Nome do Produto")
                n_preco = st.number_input("Novo Preço Unitário", min_value=0.0, format="%.2f")
                n_quantidade = st.number_input("Nova Quantidade", min_value=0, step=1)
                n_categoria = st.selectbox("Nova Categoria", categorias)
                n_marca = st.text_input("Nova Marca")
                
                submitted = st.form_submit_button("Alterar Produto")
                if submitted:
                    sucesso, msg = alterar_produtos(cod_barras, n_produto, n_preco, n_quantidade, n_categoria, n_marca)
                    if sucesso:
                        st.success(msg)
                    else:
                        st.error(msg)


        elif menu == "Remover Produto":
            st.subheader("Remover Produto")

            with st.form("form_remover_produto", clear_on_submit=True):
                cod_barras = st.text_input("Código de Barras do Produto a Remover")
                
                submitted = st.form_submit_button("Remover Produto")
                if submitted:
                    sucesso, msg = remover_produtos(cod_barras)
                    if sucesso:
                        st.success(msg)
                    else:
                        st.error(msg)

        elif menu == "Listar Produtos":
            st.subheader("Painel de Produtos")
            status, tabela = listar_produtos()
            if status:
                st.dataframe(tabela)
            else:
                st.info("Ainda não há produtos cadastrados.")

        elif menu == "Documentos":
            documentos_view.show()

        elif menu == "SofIA":
            sofia.show()
            

    else:
        if st.session_state["tela"] == "cadastro":
            cadastro_view()
        elif st.session_state["tela"] == "login":
            login_view()

if __name__ == "__main__":
    init_db()
    main()
    