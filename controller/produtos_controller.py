from database.db import conexao
from models.Produtos import Produtos
import pandas as pd

def adicionar_produtos(cod_barras, produto, preco_unit, quantidade, categoria, marca):
    categorias = [
        "Vinho", "Refrigerante", "Suco", "Cerveja", "Destilado",
        "Energético", "Gelo", "Água", "Sem Álcool", "Isotônico",
        "Cigarro", "Sem Categoria"
    ]

    if not cod_barras.strip():
        return False, "O campo Código de Barras é obrigatório."
    if not produto.strip():
        return False, "O campo Nome do Produto é obrigatório."
    if preco_unit <= 0:
        return False, "O Preço Unitário deve ser maior que zero."
    if quantidade < 0:
        return False, "A Quantidade não pode ser negativa."
    if not marca.strip():
        return False, "O campo Marca é obrigatório."

    if categoria not in categorias:
        return False, f"Categoria inválida. Escolha entre: {categorias}"

    if not Produtos.validar_cod_barras(cod_barras):
        return False, "Insira um código de barras válido."

    try:
        conn = conexao()
        cursor = conn.cursor()

        cursor.execute("select cod_barras from produtos where cod_barras = ?", (cod_barras,))
        existente = cursor.fetchone()
        if existente:
            return False, "Produto já cadastrado com esse código de barras."

        produto_obj = Produtos(cod_barras, produto.title(), round(preco_unit, 2), quantidade, categoria, marca.title())

        cursor.execute(
            "insert into produtos (cod_barras, produto, preco_unit, quantidade, categoria, marca) values (?, ?, ?, ?, ?, ?)",
            (produto_obj.cod_barras, produto_obj.produto, produto_obj.preco_unit,
             produto_obj.quantidade, produto_obj.categoria, produto_obj.marca)
        )
        conn.commit()
    except Exception as e:
        return False, f"Erro ao cadastrar produto: {e}"
    finally:
        conn.close()

    return True, "Produto adicionado!"


def listar_produtos():
    try:
        conn = conexao()
        cursor = conn.cursor()

        cursor.execute("select * from produtos")
        registros = cursor.fetchall()

        if registros:
            colunas = [col[0] for col in cursor.description]
            df_produtos = pd.DataFrame(registros, columns=colunas)


            df_produtos["valor_total"] = df_produtos["preco_unit"] * df_produtos["quantidade"]

            return True, df_produtos
        else:
            return False, "Ainda não há produtos cadastrados."

    except Exception as e:
        return False, f"Erro ao listar os produtos: {e}"
    finally:
        conn.close()



def remover_produtos(cod_barras):
    try:
        conn = conexao()
        cursor = conn.cursor()

        cursor.execute("select cod_barras from produtos where cod_barras = ?", (cod_barras, ))
        registro = cursor.fetchone()

        if registro:
            cursor.execute("delete from produtos where cod_barras = ?", (cod_barras, ))
            conn.commit()
            return True, "Produto removido!"
        else:
            return False, "Produto não encontrado."
        
    except Exception as e:
        return False, f"Erro ao remover produto: {e}"
    finally:
        conn.close()


def alterar_produtos(cod_barras, n_produto, n_preco, n_quantidade, n_categoria, n_marca):
    categorias = [
        "Vinho", "Refrigerante", "Suco", "Cerveja", "Destilado",
        "Energético", "Gelo", "Água", "Sem Álcool", "Isotônico",
        "Cigarro", "Sem Categoria"
    ]

    if not cod_barras.strip():
        return False, "O campo Código de Barras é obrigatório."
    if not n_produto.strip():
        return False, "O campo Nome do Produto é obrigatório."
    if n_preco <= 0:
        return False, "O Preço Unitário deve ser maior que zero."
    if n_quantidade < 0:
        return False, "A Quantidade não pode ser negativa."
    if not n_marca.strip():
        return False, "O campo Marca é obrigatório."

    if n_categoria not in categorias:
        return False, f"Categoria inválida. Escolha entre: {categorias}"

    try:
        conn = conexao()
        cursor = conn.cursor()

        cursor.execute("select cod_barras from produtos where cod_barras = ?", (cod_barras,))
        registro = cursor.fetchone()

        if registro:
            cursor.execute(
                "update produtos set produto = ?, preco_unit = ?, quantidade = ?, categoria = ?, marca = ? where cod_barras = ?",
                (n_produto.title(), round(n_preco, 2), n_quantidade, n_categoria, n_marca.title(), cod_barras)
            )
            conn.commit()
            return True, "Produto alterado com sucesso!"
        else:
            return False, "Produto não encontrado!"

    except Exception as e:
        return False, f"Erro ao tentar alterar o produto: {e}"
    finally:
        conn.close()

    