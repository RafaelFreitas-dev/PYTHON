# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

num = int(input("Informe um Número: "))

'''div = str(num)
print("Analisando o Número {}".format(num))
print("Unidade {}".format(div[3]))
print("Dezena {}".format(div[2]))
print("Centena {}".format(div[1]))
print("Milha {}".format(div[0]))'''

# Neste modelo acima o programa funciona mais tem um pequeno problema que se digitar menos numeros ele nao funciona então a melhor forma de resolver esse Probrema é na forma matematica

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o Número {}".format(num))
print("Unidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milha {}".format(m))