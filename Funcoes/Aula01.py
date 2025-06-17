# Funções - Blocos de código reutilizáveis, retornam algo ou não
# Criamos a função utiilizando o def
# Parámetros é oq passa na função, argumentos são os valores q passamos para realizar o funcionamento da função

def minha_primeira_funcao():
    """Esta é a docstring. Ela explica o que a função faz."""
    print('Olá, mundo')

def entrar_mensagem(nome):
    print(f"Seja bem vindo {nome}")
# Seja bem vindo Yuri

def exibir_mensagem_nome_nela(nome="Anônimo"):
    print(f'Seja bem vindo {nome}')

# Seja bem vindo anônimo

# Chamando a função
minha_primeira_funcao() # Olá, mundo

exibir_mensagem_nome_nela()  # Seja bem vindo anônimo

entrar_mensagem("Yuri") # Seja bem vindo Yuri

# Funções com retorno - São funções q vão retornar algo para o código

def somar(a, b): 
    """Retornar a soma de doiss números."""
    result = a + b
    return result


def calcular_total(numeros):
    return sum(numeros)

def func_3():
    print("Olá mundo!") 
    # Por padrão, o python implicitamente retorna None

soma_total = somar(5, 3)
print(f"A soma é: {soma_total}") # 8

print(calcular_total([10, 20, 30, 40, 50])) # 150


# Tipos de Argumentos

# Argumentos Posicionais
def dividir(dividendo, divisor):
    return dividendo/divisor

print(dividir(10, 2)) # dividendo=10, divisor=2
print(dividir(2, 10)) # dividendo=2, divisor=10

# Argumentos de Palavre-Chave
def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Pálio", 1999, "ABC-1234")
salvar_carro(marca="Fiat",modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa":"ABC-1234"})

# args e kwargs

# *args(Argumentos Posicionais Variáveis): Permite q uma função aceite um número variável de argumentos posicionais. Eles são recebidos como uma tupla
def somar_tudo(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total
print(soma_total(1,2,3)) # 6

# **kwargs(Argumentos Nomeados Variáveis): Permite q uma função aceite um número variável de argumentos nomeados. Eles são recebidos como um dicionárrio

def exibir_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Ana", idade=30, cidade="Recife")
# nome: Ana
# idade: 30
# cidade: Recife

# Funçẽos Anônimas(Lambda)

multuplicar = lambda a, b: a *b
print(multuplicar(4, 5))

lista_numeros = [1, 2 , 3, 4, 5]
quadrados = list(map(lambda x: x**2, lista_numeros))
print(quadrados) # [1, 4, 9, 16, 25]