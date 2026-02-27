import os
os.system("cls || clear")

lista_de_numeros = []

for i in range(5):
    numero= int(input("Digite um número: "))
    lista_de_numeros.append(numero)

maior = max(lista_de_numeros)
menor = min(lista_de_numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

for i, numero in enumerate(lista_de_numeros, start=1):
    print(f"Número na posição {i}: {numero}")