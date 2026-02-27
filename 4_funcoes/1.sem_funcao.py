import os

#Função sem retorno
def logo():
    os.system("cls || clear")
    print("== Logo ==")

logo()
#Chamando função
nome= input("Digite seu nome: ")
logo()
idade= int(input("Digite sua idade: "))

logo()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
