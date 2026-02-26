import os
os.system("clear")

contador = 0
soma = 0 
par = 0
impar=0
soma_pares = 0
soma_impares = 0


while True:
    valor = int(input("Digite um valor: "))
    contador +=1
    soma+= valor
    if valor % 2 == 0:
        par+=1
        soma_pares += valor
    else:
        impar+= 1
        soma_impares+= valor
    if valor == 1:
        break
media_pares = soma_pares / par
media_impares = soma_impares/ impar

print(f"Números pares: {par}")
print(f"Números impares: {impar}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números Ìmpares: {media_impares:.2f}")