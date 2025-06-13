# # End e sep
# nome = 'Renato'
# sobrenome = ' Carvalho'

# print(nome, sobrenome)
# print(nome, sobrenome, end="...\n")
# print(nome, sobrenome, sep="#")

# # entrada de valores

# nome = input("Informe o seu nome:")
# print(nome)

# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
def verificar_email(email):
    if "@gmail.com" in email or "@outlook.com" in email:
        if email.endswith("@") or email[0] == '@' or " " in email:
            return "E-mail inválido"
        return "E-mail válido"
    else:
        return "E-mail inválido"
