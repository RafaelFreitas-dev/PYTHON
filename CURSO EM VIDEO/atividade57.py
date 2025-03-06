# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F" caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MF":
        sexo = str(input("Dados Invalidos. Por favor, informe seu sexo: ")).strip().upper()[0]
        
print("Sexo {} Registrado com Sucesso.".format(sexo))