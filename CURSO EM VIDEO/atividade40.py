#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A MEDIA ATINGIDA

# --- MEDIA ABAIXO DE 5 = REPROVADO
# --- MEDIA ABAIXO DE  6.99 E ACIMA DE 5 = RECUPERAÇÃO
# --- MEDIA ACIMA DE 7 = APROVADO

n1 = float(input("Qual foi a sua Primeira Nota"))
n2 = float(input("Qual foi a sua Segunda Nota"))

res = (n1+n2) / 2

if res >= 7:
    print("tirando {} e {} sua nota final foi {}.".format(n1,n2,res))
    print("PARABÉNS VOCÊ FOI APROVADO")
    
elif res < 7 and res > 5:
    print("tirando {} e {} sua nota final foi {}.".format(n1,n2,res))
    print("VOCÊ ESTA DE RECUPERAÇÃO")
    
else:
    print("tirando {} e {} sua nota final foi {}.".format(n1,n2,res))
    print("VOCÊ ESTA REPROVADO")
    