# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print("~~"*15)
print("VAMOS JOGAR PAR OU IMPAR")
print("~~"*15)

v = 0
while True:
    jogador = int(input("Digite um Valor: "))
    computador = randint(0,20)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar [P / I]: ")).upper().strip()[0]
    print(f"Você jogou {jogador} e o computador foi {computador} ficando no total de {total} ", end = "")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("VOCÊ VENCEU")
            v+=1
        else:
            print("VOCÊ PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("VOCÊ VENCEU")
            v+=1
        else:
            print("VOCÊ PERDEU")
            break
    print()
    print("Vamos jogar novamente...")
print(f"GAMER OVER! você vence {v} vezes")