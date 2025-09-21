import sqlite3

def conexao():
    return sqlite3.connect('database/sofIA_ETE.db')

def init_db():
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        create table if not exists produtos (
            cod_barras text primary key,
            produto text not null,
            preco_unit real not null,
            quantidade integer not null,
            categoria text,
            marca text not null
        )
    """)

    cursor.execute("""
        create table if not exists clientes (
            id integer primary key,
            nome text not null,
            email text unique not null,
            senha text not null
        )
    """)

    cursor.execute("""
        create table if not exists documentos (
            id integer primary key autoincrement,
            nome text,
            data_upload text
        )
    """)

    conn.commit()
    conn.close

#def view_estoque_total():
    #conn = conexao()
    #cursor = conn.cursor()

    #cursor.execute("create view if not exists estoque_total as select sum(preco_unit * quantidade) as estoque from produtos ")

    #conn.commit()
    #conn.close()