# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:

# ATÉ 9 ANOS : MIRIM
# ATÉ 14 ANOS : INFANTIL
# ATÉ 19 ANOS : jUNIOR
# ATÉ 25 ANOS : SENIOR
# ACIMA : MASTER

from datetime import date
atual = date.today().year
nasc = int(input("Em que ano você nasceu: "))
idade = atual - nasc

print("O atleta tem {} anos.".format(idade))
if idade <= 9 :
    print("CLASSIFICAÇÃO: MIRIM")
    
elif idade <= 14 :
    print("CLASSIFICAÇÃO: INFANTIL")
    
elif idade <= 19 :
    print("CLASSIFICAÇÃO: JUNIOR")
    
elif idade <= 25 :
    print("CLASSIFICAÇÃO: SENIOR")
    
else:
    print("CLASSIFICAÇÃO: MASTER")