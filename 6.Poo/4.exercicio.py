import os
from dataclasses import dataclass
os.system ("clear")

@dataclass
class Paciente:
#Atributos: são variáveis que pertencem a classe
    nome : str
    idade : int

#Este método para exibir dados do paciente
    def exibir_dados(self):
        print(f"Nome: {self.nome} \n Idade: {self.idade}\n\n")


#Atribuindo dados ao paciente1.
lista_de_paciente = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
                        nome= input("Digite seu nome: "),
                        idade= int(input("Digite sua idade: ")))
    lista_de_paciente.append(paciente)

#Exibindo dados do paciente
print("\nExibindo dados do usuário.")
for paciente in lista_de_paciente:
    paciente.exibir_dados()