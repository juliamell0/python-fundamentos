import os

def limpando():
    os.system ("cls || clear")

def calculando_media(n1, n2):
    soma = n1 + n2
    media = soma / 2
    return media

limpando()
n1 = float(input("Digite a primeria nota: "))
n2 = float(input("Digite a segunda nota: "))

media = calculando_media(n1, n2)
print(f"Média: {media}")