# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(DESCONSIDERANDO O FLAG)


soma = quant = 0

while True:
    num = int(input("Digite um Número: obs: parar 999? "))
    if num == 999:
        break
    quant +=1
    soma +=num
    
print(f"Foram digitados {quant} valores e somando é {soma}")
    