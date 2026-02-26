import os
os.system("cls || clear")

soma = 0
preco =0 
 
for i in range(1):
    while True:
      print("""
      Código:\t Prato:          \t  Valor:
        1    \t Picanha         \tR$ 25,00
        2    \t Lasanha         \tR$ 20,00
        3    \t Strogonoff      \tR$ 18,00
        4    \t Bife Acebolado  \tR$ 15,00
        5    \t Pão com ovo     \tR$ 5,00
        """)
      
      opcao= int(input("Digite a opção desejada: "))

      match opcao:
          case 1:
              print("Prato: Picanha, Valor: R$25,00")
              prato= "Picanha"
              preco = 25
          case 2:
              print('Prato: Lasanha, Valor: R$20,00')
              prato= "Lasanha"
              preco = 20
          case 3:
              print('Prato: Strogonoff, Valor: R$18,00')
              prato= "Strogonoff"
              preco = 18
          case 4:
              print('Prato: Bife acebolado, Valor: R$15,00')
              prato= "Bife acebolado"
              preco = 15
          case 5:
              print('Prato: Pão com ovo, Valor: R$5,00')
              prato= "Pão com ovo"
              preco = 5
          case _:
              print('Opção inválida!!')
      soma += preco

      continuar = input("Deseja escolher outro prato? \n 'S' ou 'N':").lower()
      if continuar == "n":
          break

print(f"\nTotal a pagar: R$ {soma}")