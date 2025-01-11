# CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA

'''import math
num = float(input('Digite um Número: '))
res = math.floor(num)

print('O valor digitado foi {} e a sua porção inteira arredondando para menos é {} e arredondando para mais é {}'.format(num, res, math.ceil(num))) '''


# ESSA É A OUTRA FORMA DE FAZER (FAÇA SEUS TESTES TAMBÉM)


'''from math import floor, ceil
n1 = float(input('Digite um Número: '))
resul = floor(n1)
print('O valor digitado foi {} e a sua porção inteira arredondando para menos é {} e arredondando para mais é {}'.format(n1, resul, ceil(n1)))'''

# Conseguimos fazer essa atividade sem importar bibliotecas também usando a tag int -> inteira

n2 = float(input('Digite um Número: '))
print(' O valor digitado foi {} e a sua porção inteira é {}'.format(n2, int(n2)))
