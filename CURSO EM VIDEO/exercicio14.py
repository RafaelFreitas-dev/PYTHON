# Escreva um programa que converta uma temperatura digitada em Graus C para F.

temp = float(input('Informe a temperatura atual em Graus Celsius: '))

f = 1.8 * temp + 32 # a formula para converter graus Celsius para fahrenheit é F = 1.8 x C + 32. Onde C é o grau.

print('A temperatura de {} Graus, Corresponde a {}F!'.format(temp, f))