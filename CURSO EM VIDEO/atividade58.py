# Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinha até acertar, mostrando no final quantos palpites foram necessarios para vencer.

# Cores em python

vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
roxo = "\033[35m"
sr = "\033[36m"
cinza = "\033[37m"
cancela = "\033[m"


# Importando só a função RANDINT
from random import randint
pc = randint(0, 10) # o pc vai Escolher um número aleatorio entre 0 e 10.

print(verde,"Sou seu computador...")
print("Acabei de pensar em um numero entre 0 e 10.")
print("Será que você consegue advinhar qual foi..", cancela)

acertou = False
palpite = 0

while not acertou:
    jogador = int(input("Qual foi o seu palpite "))
    palpite = palpite + 1
    if jogador == pc:   
        acertou = True
    else:
        if jogador < pc:
            print("Mais... tente mais uma vez.")
        else:
            print("Menos... tente mais uma vez")
        
print("Você Acertou em {}{} tentativas...{}".format(verde, palpite, cancela))