import os
os.system ("cls || clear")



def converter_metros(centimetros):
    return metros * 100

print("= CONVERTER METROS EM CENTIMETROS =")
metros = float(input("Digite  um número: "))

centimetros= converter_metros(metros)

print("\n= Resultados =")
print(f"{metros} metros é igual a {centimetros} centímetros. ")