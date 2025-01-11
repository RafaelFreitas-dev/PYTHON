# Laços de repetição = Capitulo 6 - Questão 5

# 5. Faça um programa que exiba as tabuadas de 1 até 10 no formato: "2 x 3 = 6", (utilize dois comandos for)



# Exibindo as tabuadas de 1 até 10
for i in range(1, 11):  # Primeira iteração para os números de 1 a 10
    for j in range(1, 11):  # Segunda iteração para os multiplicadores de 1 a 10
        resultado = i * j
        print(f"{i} x {j} = {resultado}")  # Exibe a tabuada no formato desejado
    print()  # Adiciona uma linha em branco entre as tabuadas
