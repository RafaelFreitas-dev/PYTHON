# Dicionarios = Capitulo 8 - Questão 2

''' Faça um programa que inicialize uma lista de compras com 5 itens diferentes, onde cada item é um dicionário contendo a descrição e preço do produto. Depois disso, percorra a lista e exiba as informações de cada item.

lista_compras = [
    {"descrição": "Água", "preço": 2.00},
    {"descrição": "Leite", "preço": 3.00},
    {"descrição": "Carne", "preço": 18.00},
    {"descrição": "Pizza", "preço": 9.00},
    {"descrição": "Chocolate", "preço": 6.50},
]

for item_compra in lista_compras:
print("Produto:",( item_compra["descrição"]), "por", str(item_compra["preço"]), "reais."'''

# Inicializando a lista de compras com os 5 itens
lista_compras = [
    {"descrição": "Água", "preço": 2.00},
    {"descrição": "Leite", "preço": 3.00},
    {"descrição": "Carne", "preço": 18.00},
    {"descrição": "Pizza", "preço": 9.00},
    {"descrição": "Chocolate", "preço": 6.50},
]

# Percorrendo a lista e exibindo as informações de cada item
for itens in lista_compras:
    print("Produto:", itens["descrição"], "por R$", format(itens["preço"], '.2f'), "reais.") # concatenada "#", 
    
    # print("Produto {} por R$ {:.2f} reais".format(itens["descrição"], itens["preço"])) # com .format()