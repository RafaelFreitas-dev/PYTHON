''' ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER QUAL SERA A BASE A BASE DE CONVERSÃO:
- 1 PARA BINARIO 
- 2 PARA OCTAL
- 3 PARA HEXADECIMAL'''

num = int(input("Digite um número: "))
print('''Escolha umas das palavras para conversão:
      [ 1 ] Converter para Binario
      [ 2 ] Converter para Octal
      [ 3 ] Converter para Hexadecimal''')
opção = int(input("Escolha o Numero para Conversão: "))

if opção == 1:
    print(" Seu numero escolhido foi {} e convertido para binario é {}.".format(num, bin(num)[2:])) 
    #  [2:]Foi usado o fatiamento de strings para eliminar as letras na posição 0 e 1 e iniciar na posição 2 até o fim.
elif opção == 2:
    print(" Seu numero escolhido foi {} e convertido para Octal é {}.".format(num, oct(num)[2:]))
elif opção == 3:
    print(" Seu numero escolhido foi {} e convertido para Hexadecimal é {}.".format(num, hex(num)[2:]))
else:
    print(" # ERRO # DIGITE UM NUMERO VALIDO!!! " ) 
    