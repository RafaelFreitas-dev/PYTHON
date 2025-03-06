# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.abs

from time import sleep

print("=-"*10)
print("MAIOR E MENOR")
print("=-"*10)

res = 'S'
soma = cont = maior = menor = 0
while res == 'S':
    num = int(input("Digite um número: "))
    soma = soma + num
    cont+=1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor = num
    res = str(input("Deseja continuar [S/N]: ")).upper().strip()[0] # Foi utilizado o upper para deixar todos em maiusculos e strip para tirar todos os espaços e a lista para considerar só a primeira letra.
media = soma/cont
print("Foram contados {} numeros digitados e a soma deles é {}  ficando na média {}.".format(cont,soma,media))
print("O maior é {} e o menor é {}".format(maior, menor))
sleep(2)
print("Acabou, Volte Sempre...")