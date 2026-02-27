import os

def limpando():
    os.system ("cls || clear")

def somando(n1, n2):
    soma= n1 + n2
    return soma
def subtraindo(n1, n2):
    subtracao= n1 - n2
    return subtracao
def multiplicando(n1, n2):
    multiplicacao= n1 * n2
    return multiplicacao
def dividindo(n1, n2):
    divisao= n1 / n2
    return divisao

limpando()
n1= float(input("Digite um número: "))
n2= float(input("Digite um número: "))


soma = somando(n1, n2)
subtracao = subtraindo(n1, n2)
multiplicacao = multiplicando(n1, n2)
divisao = dividindo(n1, n2)

limpando()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")