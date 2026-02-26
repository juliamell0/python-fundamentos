import os
os.system ("cls || clear")

while True:
    login_cadastrado = "julia"
    senha_cadastrada = "12345"
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_cadastrado and senha == senha_cadastrada:
        print("Acesso Liberado!")
        break
    else:
        print("Login ou senha inválidos!")

