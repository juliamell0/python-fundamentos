import os

def limpando():
    os.system ("cls || clear")
limpando()

def inflacionado(valor):
    if valor < 100:
       resultado= valor * 1.10

    else:
        resultado = valor * 1.20

    return resultado

valor = float(input("Digite o valor do produto: "))
inflacao = inflacionado(valor)

limpando()
print(f"Valor sem modificações: {valor}")
print(f"Valor total: {inflacao:.2f}")