# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre.

# A média de idade do Grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

#variaveis somando a idade
somaidade = 0
mediaidade= 0

# Variaveis mostrando o homem mais velho
nomevelho = " "
maioridade = 0

# variaveis mulheres menores de 20 anos
totmenor20 = 0


for p in range(1,5):
    print("{} {} PESSOA {}".format("="*5, p, "="*5))
    nome = str(input("\033[32m Nome: \033[m ")).strip()
    idade = int(input("\033[33m Idade: \033[m"))
    sexo = str(input("\033[34mSexo [M / F]: \033[m")).strip()
    
    # somando a idade do grupo
    somaidade = somaidade + idade                  # Somando as idades.
    mediaidade = somaidade / 4          # dividindo pela quantidade estabelecida.
    
    # Mostrando qual é o homem mais velho
    if p == 1 and sexo in "Mm":
        maioridade = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridade:
        maioridade  = idade
        nomevelho = nome
    
    # Mostrando a quantidade de mulheres menos de 20 anos.
    if sexo in "Ff" and idade < 20:
        totmenor20 += 1
        
print("\033[1;32m-------- RESULTADO --------\033[m")
print(" \033[34m---------------------------\033[m")
print("a media de idade do grupo é \033[32m{}\033[m.".format(mediaidade)) 
print("O homem mais velho tem \033[32m{}\033[m anos e se chama {}.".format(maioridade, nomevelho))
print("Ao todo são \033[32m{}\033[m mulheres com menos de 20 anos.".format(totmenor20))
print("\033[34m ---------------------------\033[m")
    