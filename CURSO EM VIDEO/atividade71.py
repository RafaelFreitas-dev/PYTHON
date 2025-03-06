#CRIE UM PROGRAMA QUE SIMULE UM FUNCIONAMENTO DE UM CAIXA ELETRONICO. NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉLULAS DE CADA VALOR SERÃO ENTREGUES.

# OBS: CONSIDERE QUE O CAIXA POSSUI CÉLULAS DE R$100, R$50, R$20, R$10, R$5 E R$2.

print("=="*20)
print("{:^40}".format("BANCO FREITAS"))
print("=="*20)
valor = int(input("Que valor você quer sacar: R$ "))
total = valor
ced = 100
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"O total de {totalced} cédulas de R${ced}")
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 0
        totalced = 0
        if ced == 0:
            break