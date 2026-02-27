import os
os.system ("cls || clear")




def calculando_idade(ano):
    return 2025 - ano

ano = int(input("Digite seu ano de nascimento: "))

mostrando_idade = calculando_idade(ano)

print(f"Idade: {mostrando_idade}")