# Laços de repetição = parte 2 = Capitulo 7 - Questão 3

# Faça um programa que inicialize uma lista vazia, solicite ao usuário 10 números ímpares diferentes, um por vez. Caso o número digitado seja par, solicite novamente um número, até que o valor seja um número ímpar. Depois disso, exiba os 10 números digitados.

# Inicializando uma lista vazia
numeros_impares = []

# Solicitando ao usuário 10 números ímpares diferentes
while len(numeros_impares) < 10:
    try:
        numero = int(input(f"Digite o {len(numeros_impares) + 1}º número ímpar: "))
        
        # Verifica se o número é par
        if numero % 2 == 0:
            print("O número digitado é par. Tente novamente.")
            continue
        
        # Verifica se o número já foi digitado
        if numero in numeros_impares:
            print("Você já digitou esse número. Tente novamente.")
            continue
        
        # Adiciona o número à lista
        numeros_impares.append(numero)
        
    except ValueError:
        print("Por favor, digite um número válido.")

# Exibindo os 10 números ímpares digitados
print("Os 10 números ímpares digitados são:")
for num in numeros_impares:
    print(num)
