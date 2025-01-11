# Média do Aluno

n1 = float(input('Qual foi a sua Primeira Nota: '))
n2 = float(input('Qual foi a sua Segunda Nota: '))

media = (n1+n2) / 2

if (media>=7):
    print('Parabéns sua Média foi ', media ,' você foi aprovado(a). ')
    
elif (media<7) and (media >= 5):
    print('Sua Média final foi ', media ,' e ficou de Recuperação')
    
else:
    print('A sua Média foi ', media ,' E VOCÊ ESTÁ REPROVADO')