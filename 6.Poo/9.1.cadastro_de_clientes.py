import os
from dataclasses import dataclass
os.system ("clear")

lista_de_funcionarios = []
lista_de_clientes = []
QUANTIDADE_DE_FUNCIONARIOS = 1
QUANTIDADE_DE_CLIENTES = 1

@dataclass
class Funcionario:
    nome: str
    data: str
    matricula: str
    endereco: str
    def dados_funcionarios(self):
        print(f"Nome: {self.nome}, Data de admissão: {self.data}, Matrícula: {self.matricula}, Endereço: {self.endereco}. ")
@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str
    def dados_clientes(self):
        print(f"Nome: {self.nome}, Data de nascimento: {self.nascimento}, Endereço: {self.endereco}. ")


for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    funcio= Funcionario(
            nome= input("Digite o nome: "),
            data= input("Digite sua data de admissão:"),
            matricula = input("Digite sua matrícula: "),
            endereco = input("Digite seu endereço: "))
    lista_de_funcionarios.append(funcio)
    print()



for i in range(QUANTIDADE_DE_CLIENTES):
    clientes= Cliente(
            nome= input("Digite o nome: "),
            nascimento= input("Digite sua data de nascimento:"),
            endereco = input("Digite seu endereço: "))
    lista_de_clientes.append(clientes)
    print()


def arquivo(Funcionario):
    nome_arquivo = "Funcionarios.3.txt"
    with open(nome_arquivo, "w") as arquivo_funcionarios:
        for funcio in lista_de_funcionarios:
            arquivo_funcionarios.write(f"{funcio.nome}, {funcio.data}, {funcio.matricula}, {funcio.endereco} \n")
            
    
            
criando_arquivo_funcio = arquivo(Funcionario)

def arquivo(Cliente):
    nome_arquivo = "Clientes.3.txt"
    with open(nome_arquivo, "w") as arquivo_clientes:
        for clientes in lista_de_clientes:
            arquivo_clientes.write(f"{clientes.nome}, {clientes.nascimento}, {clientes.endereco} \n")

criando_arquivo_cliente = arquivo(Cliente)