lista = []
maior = 0

qtd = int(input("Digite a quantidade de números que deseja digitar:"))

for i in range(qtd):
    numero = int(input(f"Digite o { i + 1 } ° número: "))
    lista.append(numero)

for numero in lista:
    if numero % 2 == 0:
        print (numero)

