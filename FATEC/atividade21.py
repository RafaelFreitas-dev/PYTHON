# Laços de repetição = parte 2 = Capitulo 7 - Questão 2

# Faça um programa que inicialize uma lista com os valores de 1 até 10 e depois exiba apenas os números pares utilizando while

# Criando uma lista com valores de 1 a 10
numeros = list(range(1, 11))

# Inicializando o contador
i = 0

# Exibindo apenas os números pares usando um laço while
print("Números pares de 1 a 10:")
while i < len(numeros):
    if numeros[i] % 2 == 0:  # Verifica se o número é par
        print(numeros[i])
    i += 1  # Incrementa o contador
