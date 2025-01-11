# Laços de repetição = parte 2 = Capitulo 7 - Questão 3

# Faça um programa que exiba um menu para o usuário selecionar uma das três opções:
# 1 - Olá mundo
#2 - Eu programo em Python
#3 - Laços de repetição
# O· programa deve solicitar ao usuário uma das 3 opções, caso o usuário digite um valor diferente das opções (1, 2 ou 3), o programa deve apresentar novamente o menu de opções até que uma delas seja escolhida. Por fim, o programa deve exibir uma mensagem diferente para cada opção.

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("Escolha uma das opções:")
    print("1 - Olá mundo")
    print("2 - Eu programo em Python")
    print("3 - Laços de repetição")

# Inicializando a variável de escolha
escolha = None

# Laço para solicitar uma opção válida
while escolha not in ['1', '2', '3']:
    exibir_menu()
    escolha = input("Digite sua opção (1, 2 ou 3): ")

# Exibindo a mensagem correspondente à escolha
if escolha == '1':
    print("Você escolheu: Olá mundo!")
elif escolha == '2':
    print("Você escolheu: Eu programo em Python!")
elif escolha == '3':
    print("Você escolheu: Laços de repetição!")
