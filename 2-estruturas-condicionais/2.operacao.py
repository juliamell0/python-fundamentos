import os
os.system("cls || clear")

#entrada
n1 = int(input("Digite um número: "))
operador = input("Digite a operação desejada(/, *, -, +): ")
n2 = int(input("Digite outro número: "))


#Processamento
match operador:
    case "*":
        resultado = n1 * n2
    case  "/":
        resultado = n1 / n2
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
#Caso não apareça nenhum deles
    case _:
        resultado = "Opção inválida!"

#Saída
print(f"\nPrimeiro número: {n1}")
print(f"Operação: {operador}")
print(f"Segundo número: {n2}")
print(f"Resultado: {resultado}")