import os

def limpando():
    os.system ("cls || clear")
limpando()

quantidade_notas = 3
nota = 0

for i in range(quantidade_notas):
    nota += float(input("Digite sua nota: "))

limpando()

def calculando_media(nota):
    media = nota / quantidade_notas
    return media

mostrando = calculando_media(nota)
print(f"Média: {mostrando}")