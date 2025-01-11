# Laços de repetição = Capitulo 6 - Questão 3

# Faça um programa que exiba todos os valores ímpares entre 50 e 100 utilizando o range.

numeros = list(range(0, 100))

# Exibindo apenas os números impares
print("Números Impares de 0 a 100:")
for numero in numeros:
    if numero % 2 == 1:
        print(numero)