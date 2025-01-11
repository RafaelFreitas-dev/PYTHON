# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome dos escolhidos:

''' import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido)) '''

# Outra forma de fazer com uma unica funcionalidade

from random import choice

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1,n2,n3,n4]
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))