# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME.abs

nome = str(input('Qual é o seu nome: ')).strip()
print('Seu nome tem Silva: {}'.format('SILVA' in nome.upper()))
