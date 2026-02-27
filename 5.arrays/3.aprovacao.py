import os
os.system ("cls || clear")


Quantidade_de_notas = 4
lista_notas = []

for i in range(Quantidade_de_notas):
    nota= float(input("Digite sua nota: "))
    lista_notas.append(nota)

def calculando_media(nota):
    media = sum(lista_notas) / Quantidade_de_notas
    return media 


def fazendo_resultado(media):
    if media >= 7:
            print("Aprovado!")
    elif media >= 5:
            print("Você está de Recuperação!")
    else:
            print("Reprovado!")
    return media

media= calculando_media(nota)
print(f"Sua média é: {media}")
resultado = fazendo_resultado(media)