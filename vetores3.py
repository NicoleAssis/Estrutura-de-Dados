lista1, lista2, lista3 = [], [], []

qtd = int(input("Digite a quantidade de números que deseja digitar: "))

for i in range(qtd):
    numero = int(input(f"Digite o {i + 1}° número da 1ª Lista: "))
    lista1.append(numero)

for i in range(qtd):
    numero = int(input(f"Digite o {i + 1}° número da 2ª Lista: "))
    lista2.append(numero)


for n, i in zip(lista1, lista2):
    soma = n + i
    print(soma)
    lista3.append(soma)

print("Lista com as somas:", lista3)


