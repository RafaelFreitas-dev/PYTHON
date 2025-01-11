# DESCREVA UM PROGRAMA QUE LEIA O COMPRIMENO DE 3 RETAS E DIGA AO USUARIO SE ELA PODE OU NAO FORMAR UM TRIANGULO

r1 = float(input("Qual é a Primeira reta: "))
r2 = float(input("Qual é a segunda reta: "))
r3 = float(input("Qual é a Terceira reta: "))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("As Retas acima PODEM formar um triangulo")
else:
    print("As Retas Acima NÃO PODEM formar um triangulo")