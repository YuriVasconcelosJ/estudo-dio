# Parâmetros especiais
# Antes da barra, vai aceitar apenas parametros posicionais
# Após a barra, vai aceitar parâmetros nomeados
# A utilização do * serve para indicar que após ele, só vai aceitar argumentos nomeados

# Utilização da / para indicar que antes só dela só vai aceitar posiciononais
def criar_carro(modelo, ano, placa,/, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 199, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Utilização do * para indicar 
def configurar_sistema(user, *, vebose=False, log_file=None):
    # 'user' pode ser passado por posição ou nome
    # 'verbose' e 'log_file' DEVEM ser passados por nome
    print(f"Usuário: {user}")
    print(f"Verbose: {vebose}")
    print(f"Log File: {log_file}")

configurar_sistema("admin", verbose=True)
    
# Funções de primeira classe em objetos

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


# Escopo global e local
salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista) # 2500
print(salario_com_bonus)
print(lista)