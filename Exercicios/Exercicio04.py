class Livro:
    qtd_livros_criados = 0

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__class__.qtd_livros_criados += 1
    
    def exibir_info(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    @classmethod
    def total_livro(cls):
        return(f"{cls.qtd_livros_criados} livros criados")

class Ebook(Livro):
    def __init__(self, titulo, autor, tamanho_mb):
        super().__init__(titulo, autor)
        self.tamanho_mb = tamanho_mb
    
    def exibir_info(self):
        return super().exibir_info() + f", tamanho_mb = {self.tamanho_mb}"