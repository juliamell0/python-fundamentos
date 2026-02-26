import os
os.system ("cls || clear")

contador=0
soma=0

while True:
    nota=float(input("Digite sua nota:"))

    if nota>0:
        contador+=1
        soma+=nota
    else:
        print("Erro: número negativo!")
        break
media = soma/contador
print(f"Média: {media}")
