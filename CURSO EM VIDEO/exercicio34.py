# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
 
 
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Qual é o salário do Funcionario: "))


if sal <= 1250: 
   novo = sal * 1.15
else :
    novo = sal * 1.10
print("Seu aumento será de R${:.2f}, para R${:.2f}.".format(sal, novo))
    
