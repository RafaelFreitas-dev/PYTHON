# DESENVOLVA UM PROGRAMA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS DE ACORDO COM A TABELA ABAIXO.

# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 E 25: PESO IDEAL
# ENTRE 25 ATÉ 30: SOBREPESO
# ENTRE 30 ATÉ 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MÓRBIDA

peso = float(input("Qual o seu peso: Kg "))
altura = float(input("Qual a sua Altura: M "))

imc = peso / (altura ** 2)

print("De acordo com seu peso de {} kg e sua altura de {} metros, seu IMC É {:.2f} .".format(peso,altura, imc), end=" ")

if imc <= 18.5:
    print("ABAIXO DO PESO")

elif imc <= 25:
    print("PESO IDEAL")

elif imc <= 30:
    print("SOBREPESO")
    
elif imc <= 40:
    print("OBESIDADE")
    
else :
    print("OBESIDADE MÓRBIDA")