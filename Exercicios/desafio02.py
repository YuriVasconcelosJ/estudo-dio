class Produto:
    def __init__(self, nome: str, preco: float, qtd_estoque: int):
        self.nome = nome          # chama o setter com validação
        self.preco = preco        # idem
        self.qtd_estoque = qtd_estoque  # idem

    # --- Nome ---
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Nome deve ser uma string não vazia.")
        self.__nome = novo_nome.strip()

    # --- Preço ---
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if not isinstance(novo_preco, (int, float)) or novo_preco < 0:
            raise ValueError("Preço deve ser um número positivo.")
        self.__preco = float(novo_preco)

    # --- Estoque ---
    @property
    def qtd_estoque(self):
        return self.__qtd_estoque

    @qtd_estoque.setter
    def qtd_estoque(self, nova_qtd: int):
        if not isinstance(nova_qtd, int) or nova_qtd < 0:
            raise ValueError("Quantidade em estoque deve ser um inteiro não negativo.")
        self.__qtd_estoque = nova_qtd

    # --- Métodos ---
    def baixar_estoque(self, qtd: int):
        if not isinstance(qtd, int) or qtd <= 0:
            raise ValueError("A quantidade a baixar deve ser um número inteiro positivo.")
        if qtd > self.__qtd_estoque:
            raise ValueError("Estoque insuficiente.")
        self.__qtd_estoque -= qtd
