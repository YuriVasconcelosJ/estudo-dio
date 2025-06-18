# Função adicionar_tarefa(lista_tarefas, tarefa):
# Recebe uma lista de tarefas e uma nova tarefa (string).
# Adiciona a tarefa à lista.
# Imprime uma mensagem de confirmação, como "Tarefa 'Estudar Python' adicionada."
lista_tarefas = []
opcoes = ["Adicionar Tarefa", "Listar Tarefas", "Marcar Tarefa com Concluída", "Sair"]

def adicionar_tarefa(lista_tarefas, tarefa: str):
    lista_tarefas.append(tarefa)
    print(f"Tarefa {tarefa} adicionanda com sucesso!")

def exibir_tarefa(lista_tarefas):
    print("Lista de tarefas:")
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for indice, tarefa in enumerate(lista_tarefas):
            print(f"{indice + 1}. {tarefa}")

def concluir_tarefa(lista_tarefas, indice_tarefa: int):
    if 1 <= indice_tarefa <= len(lista_tarefas):
        item_concluido = lista_tarefas.pop(indice_tarefa - 1)
        print(f"Tarefa '{item_concluido}' marcada como concluída!")
    else:
        print("Número de tarefa inválido. Por favor, digite um número existente na lista.")
def exibir_menu():
    for indice, opcao in enumerate(opcoes):
        print(f"{indice + 1}. {opcao}")

while True:
    exibir_menu()
    try:
        escolha = int(input("Escolha uma opção:").strip())
        if escolha == 1:
            tarefa = input("Informe a tarefa a ser inserida na lista").srtip()
            if tarefa: 
                adicionar_tarefa(lista_tarefas, tarefa)
            else:
                print("A tarefa não pode ser vazia")
        elif escolha == 2:
            exibir_tarefa(lista_tarefas)    
        elif escolha == 3:
            if not lista_tarefas:
                print("Nenhuma tarefa para concluir.")
            indice_tarefa_concluida = int(input("Digite o número da tarefa a ser conluída: "))
            concluir_tarefa(lista_tarefas, indice_tarefa_concluida)
        elif escolha == 4:
            print("Programa encerrando...")
            break
        else:
            print("Você digitou uma opção errada")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número para a opção ou para a tarefa.")
    except Exception as e: # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")