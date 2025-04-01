pessoas = {}

qtd = int(input("Digite a quantiade de pessoas: "))

for _ in range(qtd):
    nome = input("Digite o nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas[nome] = idade


mais_velho = max(pessoas, key = pessoas.get)

print(f"Pessoa mais velha: {mais_velho}")