# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
tot = 0

for c in range(1, num + 1):
    
    if num % c == 0:
        print("\033[33m", c, end=" ")
        tot = tot + 1
    else:
        print("\033[31m", c, end=" ")
print("\033[m O número foi dividido {} vezes.".format(tot))

if tot == 2:
    print("NÚMERO PRIMO")
else:
    print("NÃO É NÚMERO PRIMO")