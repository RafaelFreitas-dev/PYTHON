# Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]  # fatiamento de palavras... O -1 indica de trás para frente segui o fatiamento[0:0:-1].

'''for c in range(len(junto) -1, -1, -1):''' #foi feito com for
'''inverso = inverso + junto[c]''' # inverso += junto[c]

print("O inverno de \033[33m {} \033[m é \033[32m{}\033[m".format(junto, inverso))
    
if inverso == junto:
    print("\033[34m Temos um Palíndromo \033[m")
    
else:
    print("\033[31m A frase digitada Não é um Palíndromo \033[m")
    