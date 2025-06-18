# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []
# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def ordem_prioridade(lista_pacientes):
    urgente = []
    idosos = []
    demais = []
    lista_final_ordenada = []
    for nome, idade, situacao in pacientes:
        if situacao == "urgente":
            urgente.append(nome)
        elif idade > 60:
            idosos.append(nome)
        else:
            demais.append(nome)

    lista_final_ordenada.extend(urgente)
    lista_final_ordenada.extend(idosos)
    lista_final_ordenada.extend(demais)
    return lista_final_ordenada
# TODO: Exiba a ordem de atendimento com título e vírgulas:
lista_ordenada = ordem_prioridade(pacientes)
nomes_formatados = ", ".join(lista_ordenada)
print(f"Ordem de atendimento: {nomes_formatados}")