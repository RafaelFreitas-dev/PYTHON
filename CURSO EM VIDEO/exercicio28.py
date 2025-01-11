#Escreva um programa que faça o computador 'PENSAR' em um numero inteiro entre 0 e 5 e pesa para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu.



from random import randint # Importando só o Randint da biblioteca random
from time import sleep # importando dó o sleep da biblioteca time

pc = randint(0, 5) # Faz o computador pensar = Sortear
print("-===-"*20)
print("VOU PENSAR EM UM NÚMERO DE 0 A 5. TENTE ADIVINHAR...")
print("-===-"*20)

num = int(input("Em que Número estou pensando agora: "))
print("PROCESSANDO...") 
sleep(2)

if pc == num:
    print("Parabéns.. Você ACERTOU")
else:
    print("Eu Ganhei... eu pensei no {} e você pensou no número {}, Quer revanche :)".format(pc, num))