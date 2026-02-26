import os
os.system ("clear")

def limpar():
    os.system ("clear")

contador = 0
soma_salario = 0
maior_idade=0
menor_idade= 9999
mulher5k =0

while True:
    opcao = int(input("""
    Código:  | Descrição:
       1     | Adicionar pessoa
       2     | Exibir resultados
       3     | Sair
    digite a opção desejada: """))
    
    match opcao:
        case 1:
            limpar()
            idade = int(input("Digite a idade: "))
            sexo = input("digite o sexo (use M ou F): ").upper()
            salario = float(input("Digite o salário: "))
            contador += 1
            soma_salario += salario
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)
            if sexo == 'F' and salario >= 5000:
                mulher5k += 1
        case 2:
            limpar()
            if contador == 0:
                print("Nenhum dado cadastrado ainda.")
                continue
            while True:
                resultados = int(input("""
Código:  Descrição:
 1 \t Média de salário do grupo:
 2 \t Maior e menor idade do grupo
 3 \t Quantidade de mulheres com salário a patir de R$ 5.000,00  
 4 \t Voltar
Digite a opção desejada:           
"""))
                if resultados ==1:
                    limpar()
                    media_salario = soma_salario / contador
                    print(f"Média dos salários: {media_salario}")
                elif resultados == 2:
                    limpar()
                    print(f"Maior de idade do grupo: {maior_idade}")
                    print(f"Menor de idade do grupo: {menor_idade}")
                elif resultados == 3:
                    limpar()
                    print(f"Mulheres com mais de 5000: {mulher5k}")
                elif resultados == 4:
                    break 
                    limpar()
                else:
                    print("Opção inválida.")
                        
        case 3:
            print("== Fim do Programa ==")
        case _:
            print("Opção inválida.")

