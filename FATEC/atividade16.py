# Laços de repetição = Capitulo 6 - Questão 2

# Faça um programa que inicialize que crie uma lista com os valores de 1 até 10 e depois exiba apenas os números pares.


# Criando uma lista com valores de 1 a 10
numeros = list(range(1, 11))

# Exibindo apenas os números pares
print("Números pares de 1 a 10:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        

# Exibindo apenas os números impares
print("Números Impar de 1 a 10:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)