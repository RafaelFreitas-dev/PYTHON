# Faça um programa que solicite ao usuário 2 valores, utilize uma condição ternária para escrever qual o maior valor: o primeiro ou o segundo (caso os valores sejam iguais, considere o segundo).

# Solicita dois valores ao usuário
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

# Condição ternária para determinar o maior valor (considera o segundo em caso de empate)

if v1 > v2:
    print("O Primeiro Valor escolhido foi {}, portanto foi o maior".format(v1))
elif v1 == v2:
    print("As regras determinaram se os numeros forem iguais considere o segundo Valor Maior.. :D ")
else: v1 < v2
print ("O segundo Número que é {}, é o menor Valor!".format(v2))
