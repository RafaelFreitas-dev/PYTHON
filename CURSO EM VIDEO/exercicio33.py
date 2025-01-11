# Faça um programa que leia 3 numeros e mostre qual é o maior e o menor

a = int(input("Digite o primeiro valor: "))
b = int(input("Escolha o Segundo Valor: "))
c = int(input("Escolha o terceito valor: "))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print("O valor Menor é: {}".format(menor))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O valor Maior é: {}".format(maior))