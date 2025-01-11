# Laços de repetição = parte 2 = Capitulo 7 - Questão 4

'''Remove a instrução break e a instrução continue do laço de repetição abaixo:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
posicao = 0
while posicao < len(numeros):
posicao += 1
if posicao == 3:
continue
elif posicao == 6:
break
print(numeros[posicao-1])
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
posicao = 0
while posicao < 5: 
if posicao != 2:
print(numeros[posicao])
posicao +=1 '''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

posicao = 0

while posicao < len(numeros):
    posicao += 1

    # Verifica se a posição é 3, mas não usa continue
    if posicao == 3:
        # Se for 3, não imprime e simplesmente continua para a próxima iteração
        pass
    else:
        # Se não for 3, imprime o número
        print(numeros[posicao - 1])

# Para o segundo laço:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

posicao = 0

while posicao < 5:
    # Verifica se a posição é 2, mas não usa continue
    if posicao != 2:
        print(numeros[posicao])
    posicao += 1
