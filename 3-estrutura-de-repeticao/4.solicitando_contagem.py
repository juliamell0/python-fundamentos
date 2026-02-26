import os
import time
os.system ("clear")

numero= int(input("Digite um número: "))
for i in range(numero,0,-1):
    print(f"Número: {i}")
    time.sleep(1)