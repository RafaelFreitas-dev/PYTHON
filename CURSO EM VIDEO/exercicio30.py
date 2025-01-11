# Crie um programa que leia um numero inteiro e diga se ele é par ou Impar.

num = int(input("Digite um Número: "))
resultado = num % 2

if resultado == 0:
    print("O numero escolido foi {}, portanto ele é Par".format(num))
else:
    print("O numero escolhido foi {}, portanto ele é Impar".format(num))
print("tenha um Bom Dia...")

