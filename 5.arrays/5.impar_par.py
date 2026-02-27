import os
os.system("cls || clear")

lista_de_numeros = []
impares = 0
pares = 0

for i in range(6):
    numero = int(input("Digite um número: "))
    lista_de_numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números Ímpares: {impares}")
print(f"Números Pares: {pares}")
for i, numero in enumerate(lista_de_numeros, start=1):
    print(f"Número na posição {i}: {numero}")