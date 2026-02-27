import os
from dataclasses import dataclass
os.system ("clear")

lista_de_funcionarios= []
QUANTIDADE_DE_FUNCIONARIOS = 5

@dataclass
class Funcionarios:
#Atributos: são variáveis que pertencem a classe
    nome : str
    nascimento : str
    rg : str
    cpf : str
    def exibir_dados(self):
        print(f"Nome: {self.nome} \n nascimento: {self.nascimento}\n Rg: {self.rg}\n CPF: {self.cpf}")

for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    usuarios = Funcionarios(
            nome= input("Digite o nome: "),
            nascimento = input("Digite sua data de nascimento:"),
            rg = input("Digite seu RG: "),
            cpf = input("Digite seu CPf: "))
    lista_de_funcionarios.append(usuarios)
    print()

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "w") as arquivo_livros:
    for livros in lista_de_funcionarios:
        arquivo_livros.write(f"{livros.nome}, {livros.nascimento}, {livros.rg}, {livros.cpf} \n")