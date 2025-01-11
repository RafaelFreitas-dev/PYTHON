# Dicionarios = Capitulo 8 - Questão 1


''' Faça um programa que crie um dicionário para definir um produto, contendo sua descrição e seu preço.
ex: produto = {
    "descrição": "Água",
    "preço": 2.00
} '''

# Criando um dicionário para definir um produto
produto = {
    "descrição": "Água",
    "preço": 2.00
}

# Exibindo as informações do produto
print("Detalhes do Produto:")
print(f"Descrição: {produto['descrição']}")
print("Preço: R$ {:.2f}".format(produto["preço"])) # foi utiizado o .format() para melhor visualização dos pontos flutuantes dentro do resultado .2f (2 pontos flutuantes) = (2.f) depois da virgula