''' ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPAREOS MOSTRANDO NA TELA UMA MENSAGEM :
- O PRIMEIRO VALOR É MAIOR
- O SEGUNDO VALOR É MAIOR
- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS '''

num1 = int(input("Qual o Primeiro Valor: "))
num2 = int(input("Qual o Segundo Valor: "))


if num1>num2:
    print("O Primeiro numero que foi {} é maior".format(num1))
elif num1<num2:
    print("O Segundo numero que foi {} é maior". format(num2))
else:
    print("Não existe valor maior os numeros escolhidos foras {} e {} e são iguais".format(num1,num2))
