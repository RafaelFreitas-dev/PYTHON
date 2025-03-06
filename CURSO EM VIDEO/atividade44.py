#Elabore um programa que calcule o valor a ser pago de um produto, considerando seu preço normal a condição de pagamento.

# A vista dinheiro/chegue: 10% de desconto
# A vista no cartã: 5% de desconto
# Em até 2 vezes no cartão: Preço normal
# 3x ou mais no cartão: 20% de Juros


print("="*20, "LOJAS FREITAS", "="*20)

preço = float(input("Valor das Compras: R$ "))

print(''' FORMAS DE PAGAMENTO 
      [ 1 ] À Vista Dinheiro/Pix
      [ 2 ] À vista Cartão
      [ 3 ] 2x no Cartão
      [ 4 ] 3x ou mais no Cartão''')
opção = int(input("Qual é a Opção: "))

if opção == 1:
    saldo = preço - (preço * (10 / 100))
    print("A vista no dinheiro ou pix com desconto de 10% ficará", saldo)
    
elif opção == 2:
    saldo = preço - (preço * (5 / 100))
    print("A vista no cartão com desconto de 5% ficará", saldo)
    
elif opção == 3:
    parcelas = preço / 2
    saldo = preço
    print(" Sua compra de {} dividido de 2x ficara {} por mês.".format(preço, parcelas))
    
elif opção == 4:
    parcelas = int(input("Quantas vezes quer parcelar com juros: "))
    saldo = preço * 1.20
    tot = saldo / parcelas
    print("O total de R${} com acrecimos de 20% fica R${}, parcelado de {} vez  fica {} por mês".format(preço, saldo, parcelas, tot))
else:
    saldo= preço
    print("Erro ### Digite um numero valido")
    
print("Sua compra de  {} vai custar {} no final.".format(preço, saldo))