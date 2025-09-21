class Produtos:

    def __init__(self, cod_barras, produto, preco_unit, quantidade, categoria, marca):
        self.cod_barras = cod_barras
        self.produto = produto
        self.preco_unit = preco_unit
        self.quantidade = quantidade
        self.categoria = categoria
        self.marca = marca

    @staticmethod
    def validar_cod_barras(cod_barras):
        if len(cod_barras) > 13:
            return False
        return True
    