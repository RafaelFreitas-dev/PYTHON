#Média do Aluno

nome =str(input('Qual é o Nome do Aluno')) 
p1 = float(input('Qual Foi a Primemira Nota: '))
p2 = float(input('Qual foi a Segunda Nota: '))

media = (p1 + p2) / 2

print('A média entre ', p1 ,' e  ', p2 ,' Resultou na Média ', media)


# MODOS DIFERENTES DE FAZER A MESMA IMPRESÃO DE CONTEÚDO NA TELA
print('A media entre {} e {} Resultou na Média {:.1f}.'.format(p1, p2, media))


# A sigla :.1f  ponto flutuante e 1 casa após a virgula