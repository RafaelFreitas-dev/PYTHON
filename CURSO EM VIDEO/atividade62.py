# Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar o termo 0.


print("\033[35mGERADOR DE PA \033[m")

print("-="*10)
termo = int(input("Primeiro Termo: "))
razão = int(input("Razão da Pa: "))
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo,"=> ", end ="" )
        termo = termo + razão
        cont += 1
    print("\033[32mPAUSA...\033[m")
    mais = int(input("Quantos termos você quer mostrar a mais: "))
print("Progressão finalizadas com \033[32m{}\033[m termos mostrados".format(total))
