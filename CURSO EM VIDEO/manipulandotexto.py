# A MANIPULAÇÃO DE TEXTO e fatiamento

# TIRE AS ASPAS ''' E TESTE O PROGRAMA PARA MELHOR ENTENDIMENTO

#======================================================================================
# EXEMPLOS DE FUNCIONALIDADES DE FATIAMENTO DE STRINGS (CARACTERES)
#======================================================================================

'''frase = 'Curso em Video Python'
print(frase[9])'''
# APARECERÁ A LETRA V NA TELA

'''frase = 'Curso em Video Python'
print(frase[9:14])'''
# APARECERÁ AS LETRAS 'Video' NA TELA..
# OBS: AS LETRAS/NUMEROS NO INICIO (INICIO[9] : [14]FIM) COMEÇA CERTO MAIS NA LETRA FINAL SEMPRE IMPRIME ATÉ UMA ANTES QUE NO CASO IMPRIMIRA NA TELA ATÉ O NUMERO 13

'''frase = 'Curso em Video Python'
print(frase[9:21:2])'''
# Vou começar no 9 finalizar no 21 e o 2 indica que sera pulado de 2 em 2 casas... mostrando na tela VdoPto

'''frase = 'Curso em Video Python'
print(frase[:14])'''
# QUANDO NÃO SE INDICA NENHUM NUMERO ELE RECONHECE COMO ZERO NO INICIO E QUANDO NAO COLOCA NADA NO FIM (NO EXEMPLO SERIA NO NUMERO 14 ILUSTRADO ACIMA) MOSTRA ATÉ O FINAL DO TEXTO.

'''
INICIO = 0
FIM = 21
SALTO = 3
frase = 'Curso em Video Python'
print(frase[INICIO:FIM:SALTO])
'''
# FOI USADO COMO VARIAVÉL PARA MELHOR ENTENDIMENTO E FORTALECIMENTO DO CONHECIMENTO

#======================================================================================
# EXEMPLOS DE FUNCIONALIDADES DE ANALISE DE STRINGS (CARACTERES)
#======================================================================================

'''frase = 'Curso em Video Python'
print(len(frase))'''
# len função para mostra a quantidade de caracteres do texto.

'''frase = 'Curso em Video Python'
print(frase.count('o'))'''
# frase.count('o') função para contrar a quantidade de palavras o no texto

'''frase = 'Curso em Video Python'
print(frase.count('o',0,13))'''
# IRA FAZER A CONTAGEM DE LETRAS 'o' DO NUMERO 0 ATÉ O 12. LEMBRA QUE INDICA ATÉ O 13 MAIS ELE CONTA ATÉ O 12.

'''frase = 'Curso em Video Python'
print(frase.find('RAFAEL'))'''
# find = encontrar. .find é uma função que encontra a posição inicia que a palavra indicada inicio.
# QUANDO PASSA UM NUMERO OU LETRA QUE NÃO TEM NO TEXTO INDICADO RETORNARA -1 - INFORMANDO QUE NÃO EXISTE A PALAVRA PESQUISADA NO TEXTO.

'''frase = 'Curso em Video Python'
print('Curso' in frase)'''
# ESSA NÃO É UMA FUNÇÃO E SIM UM OPERADOR LOGICO... ELE CONFIRMA SE EXISTE A PALAVRA CURSO NA FRASE RETORNANDO TRUE(VERDADEIRO) OU FALSE (FALSO) NA TELA.

'''frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android'))'''
# A FUNÇÃO REPLACE ELA SUBSTITUI O TEXTO DA PALAVRA PYTHON POR ANDROID. é uma substituição secundaria.

'''frase = 'Curso em Video Python'
print(frase.upper())
print(frase.lower())'''
# função upper é um metodo deixando todos as letras MAIUSCULAS
# função lower deixa todos as letras MINUSCULAS

'''frase = 'Curso em Video Python'
print(frase.capitalize())'''
# A função capitalize deixa todas as letras MINUSCULAS e só a Primeira letra do texto fica MAIUSCULA.

'''frase = 'Curso em Video Python'
print(frase.title())'''
# a função title ela faz uma analise mais profunda das palavras e deixa todos os inicio de palavras com a letra MAIUSCULAS  e o restante MINUSCULOS == EXEMPO  === Curso Em Video Python

'''frase = '   Curso em Video Python   '
print(frase.strip()) # ELIMINA TODOS OS ESPAÇOS
print(frase.rstrip())  # ELIMINA SÓ OS ESPAÇOS DA DIREITA R(RIGTH)
print(frase.lstrip())  # ELIMINA SÓ OS ESPAÇOS DA ESQUERDA L(LIFT)'''

# frase.strip() essa função remove todos os espaços vazio de uma  palavra no INICIO E NO FIM.
# frase.rstrip() função r(rigth) remove todos os espaços vazio de uma  palavra a sua DIREITA
# frase.Lstrip() essa função l(lift) remove todos os espaços vazio de uma  palavra a sua ESQUERDA

#======================================================================================
# EXEMPLOS DE FUNCIONALIDADES DE DIVISÃO DE STRINGS (CARACTERES)
#======================================================================================

'''frase = '   Curso em Video Python   '
print(frase.split())'''
# a função split ele cria uma divisão entre as palavras, ele vai transforma uma string em uma lista exemplo ['Curso', 'em', 'Video', 'Python']

frase = '   Curso em Video Python   '
print('-'.join(frase))
# A função JOIN ele completa os espaços com a formatação que vc queira para separar as palavras em uma string.

 #DESAFIOS DOS EXERCICIOS 22 AO 27
