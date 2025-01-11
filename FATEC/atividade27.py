# Dicionarios = Capitulo 8 - Questão 3

'''Utilize a lista de compras do programa anterior para identificar qual o produto mais barato e qual o produto mais caro da lista de compras.

mais_barato = None
mais_caro = None
indice = 0
while indice < len(lista_compras):
    item_compra = lista_compras[indice]
        if indice == 0:
            mais_caro = item_compra
            mais_barato = item_compra
        else:
            if item_compra["preço"] > mais_caro["preço"]:
                mais_caro = item_compra
            if item_compra["preço"] < mais_barato["preço"]:
            mais_barato = item_compra
indice += 1
print("Produto mais caro: ", mais_caro["descrição"], "por", mais_caro["preço"],"reais")
print("Produto mais barato: ", mais_barato["descrição"], "por", mais_barato["preço"],"reais") '''

# Inicializando a lista de compras com 5 itens diferentes
lista_compras = [
    {"descrição": "Água", "preço": 2.00},
    {"descrição": "Leite", "preço": 3.00},
    {"descrição": "Carne", "preço": 18.00},
    {"descrição": "Pizza", "preço": 9.00},
    {"descrição": "Chocolate", "preço": 6.50},
]

# Inicializando variáveis para o produto mais barato e mais caro
mais_barato = None
mais_caro = None
indice = 0

# Loop para identificar o produto mais barato e mais caro
while indice < len(lista_compras):
    itens = lista_compras[indice]

    if indice == 0:
        mais_caro = itens
        mais_barato = itens
    else:
        if itens["preço"] > mais_caro["preço"]:
            mais_caro = itens

        if itens["preço"] < mais_barato["preço"]:
            mais_barato = itens

    indice += 1  # Incrementa o índice

# Exibindo os produtos mais caro e mais barato
'''print("Produto mais caro:", mais_caro["descrição"], "por R$", format(mais_caro["preço"], '.2f'), "reais.")
print("Produto mais barato:", mais_barato["descrição"], "por R$", format(mais_barato["preço"], '.2f'), "reais.")'''


print("Produto mais barato: {} por R$ {:.2f} reais.".format(mais_barato["descrição"], mais_barato["preço"]))
print("Produto mais caro: {} por R$ {:.2f} reais.".format(mais_caro["descrição"], mais_caro["preço"]))
