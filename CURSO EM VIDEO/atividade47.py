# Crie um prgrama que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep

for c in range(2, 51, +2): # laço de repetição iniciado no 2, indo até o 51 porque ele nao imprimi o numero indicado e pular de 2 em 2
        print(c, end=" ")
        sleep(1)
    
print("Contagem efetuada mostrando só numeros positivos na tela ")