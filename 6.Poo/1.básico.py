import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoa: 
  nome: str
  idade: int

@dataclass
class Pet: 
  nome: str
  idade: int
  raca: str
pet1= Pet("Maggie", 3 , "Maltês")
pet2= Pet("Rex", 5 , "Pastor Alemão")

pessoa1 = Pessoa("João", 20)
pessoa2 = Pessoa("Maria", 25)

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")
print(f"Pet 1 - Nome: {pet1.nome}, Idade: {pet1.idade}, Raça: {pet1.raca}")
print(f"Pet 2 - Nome: {pet2.nome}, Idade: {pet2.idade}, Raça: {pet2.raca}")
