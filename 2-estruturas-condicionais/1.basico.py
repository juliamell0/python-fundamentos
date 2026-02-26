import os
os.system("cls || clear")

dia = input("Digite um dia na semana: ")

match dia:
    case "segunda":
        print("Hoje é segunda-feira")
    case "terca":
        print("Hoje é terça-feira")
    case "quarta":
        print("Hoje é quarta-feira")
    case "quinta":
        print("Hoje é quinta-feira")
    case "sexta":
        print("Hoje é sexta-feira")
    case "sabado":
        print("Hoje é sabado")
    case "domingo":
        print("Hoje é domingo")

print("==FIM==")