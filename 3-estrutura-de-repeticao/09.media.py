import os
os.system ("cls || clear")

soma = 0

print("Média das notas:")
for i in range(1, 5):
    numero = float(input(f"Digite sua {i}º nota:  "))
    soma += numero

media = soma / 4
print()
print(f"Média: {media}")

if media < 4:
    print("Reprovado!")
elif media >= 7:
    print("Aprovado!")
else: 
    print("Você está em recuperação!")

      
