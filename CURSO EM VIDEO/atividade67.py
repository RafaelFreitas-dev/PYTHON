# Faça um programa que mostre uma tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário. O programa sera interrompido quando o Solicitado for negativo.
while True:
    num = int(input("Quer ver a tabuada de qual valor: "))
    if num < 0:
        break
    valor = int(input("Até qual valor: "))
    print("-"*20)
    for c in range(1, valor+1):
        print(f"{num} x {c} = {num*c}")
    print("-"*20)
print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!")       
    

    
