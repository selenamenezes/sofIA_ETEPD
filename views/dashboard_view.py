import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from controller.produtos_controller import listar_produtos

def dash_view():
    categorias = [
        "Vinho", "Refrigerante", "Suco", "Cerveja", "Destilado",
        "Energético", "Gelo", "Água", "Sem Álcool", "Isotônico", "Cigarro"
    ]

    # Filtro de categorias
    filtro_categoria = st.multiselect("📌 Filtrar por categoria:", categorias)

    status, resultado = listar_produtos()

    if not status:
        st.warning(resultado)
        return

    df = resultado.copy()

    # Aplica filtro se selecionado
    if filtro_categoria:
        df = df[df["categoria"].isin(filtro_categoria)]

    # KPIs
    col1, col2 = st.columns(2)
    col1.metric("Total de Itens", int(df["quantidade"].sum()))
    col2.metric("Valor Total em Estoque", f"R$ {df['valor_total'].sum():,.2f}")

    # Tabela de produtos (sem índice)
    st.subheader("Produtos")
    df_exibir = df.reset_index(drop=True)  # Remove índice
    st.dataframe(df_exibir, use_container_width=True)

    # Gráfico de valor por categoria
    st.subheader("Valor por Categoria")
    valor_categoria = df.groupby("categoria")["valor_total"].sum().reset_index()

    fig, ax = plt.subplots()
    ax.bar(valor_categoria["categoria"], valor_categoria["valor_total"])
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Valor Total (R$)")
    ax.set_title("Distribuição do Estoque por Categoria")
    plt.xticks(rotation=45)

    st.pyplot(fig)
