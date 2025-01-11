idade = int(input('Qual a sua idade? '))

if (idade<11):
    print('CRIANÇA')
elif (idade>=12) and (idade<=18):
    print('Adolescente')
elif (idade>=19) and (idade<=24):
    print('JOVEM')
elif (idade>=25) and (idade<=40):
    print('ADULTO')
elif (idade>=41) and (idade<=60):
    print('MÉDIA IDADE')
else:
    print('IDOSO')