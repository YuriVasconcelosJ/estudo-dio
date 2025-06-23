# Inner Function
# Função com retorno de função

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função")
    
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá {nome}")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

# Sem marcador
def aprimorar_foto(funcao_de_foto): # 'funcao_de_foto' é a nossa 'tirar_foto' original
    # Dentro do recurso, ele cria uma NOVA forma de tirar a foto
    def nova_funcao_de_foto_aprimorada():
        print("Preparando câmera...") # Mensagem "antes"
        funcao_de_foto()             # CHAMA a função original de tirar a foto
        print("Salvando na galeria...") # Mensagem "depois"

    return nova_funcao_de_foto_aprimorada # O recurso te entrega essa nova função aprimorada


# Utilizando marcador
def aprimorar_foto(funcao_de_foto):
    def nova_funcao_de_foto_aprimorada():
        print("Preparando câmera...")
        funcao_de_foto()
        print("Salvando na galeria...")
    return nova_funcao_de_foto_aprimorada

@aprimorar_foto # Isso é o mesmo que 'tirar_foto = aprimorar_foto(tirar_foto)'
def tirar_foto():
    print("Click! Foto tirada.")

tirar_foto()


def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")

aprender("Python")

# Retornando valores de função decoradas

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)

# Introspecção - functools