import os
os.system ("clear")

valor = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
Código:     Forma de Pagamento:
 1            À vista
 2            À prazo

Digite a forma de pagamento: """))



match forma_de_pagamento:
    
    case 1:
        desconto = float(valor * 0.10)
        print(f"Valor total: {valor - desconto} ")
        print(f"Valor do desconto: {desconto}")
        
    case 2:
            parcelas = int(input("Digite a quantidade de parcelas desejada: "))
            parce = valor / parcelas
            match parcelas:
                case 1:
                      print("Pagará uma parcela")
                case 2:
                      print("Pagará duas parcelas")
                case 3:
                      print("Pagará três parcelas")
                case 4:
                      print("Pagará quatro parcelas")
            print(f"Valor das parcelas: {parce}")

