N = int(input())

valores = []
for i in range(N):
    numero = int(input())
    valores.append(numero)

pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

if len(pares) > 0:
    media_pares = sum(pares) / len(pares)
    print(f"{media_pares:.1f}")
else:
    print(0)
