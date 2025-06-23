# Criar um decorador que mede o tempo de execução

# import time

# def medir_tempo(func):
#     def tempo_para_execucao():
#         inicio = time.time()
#         func()
#         fim = time.time()
#         print(f"A função demorou {fim - inicio:.2f}")
    
#     return tempo_para_execucao

# @medir_tempo
# def tarefa_pesada(): # tarefa_pesada = medir_tempo(tarefa_pesada)
#     time.sleep(2)
#     print("Função finalizada!")


# tarefa_pesada()


# Decorador que exige login

usuario_logado = True

def exigir_login(func):
    def envelope(*args,**kwargs):
        if usuario_logado:
            return func(*args, **kwargs)
        else:
            print("Acesso negado!")
        return envelope
@exigir_login # acessar_dados = exibir_login(acessar_dados)
def acessar_dados():
    print("Dados sensíveis sendo acessados...")

acessar_dados()
