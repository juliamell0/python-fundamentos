import os
import time
os.system ("clear")

print("Apenas números Ímpares:")
for i in range(100,121):
    if i % 2 != 0:
        print(i)
    time.sleep (0.5)