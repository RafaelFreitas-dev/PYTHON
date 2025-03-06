#Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no intervalos de 1 entre 500.


soma = 0         # varialvel soma para contar todos os numeros
cont = 0         # variavel contadora para contar quantas vezes apareceu o nuemro solicitado
for c in range(1, 500, 2):
    if c % 3 == 0: 
        cont = cont + 1 # se quiser pode facilicar o codigo dessa forma " cont += 1 "
        soma = soma + c # se quiser pode facilicar o codigo dessa forma " soma += 1 "
print(" São ao todo {} numeros impares".format(conttot))
print("A soma de todos os {} numeros impares divisivel por 3 é {}.".format(cont, soma))