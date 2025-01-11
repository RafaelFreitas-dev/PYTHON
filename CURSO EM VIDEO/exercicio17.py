# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJASCENTE DE UM TRIANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.


''' co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjascente: '))

hip = (co**2+ca**2)**(1/2)

print('O valor digitado para cateto oposto foi {} e para o cateto adjascente foi {} onde o valor da hipotenusa será de {:.2f}'.format(co,ca,hip)) '''

# Outra forma de fazer essa atividade

''' import math
co1 = float(input('Qual é o comprimento do cateto oposto: '))
ca1 = float(input('Qual é o comprimento do cateto adjascente: '))

hi = math.hypot(co1,ca1)
print('O valor da hipotenusa é {:.2f}'.format(hi)) '''

# Ou como estamos usando só uma funcionalidade podemos fazer assim também para economizar memoria


from math import hypot
co1 = float(input('Qual é o comprimento do cateto oposto: '))
ca1 = float(input('Qual é o comprimento do cateto adjascente: '))
hi = hypot(co1,ca1)
print('O valor da hipotenusa é {:.2f}'.format(hi))