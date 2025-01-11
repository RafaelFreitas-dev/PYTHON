# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome = str(input('Em que cidade você nasceu: ')).strip() # eliminando os espaços se houver pelo usuario.
print (nome[:5].upper() == 'SANTO') # foi convertido para maiusculo por que se o usuario digitar bagunçado nao tem riscos de não funcionar :) 