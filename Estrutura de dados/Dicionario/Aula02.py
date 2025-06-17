# Métodos em dionários

contatos = {
    "Guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-3333"},
    "Yuri@gmail.com": {"nome": "Yuri", "telefone": "8888-8888"},
    "Charlie@gmail.com": {"nome": "Charlie", "telefone": "9999-9999"},
    
}

contatos.clear() # contatos = {}

# Método copy

contatos = {"yuri@gmail.com": {"nome": "Yuri", "telefone": "6666-6666"}} 
copia = contatos.copy()
copia["yuri@gmail.com"] = {"nome": "YuriJ"}

# Método fromkeys

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}


dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": None, "telefone": None}

# Método get

contatos = {
    "yuriteste@gmail.com": {"nome": "Yuri", "telefone": "9999-9999"}
}

contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {})
contatos.get("yuriteste@gmail.com", {}) # {"yuriteste@gmail.com": {"nome": "Yuri", "telefone": "9999-9999"}}

# Método items

contatos = {
    "yuriteste@gmail.com": {"nome": "Yuri", "telefone": "9999-9999"}
}

contatos.items() # dict_items([()])

# Método Pop

