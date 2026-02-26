import os

os.system ("cls || clear")

pares = 0
impares = 0

print("NÚMEROS Pares e impares:")
for i in range(3):
    valor = int(input(f"Digite um número: "))

    if valor % 2 == 0:
            pares += 1
    else:
        impares += 1
   
print()
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")