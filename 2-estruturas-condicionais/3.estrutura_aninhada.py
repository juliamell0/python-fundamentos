import os
os.system("clear")

idade = 40
# se idade < 18
#   escreval("Acesso negado.")
#senao
#   escreval("Somente com permissão dos pais.")
#senao
#   escreval("acesso permitido")
#fimse

if idade < 12:
    print("Acesso negado.")
elif idade < 18:
    print("Somente com permissão dos pais.")
else:
    print("Acesso permitido")
 
print("== Fim ==")