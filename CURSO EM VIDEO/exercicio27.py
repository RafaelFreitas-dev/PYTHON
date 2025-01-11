# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente:
# ex: Rafael de Souza Freitas
# Primeiro Nome: Rafael
# Último Nome: Freitas

nome = str(input("Qual é o seu Nome Completo:")).strip() # Eliminou todos os espaços
nome = nome.split() # Divindo o nome em listas

print("Muito Prazer em ti conhecer :) ")
print("Seu Primeiro nome é: {}".format(nome[0])) # Puxando a primeira Posição da lista que inicia com Zero
print("Seu Último Nome é: {}".format(nome[len(nome)-1]))

