#  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessário para pinta-lá sabendo que cada litro de tinta pinta uma area de 2m2.

lp = float(input('Qual a Largura da Parede em m2: '))
ap = float(input('Qual a Altura da Parede em m2: '))

sp = lp * ap
tp = sp / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {} m2.'.format(lp,ap,sp))
print('E para pintar essa parede, você precisara de {:.3f}l de tinta.'.format(tp)) #com :.3f 3 casas depois da virgula