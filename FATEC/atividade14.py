# Capitulo 5 - Questão 4

# Faça um programa que inicialize uma lista vazia e a preencha com 5 nomes diferentes digitados pelo usuário, depois disso solicite um número de 0 até 4 e remova o elemento desta posição.

nomes = []

for i in range(5):
    nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(nome)

print("Lista de nomes:", nomes)

# Solicita um número de 0 a 4 para remover o elemento na posição correspondente
remover = int(input("Digite um número de 0 a 4 para remover o nome nessa posição: "))

# Verifica se o índice está dentro do intervalo válido
if 0 <= remover < len(nomes):
    removed_nome = nomes.pop(remover)
    print(f"Nome removido: {removed_nome}")
else:
    print("Índice inválido. Por favor, digite um número entre 0 e 4.")

# Exibe a lista atualizada
print("Lista de nomes atualizada:", nomes)

