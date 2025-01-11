# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considernado o valor do dolar a 5,50.

dim = float(input('Quantos Reais você tem na carteira: R$ '))

dolar = dim / 5.50

print(' Com {:.2f} Reais você pode comprar US$ {:.2f} Dolares.'.format(dim, dolar))