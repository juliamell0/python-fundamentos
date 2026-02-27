import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa1 = Pessoa(nome, idade, peso, altura)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}")