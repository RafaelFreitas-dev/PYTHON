# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO: 

''' import math
ang = float(input('Digite o ângulo que você deseja : '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan)) '''


# também como os exercicios anteriores podemos fazer com importações unicas

from math import radians, sin, cos,tan
ang = float(input('Digite o ângulo que você deseja : '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan))
