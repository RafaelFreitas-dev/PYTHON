# Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custa 7,00 reias por km acima do limite.

v = float(input("Qual a velocidade do Carro: "))

if v > 80:
    print("Você foi MULTADO.")
    multa = (v-80) * 7
    print("Sua velocidade atual foi {:.0f} km, numa via que o permitido é 80km, portanto você pagara {:.2f} Reais.".format(v, multa))
print("Tenha um Bom Dia, dirija com segurança.")