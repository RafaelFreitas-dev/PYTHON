# desenvolva um programa que leia 6 numeros inteiros e mostre a soma daqueles que apenas forem pares. se o valor digitado for impar, desconsidere.
soma = 0
contp = 0
contn = 0
for c in range(1,7):
    num = int(input("Digite o {} numero: ".format(c)))
    
    if num % 2 == 0:
        soma = soma + num
        contp = contp + 1
    else:
        contn = contn + 1
    
print("Foram digitados {} numeros Pares.".format(contp))
'''print("Foram digitados {} numeros Impares.".format(contn))''' # Jáz fiz os contadores de impar e pares 

print("A soma de dos numeros pares é {}".format(soma))