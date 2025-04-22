
N = int(input(" "))

valores = []

for i in range(N):
    numero = float(input())
    valores.append(numero)

# Cálculo da média
soma = 0
for valor in valores:
    soma += valor

media = soma / N


print(media)

for valor in valores:
    if valor < media:
        print(f"{valor:.1f}")
