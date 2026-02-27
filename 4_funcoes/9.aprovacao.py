import os

def limpando():
    os.system ("cls || clear")
limpando()

quantidade_notas = 2
nota = 0

for i in range(quantidade_notas):
    nota += float(input("Digite sua nota: "))

limpando()
def calculando(nota):
    media = nota / quantidade_notas

    if media >= 7:
        print("Aprovado!")
    else: 
        print("Reprovado!")
    return media

chamando = calculando(nota)
print(f"Média: {chamando}")