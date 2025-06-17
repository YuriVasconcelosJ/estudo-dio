# Dicionários

# Maneira de criar dicionários
pessoa = {"Nome": "Yuri", "Idade": 21}

# Segunda maneira
pessoa = dict(nome="Yuri", idade=21)

pessoa["telefone"] = "3333-1234" 

# Acessando os dados de um dicionário

dados = {"Nome": "Yuri", "Idade": 21, "Telefone": "9999-9999"}

dados["Idade"] # 28
dados["Nome"] # Yuri

# Dicionários aninhados

contatos = {
    "yurivascs@gmail.com" : {"nome": "Yuri", "Telefone": "8888-8888"},
    "teste@gmail.com" : {"nome": "Teste", "Telefone": "9999-9999"}
}