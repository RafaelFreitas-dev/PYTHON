# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input('Distancia em Metros: '))

km = medida / 1000
hect = medida / 100
dam = medida / 10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000


print(km,' KILOMETRO')
print(hect,' HECT')
print(dam,' DAM')
print(m,' METROS')
print(dm,' DECIMETRO')
print(cm,' CENTIMETRO',)
print(mm,'MILIMETRO')