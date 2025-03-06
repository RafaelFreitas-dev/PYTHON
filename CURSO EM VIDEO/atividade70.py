#CRIR UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL MOSTRE:

# A) QUAL É O TOTAL GASTO NA COMPRA
# B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000.
# C) QUAL É O NOME DO PRODUTO MAIS BARATO.

print("=="*20)
print("LOJÃO SUPER BARATÃO")
print("=="*20)

soma = pro1000 = menor = cont = 0
barato = " "

while True:
    produto = str(input("Nome do Produto: ")).strip()
    preço = int(input("Preço: "))
    
    cont +=1 #o contador serve para contar todos os produtos inseridos
    
    # Questao A - total gasto
    soma = soma + preço
    
    # Questão B - Produtos acima de 1000 Reais
    if preço >= 1000:
        pro1000 += 1
        
    # Questão C - 
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]")).upper().strip()[0]
    if resp == "N":
        break
print("="*15,"Fim do programa", "="*15)
print(f"O total da compra foi de {soma:.2f} Reais.")
print(f"Foram {pro1000} produtos acima de 1000 reais")
print(f"O produto mais barato é {barato} e custa R$ {menor}.")
print("Acabou")