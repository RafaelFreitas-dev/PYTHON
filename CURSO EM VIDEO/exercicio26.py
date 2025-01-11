# Faça um programa que leia uma frase e mostre:

# Quantas Vezes aparece a letra 'A'
# Em que Posição ela aparece a primeira vez
# Em que posição aparece a ultima vez


frase = str(input("Escreva uma frase: ")).upper().strip() #upper -- convertendo as resposta em letras maiusculas
                                                          #strip -- Eliminiar os espaços.  

print('A letra A aparece {} vezes'.format(frase.count('A'))) # count -- fazendo a contagem de letras A
print('A letra A apareceu a primeira vez na posição {}'.format(frase.find('A') + 1)) # find -- Encontrando a primeira posição da letra A
print('A letra A apareceu a ultima vez na posição {}'.format(frase.rfind('A') + 1)) # Rfind -- contagem da direita para a esquerda