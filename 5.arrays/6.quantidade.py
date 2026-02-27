import os
os.system("cls || clear")

quantidade_de_numeros= 5
lista_numeros = []

for i in range(quantidade_de_numeros):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

def pares_impares(lista):
    pares = 0
    impares = 0
    
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    return pares, impares

mostrando = pares_impares(lista_numeros)

print(f"Números Pares: {mostrando[0]}")
print(f"Números Ímpares: {mostrando[1]}")