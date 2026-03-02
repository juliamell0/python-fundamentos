import os
import time
from dataclasses import dataclass
os.system ("cls || clear")
# Corrige a função de exclusão para funcionar corretamente
lista_funcionarios = []

@dataclass 
class Funcionario:
    nome: str
    nascimento: str
    cpf: str
    funcao: str

def adicionando(lista_funcionarios):
    funcionario = Funcionario(
        nome = input("Digite o nome: "),
        nascimento = input("Digite a data de nascimento: "),
        cpf = input("Digite o cpf: "),
        funcao = input("Digite a função: "))
    
    lista_funcionarios.append(funcionario)
    print("\n Funcionário adicionado com sucesso.")

def mostrando(lista_funcionarios):
    print("\n - Lista de Funcionários - ")
    for funcionario in lista_funcionarios:
        print(f"- {funcionario.nome}, {funcionario.nascimento}, {funcionario.cpf}, {funcionario.funcao}")

def atualizando(lista_funcionarios):
            mostrando(lista_funcionarios)
            nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
            for funcionario in lista_funcionarios:
                if funcionario.nome == nome_atualizar:
                    print("O que deseja atualizar?")
                    print("1 - Nome")
                    print("2 - Nascimento")
                    print("3 - CPF")
                    print("4 - Função")
                    opcao = input("Escolha uma opção: ")
                    if opcao == "1":
                        funcionario.nome = input("Novo nome: ")
                    elif opcao == "2":
                        funcionario.nascimento = input("Nova data de nascimento: ")
                    elif opcao == "3":
                        funcionario.cpf = input("Novo CPF: ")
                    elif opcao == "4":
                        funcionario.funcao = input("Nova função: ")
                    else:
                        print("Opção inválida.")
                    print("Funcionário atualizado com sucesso.")
                    return
            print("Funcionário não encontrado.")

def excluir_nome(lista_funcionarios):
    mostrando(lista_funcionarios)
    funcionario_remove = input("Digite o funcionário que deseja remover: ")
    if funcionario_remove in lista_funcionarios:
        lista_funcionarios.remove(funcionario_remove)
        print(f"{funcionario_remove} foi removido com sucesso.")
    else:
        print(f"O funcionário {funcionario_remove} não foi encontrado.")

while True:
    print("""
    - Gerenciador de funcionarios -
    1 - Adicionar
    2 - Listar Funcionarios
    3 - Atualizar
    4 - Remover
    5 - Sair
""")
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
           adicionando(lista_funcionarios)
           os.system ("cls || clear")
        case 2:
            mostrando(lista_funcionarios)

        case 3:
            atualizando(lista_funcionarios)
            os.system ("cls || clear")
        case 4:
            excluir_nome(lista_funcionarios)
            os.system ("cls || clear")
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    input("\nPressione Enter para continuar...")
    os.system("cls || clear")
    time.sleep(4)