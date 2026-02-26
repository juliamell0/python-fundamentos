import os
os.system("cls || clear")

contador =0 
soma = 0
while True:
    nota=float(input("Digite sua nota: "))
    resposta = input("Deseja inserir mais uma nota: 's' ou 'n':").upper()
    if resposta == "N":
        break
    else:
        contador += 1
        soma+= nota
#Evitar divisão por 0
if contador == 0:
    soma = nota
    contador = 1
media = soma / contador
print(f"Média: {media}")
    
    