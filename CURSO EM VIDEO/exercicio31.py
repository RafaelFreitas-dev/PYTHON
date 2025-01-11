# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem , cobrando R$0.50 por km para viagens até 200km e R$0.45 para viagens mais longas.

viagem = float(input("Qual a distancia da viagem: "))

if viagem <= 200:
    preco1 = viagem * 0.50
    print("Para uma viagem de {} km,O preço da passagem será de {:.2f} Reais".format(viagem, preco1))
else :
    preco2 = viagem * 0.45
    print("Para uma viagem de {} km,O preço da passagem será de {:.2f} Reais".format(viagem, preco2))
    
print("Companhia pé na Estrada deseja Boa viagem")