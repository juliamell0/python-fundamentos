import os
from dataclasses import dataclass
os.system ("clear")

lista_de_livros = []
QUANTIDADE_DE_LIVROS = 3

@dataclass
class Livros:
#Atributos: são variáveis que pertencem a classe
    nome : str
    autor : str
    categoria : str
    preco : float
    def exibir_dados(self):
        print(f"Nome: {self.nome} \n autor: {self.autor}\n categoria: {self.categoria}\n preco: {self.preco}")

for i in range(QUANTIDADE_DE_LIVROS):
    livros = Livros(
            nome= input("Digite o nome do Livro: "),
            autor = input("Digite o Autor do livro:"),
            categoria = input("Digite a categoria do Livro: "),
            preco = float(input("Digite o Preço do Livro: ")))
    lista_de_livros.append(livros)
    print()

nome_arquivo = "Catalogo_livros.txt"
with open(nome_arquivo, "w") as arquivo_livros:
    for livros in lista_de_livros:
        arquivo_livros.write(f"{livros.nome}, {livros.autor}, {livros.categoria}, {livros.preco} \n")