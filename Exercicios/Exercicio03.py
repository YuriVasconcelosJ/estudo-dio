# Somando preços (tuplas simples)

produtos = [("Arroz", 10.50), ("Feijão", 8.75), ("Macarrão", 6.90)]

valor_total = [valor for _, valor in produtos]
itens = [item for item, _ in produtos]

print(valor_total)
print(itens)

# Podemos fazer dessa maneira:
for item, valor in zip(itens, valor_total):
    print(f"{item}: R${valor:.2f}")
print("-" *20)
# Segunda maneira:
for i in range(len(itens)):
    print(f"{itens[i]}: R${valor_total[i]:.2f}")

print(f"Valor total da coompra R${sum(valor_total):.2f}")

print("-" * 30)

# Exercício 2
# Com a mesma lista do exercício anterior, exiba apenas os produtos que custam mais de R$8,00.

itens_maiores_oito = [item for item, valor in produtos if valor > 8.00]
print(itens_maiores_oito)