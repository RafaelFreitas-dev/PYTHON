# Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa.
# Pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salario ou então o emprestimo será negado.

casa = float(input("Qual o valor da casa: "))
sal = float(input("Qual o seu salario: "))
anos = int(input("Quantos anos de financiamento: "))

prestacao = casa / (anos*12)
minimo = sal * 30 / 100

print("Para pagar uma casa de R$ {:.2f} em {:.2f} anos ".format(casa, anos), end="")
print(" a prestação será de R$ {:.2f}".format(prestacao))

if prestacao <= minimo:
    print("Empretimo concedido")
else :
    print("Emprestimo Negado")
