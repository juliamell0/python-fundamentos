import os
from dataclasses import dataclass
os.system ("clear")

lista_de_paciente= []
QUANTIDADE_DE_PACIENTES = 2

@dataclass
class Paciente:
#Atributos: são variáveis que pertencem a classe
    nome : str
    idade : int
    peso : float
    altura : float
    def exibir_dados(self):
        print(f"Nome: {self.nome} \n Idade: {self.idade}\n Peso: {self.peso}\n Altura: {self.altura}")


for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
            nome= input("digite seu nome: "),
            idade =int(input("Digite sua idade: ")),
            peso= float(input("Digite seu peso:")),
            altura = float(input("Digite sua altura: "))
        )
    lista_de_paciente.append(paciente)
    print()
nome_arquivo = "Dados_paciente.txt"
with open(nome_arquivo, "w") as arquivo_pacientes:
    for paciente in lista_de_paciente:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}, {paciente.peso}, {paciente.altura} \n")


print("\nExibindo dados do usuário.")
for paciente in lista_de_paciente:
    paciente.exibir_dados()