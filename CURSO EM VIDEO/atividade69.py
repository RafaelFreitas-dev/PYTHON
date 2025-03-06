#CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR. NO FINAL, MOSTRE

# A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS
# B) QUANTOS HOMENS FORAM CADASTRADOS.
# C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.

print("=="*20)
print("CADASTRE UMA PESSOA ")
print("=="*20)

total = homem = mulher = 0

while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    
    if idade >=18:
        total = total + 1
    if sexo == "M":
        homem = homem + 1
    if sexo == "F" and idade < 20:
        mulher = mulher + 1
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar: [S/N] ")).upper().strip()[0]
    if resp == "N":
        break
print(f"Foram digitadas {total} pessoas maior de 18 anos.")
print(f"Cadastraram {homem} homens.")
print(f"São ao todo {mulher} mulheres menos de 20 anos.")
