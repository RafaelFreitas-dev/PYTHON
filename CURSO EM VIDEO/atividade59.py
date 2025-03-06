# Crie um programa que leia dois valores e mostre um menu como como ao lado na tela: Seu programa deverá realizar a operação solicitada em cada caso.

# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] MAIOR
# [ 4 ] NOVOS NÚMEROS
# [ 5 ] SAIR DO PROGRAMA
from time import sleep


# PERGUNTAS
n1 = int(input("Digite o Primeiro Valor: "))
n2 = int(input("Digite o Segundo Valor: "))

opção = 0
while opção != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input("Qual é a sua opção: "))
    if opção == 1:
        soma = n1 + n2
        print("A soma de {} + {} é {}.".format(n1,n2,soma))
    elif opção == 2:
        multi = n1 * n2
        print("A multiplicação de {} x {} é {}.".format(n1, n2, multi))
    
    elif opção == 3:
        if n1>n2:
            n1=n1
            print("O Primeiro número escolhido foi {} portanto ele é maior. ".format(n1))
        else:
            print("O Segundo número escolhido foi {} porntanto ele é maior.".format(n2))
        
    elif opção == 4:
        n1 = int(input("Digite o Primeiro Valor Novamente: "))
        n2 = int(input("Digite o Segundo Valor Novamente: "))
        
    elif opção == 5:
        print("Finalizando...")
        
    else:
        print("Opção invalida!!!")
    print("-=="*20)
    sleep(2)
print("Fim do programa! Volte Sempre!")
