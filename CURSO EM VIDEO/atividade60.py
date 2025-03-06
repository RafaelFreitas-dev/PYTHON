# faça um programa que leia um numero qualquer e mostre seu número fatorial
# 5! = 5x 4x 3x 2x 1 = 120

'''
num = int(input("Digite um número para calcular seu fatorial: "))

c = num
f = 1
print("Calculando seu fatorial:",num,"! = ", end ="")
while c > 0:
    print(c,"x " if c>1 else "= ", end="")
    f = f * c
    c = c - 1 # igual a c -= 1
    
print(f)'''

# Nesta resolução conseguimos efetuar este exercicio em 5 linhas porem nao conseguimos demonstrar e com claresa os numeros sendo somado, somente colocar o valor que quer calcular e o resultado.
from math import factorial
num = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(num)
print("O fatorial de {} é = {}".format(num, f))