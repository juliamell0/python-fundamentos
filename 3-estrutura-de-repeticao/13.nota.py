import os
os.system("cls || clear")

QUANTIDADE_DE_NOTAS = 2

while True :
    primeira_nota = float(input("Digite sua nota em matemática: "))
    segunda_nota = float(input("Digite sua nota em física: "))
    media = (primeira_nota + segunda_nota) / QUANTIDADE_DE_NOTAS
    if primeira_nota < 0 or segunda_nota > 10:
        print("A nota deve ser entre 0 e 10")
    else:
        print(f"Média: {media}")
        break