# refaça o desafio 09, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for.

from time import sleep
tab = int(input("Qual tabuada quer Consultar: "))

for c in range(0,11):
    print("{} x {} = {}".format(tab, c, tab*c))
    sleep(1)
print("Contagem da tabuada do {}.".format(tab))