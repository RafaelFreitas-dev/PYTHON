# importa todos os produtos ou todas as funcionalidades de uma biblioteca usa-se a seguinte sintaxe.
 
#import math ===== Math é UMA BIBLIOTECA DE MATEMATICA COM CARACTERES ESPECIAIS.

# Essa outra forma é para importar um único produto ou funcionalidade de qualquer biblioteca e se precisar importar mais de um item se usa a sintaxe separando as funcionalidades com virgulas.

# FROM MATH IMPORT SQRS ===== (UMA UNICA FUNCIONALIDADE)   
# FROM MATH IMPORT SQRS, CEIL ====== (DUAS OU MAIS FUNCIONALIDADES)

# FUNCIONALIDADES DA MATH. 

# CEIL - Faz arredondamento para cima
# FLOOR - Faz o arredondamento para baixo
# TRUNC - Truncar um numero sem fazer arredondamento ele simplesmente elimina da virgula para frente
# POW - Potencia vai funcionar de forma semelhante aos 2 ** 'asterisco'.
# SQRT - Serve para calcular RAIZ QUADRADA 
# FACTORIAL - faz Calculos fatorial 


#import math # importando todas as funcionalidades
#num = int(input('Digite um Número: '))
#raiz = math.sqrt(num)
#print('A Raiz de {} é igual a {:.2f}'.format(num, raiz))


#from math import sqrt  # importando uma unica funcionalidade
#num = int(input('Digite um Número: '))
#raiz = sqrt(num) # Quando só uma funcionalidade remove o math.
#print('A Raiz de {} é igual a {:.2f}'.format(num, raiz))

import random
num = random.random()
print(num)