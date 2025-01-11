# CAPITULO 5 - QUESTÃO 2

# 2. Faça um programa que inicialize uma lista vazia e solicite ao usuário 3 nomes de cidades, um por vez, cada vez que o usuário digitar um nome, o programa deve incluir este nome na lista de cidades

# Inicializa uma lista vazia
cidades = []
quant = int(input("Quer colocar quantos nomes na sua lista : "))


for i in range(quant):
    cidade = input("Digite o nome de uma cidade: ")
    cidades.append("cidade")


print("As cidades digitadas foram:", cidades)
