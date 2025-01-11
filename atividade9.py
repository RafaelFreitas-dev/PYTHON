# Faça um programa que solicite a idade do usuário, verifique se o texto informado só contém números. Caso contenha somente números exiba a mensagem: "Você tem {idade digitada} anos.", caso contrário exiba a mensagem: "Você digitou uma idade inválida".

# Solicita a idade do usuário
idade = input("Digite a sua idade: ")

# Verifica se a entrada contém apenas números
if idade.isdigit():
    print("Você tem {} anos.".format(idade))
else:
    print("Você digitou uma idade inválida.")
