import os
os.system ("cls || clear")

# Criando uma lista.
lista_nota = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_nota.append(nota)

#append significa que esta adicionando na lista de nota

# Exibindo todos os vetores em uma lista.
print()
for nota in lista_nota: #ForEach= for que vc n diz a quantidade de elementos, 
#descobre sozinho quantos núm. tem no vetor
    print(nota)
