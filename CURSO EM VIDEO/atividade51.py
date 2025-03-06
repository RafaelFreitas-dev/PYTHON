# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros numeros dessa prograssão.

print("="*30)
print(" 10 TERMOS DE UMA PA")
print("="*30)

termo = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = termo + (10)* razão  # para mostrar 10 termos independente dos numeros escolhidos pelo usuario.

for c in range(termo, decimo, razão):
    print(c,"->", end=" ")
print("Acabou.")