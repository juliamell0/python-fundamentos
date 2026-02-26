import os
os.system ("cls || clear")

soma = 0
quantidade_notas = 2

for i in range(quantidade_notas):
    while True:
        nota = float(input("Digite sua nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida...\nTente novamente!")
        else:
            soma += nota
            break
            
    media = soma / quantidade_notas
    if media >= 7:
        resultado =("Você está Aprovado!")
    elif media >= 5:
        resultado =("Você está em recuperação")
    else:
        resultado =("Você está reprovado!")

print(f"Média: {media}")
print(f"Resultado: {resultado}")
