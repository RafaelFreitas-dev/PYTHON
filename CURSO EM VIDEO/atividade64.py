# Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles, (desconsiderando o flag).


cont = 0    # cont é para contar a quantidade de numeros que foram digitados
s=0         # s contar os valores digitados
print("=-"*10)
print("TRATANDO VARIOS VALORES")
print("=-"*10)
n = int(input("Digite um número (999 para o programa): "))
while n != 999:
    cont = cont + 1
    s= s+n
    n = int(input("Digite um número (999 para o programa): "))
print("foram digitados {} numeros, e o total é {}.".format(cont,s))
print("Volte sempre.")
    

