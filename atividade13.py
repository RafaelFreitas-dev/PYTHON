# CAPITULO 5 - QUESTÃO 3

# 3. Faça um programa que inicialize uma lista com vários números diferentes, depois disso, solicite ao usuário um número, verifique se o número está ou não na lista e exiba uma mensagem notificando o usuário do resultado

numlista = [3, 7, 10, 15, 21, 30, 45, 60]


numdig = int(input("Digite um número: "))


if numdig in numlista:
    print(f"O número {numdig} está na lista.")
else:
    print(f"O número {numdig} não está na lista.")