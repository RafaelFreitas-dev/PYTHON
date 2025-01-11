# Laços de repetição = Capitulo 6 - Questão 4

# Faça um programa que inicialize uma lista vazia, solicite ao usuário 10 números diferentes, um por vez. Caso o número digitado seja par, acrescente um ao seu valor. Depois disso, exiba os 10 números digitados.

# Inicializando uma lista vazia
numeros = []

# Solicitando ao usuário 10 números diferentes
for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número: "))
            # Verifica se o número já foi digitado
            if numero in numeros:
                print("Você já digitou esse número. Tente novamente.")
                continue
            # Se o número é par, acrescenta 1
            if numero % 2 == 0:
                numero += 1
            # Adiciona o número à lista
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, digite um número válido.")

# Exibindo os 10 números digitados
print("Os 10 números digitados são:")
for num in numeros:
    print(num)
