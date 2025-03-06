# Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:

# Equilatero: todos os lados iguais
# Isósceles: Dois lados Iguais
# Escaleno:  Todos os Lados diferentes 

r1 = float(input("Qual é a Primeira reta: "))
r2 = float(input("Qual é a segunda reta: "))
r3 = float(input("Qual é a Terceira reta: "))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("As Retas acima PODEM formar um triangulo", end=" ")
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
    print("As Retas Acima NÃO PODEM formar um triangulo")