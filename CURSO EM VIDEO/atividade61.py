# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, Mostrando os 10 primeiros termos da progresão usando a estrutura while


print("\033[33mGERADOR DE PA \033[m")

print("-="*10)
termo = int(input("Primeiro Termo: "))
razão = int(input("Razão da Pa: "))
cont = 1
while cont <= 10:
    print(termo,"=> ", end ="" )
    termo = termo + razão
    cont += 1
print("\033[31mFIM\033[m")
    
    
