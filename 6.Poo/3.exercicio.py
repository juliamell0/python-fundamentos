import os
from dataclasses import dataclass
os.system("cls || clear")
#objeto= pesssoa1, como se fosse uma variavel que compoe varias variaveis e pode chamar metodos(programação orientada)

@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Informacoes:
    nome: str
    email: str
    telefone: str
    endereco: Endereco


    def exibindo_dados(self):
        print(f"Nome: {self.nome}. Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco.logradouro}, Número: {self.endereco.numero}")


nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
logradouro = input("Digite seu logradouro: ")
numero = input("Digite seu número: ")
endereco = Endereco(logradouro, numero)


pessoa1 = Informacoes(nome, email, telefone, endereco)

pessoa1.exibindo_dados()

#metodo: funcao dentro da classe

#atributo da classe (variaveis que pertencem a uma classe)