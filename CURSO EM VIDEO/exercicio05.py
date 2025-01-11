n = int(input('Digite um Número: '))

ant = n - 1
suce = n + 1

print('Analisando o valor {}, Seu antecessor é {} e o sucessor é {}.'.format(n,ant,suce))


#Existe também outra forma de criar esse exercicio, eliminando as variaveis ant e suce, para ocupar menos espaço na memoria do programa. pórem se for preciso utilizar futuramente esta variavel vale mais a pena criar para evitar futuros trabalhos a mais.

# n = int(input('Digite um Número: '))
# print('Analisando o valor {}, Seu antecessor é {} e o sucessor é {}.'.format(n,(n-1),(n+1)))