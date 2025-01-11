# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

# O NOME COM TODAS AS LETRAS MAIÚSCULAS
# O NOME COM TODAS AS LETRAS MINÚSCULAS
# QUANTAS LETRAS AO TODO (SEM ESPAÇOS ESPAÇOS)
# QUANTAS LETRAS TEM O PRIMEIRO NOME


nome = str(input('Qual é o seu Nome Completo ')).strip()
print(nome)
print('Analisando seu nome...')

print('Seu nome em MAIÚSCULO é : ', nome.upper())
print('Seu nome em MINÚSCULO é: ', nome.lower())
print('Seu nome tem {} Letras.'.format(len(nome) - nome.count(" ")))

# QUANTAS LETRAS TEM O PRIMEIRO NOME
# print("Seu primeiro nome {} Letras".format(nome.find(" ")))

# Outra forma de Fazer essa ultima pergunta é atraves do split(), criando a divisão entre as plavras e mostrando através do len()
listar = nome.split()
print("Seu primeiro nome é {} e tem {} Letras.".format(listar[0], len(listar[0])))