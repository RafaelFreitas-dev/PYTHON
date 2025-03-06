#escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
# 0->1->1->2->3->5->8->13->

from time import sleep
print("-="*10)
print("\033[32mSequencia de fibonacci\033[m")
print("-="*10)
termo = int(input("Quantos termos você quer mostrar:"))
t1=0
t2=1
print("{} -> {}".format(t1,t2),end="")
cont = 3

while cont <= termo:
    t3 = t1+t2
    print(" -> {}".format(t3), end="")
    cont += 1
    t1=t2
    t2=t3
sleep(2)
print()
print("FIM...")