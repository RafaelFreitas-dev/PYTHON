# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

pp = float(input('Qual é o Preço do Produto: R$'))

dp = pp - (pp * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(pp, dp))