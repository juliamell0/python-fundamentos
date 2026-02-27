import os
from dataclasses import dataclass
os.system ("cls || clear")

lista_de_livros = []
QUANTIDADE_DE_LIVROS = 1

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_dados(self):
        print(f"Título: {self.titulo} \n Ano: {self.ano}\n Autor: {self.autor.nome}")
print(f"= Solicitando dados para o usuário =")

for i in range(QUANTIDADE_DE_LIVROS):
    livro = Livro(
        titulo = input("Digite título do livro: "),
        ano = int(input("Digite o ano de publicação: ")),
        autor = Autor(
            nome = input("Digite o nome do autor:  "),
            biografia = input ("Digite as informações de bibliografia do autor: ")

        )
    )
    lista_de_livros.append(livro)
    print()

print("\n = Salvando dados =")

nome_arquivo = "Autor.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_livros:
    for livros in lista_de_livros:
        arquivo_livros.write(f"Nome: {livro.autor.nome}, biografia: {livro.autor.biografia}, título: {livro.titulo}, ano: {livro.ano} \n")

#exibindo dados do arquivo txt
print("\n= Lendo dados do arquivo =")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Aquivo não encontrado.")