import os
import time
os.system("clear")

soma = 0
print("Ssomando números: ")
for i in range(3):
    nota = int(input("Digite um número: "))
    soma+=nota
    print()
    print(f"Soma: {soma}")
    time.sleep(0.5)
