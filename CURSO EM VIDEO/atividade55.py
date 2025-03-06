# Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi a maior e o menor peso lidos.


maior = 0
menor = 0


for c in range(1,6):
    peso = float(input("Peso da {} pessoa: ".format(c)))
    
    if c == 1: # Esta dizendo se C for igual a 1, comece a contar...
        maior = peso 
        menor = peso
    else: # Como c não foi igual a 1, começou a rodar essa parte do programa
        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso
    
    
print("O maior peso lido foi de {}".format(maior))
print("O menor peso lido foi de {}".format(menor))    