# Crie um programa que faça o computador jogar JOKENPÔ com você

from random import randint
from time import sleep

itens = ("Pedra", "Papel", "tesoura")
computador = randint(0,2)

print(''' Suas opções:
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura''')

jogador = int(input("Qual a sua jogada"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")

print("-="*20)
print("O computador jogou {}.".format(itens[computador]))
print("o jogador jogou {}".format(itens[jogador]))
print("-="*20)

if computador == 0: # computador jogando Pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR GANHOU")
    elif jogador == 2:
        print("COMPUTADOR GANHOU")
    else:
        print(ERRO)
    
elif computador == 1: # computador jogando Papel
    if jogador == 0:
        print("COMPUTADOR GANHOU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR GANHOU")
    else:
        print(ERRO)
    
elif computador == 2: # computador jogando Tesoura
    if jogador == 0:
        print("JOGADOR GANHOU")
    elif jogador == 1:
        print("COMPUTADOR GANHOU")
    elif jogador == 2:
        print("EMPATE")
    else:
        print(ERRO)
