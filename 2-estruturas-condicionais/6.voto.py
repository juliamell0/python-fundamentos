import os
os.system ("clear")

dia_da_semana = int(input(""""
 número  dia da semana 
 1 \t Domingo
 2 \t Segunda-feira
 3 \t terça-feira
 4 \t quarta-feira
 5 \t Quinta-feira
 6 \t Sexta-feira
 7 \t Sábado
                  
Digite a opção desejada: """))

match dia_da_semana:
    case 1:
     print("Dia da semana: Domingo, final de semana")
    case 2:
     print("Dia da semana: Segunda-feira, dia útil")
    case 3:
     print("Dia da semana: terça-feira, dia útil")
    case 4:
     print("Dia da semana: quarta-feira, dia útil")
    case 5:
     print("Dia da semana: quinta-feira, dia útil")
    case 6:
     print("Dia da semana: sexta-feira, dia útil")
    case 7:
     print("Dia da semana: sábado, final de semana")
          
    case _:    
     print("Dia inválido.")