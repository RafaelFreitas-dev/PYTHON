# Faça um programa que solicite o nome completo do usuário e exiba somente o seu segundo nome/primeiro sobrenome.

# Solicita o nome completo do usuário
nome_completo = input("Digite o seu nome completo: ")

# Divide o nome completo em uma lista de palavras
nomediv = nome_completo.split()

# Verifica se o usuário digitou pelo menos dois nomes
if len(nomediv) > 1:
    segundo_nome = nomediv[1]
    print("Seu segundo nome (ou primeiro sobrenome) é: {}".format(segundo_nome))
else :

    print("Você digitou apenas um nome, sem sobrenome.")
