#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio. Indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep # importando só a função sleep

for contagem in range(10, 0, -1): # Quando printado a mesma contagem do laço de repitição ele ira contar.
    print(contagem)
    sleep(1) 
    
print("BUM! BUM! POOOW!")