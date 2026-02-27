import os
os.system ("cls || clear")

lista_notas = []
nota = 0
quantidade_notas = 3

for i in range(quantidade_notas):
    nota+= float(input("Digite sua nota: "))
    lista_notas.append(nota)

for nota in lista_notas:
    media = nota / quantidade_notas

print(f"Média: {media:.2f}")