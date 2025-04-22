N = int(input())

lucro_baixo = 0
lucro_medio = 0
lucro_alto = 0
total_compra = 0
total_venda = 0
lucro_total = 0

for i in range(N):
    dados = input().split()
    nome = dados[0]
    preco_compra = float(dados[1])
    preco_venda = float(dados[2])
    
    lucro = preco_venda - preco_compra
    percentual_lucro = (lucro / preco_compra) * 100
    
    total_compra += preco_compra
    total_venda += preco_venda
    lucro_total += lucro

    if percentual_lucro < 10:
        lucro_baixo += 1
    elif 10 <= percentual_lucro <= 20:
        lucro_medio += 1
    else:
        lucro_alto += 1

print(f"Lucro abaixo de 10%: {lucro_baixo}")
print(f"Lucro entre 10% e 20%: {lucro_medio}")
print(f"Lucro acima de 20%: {lucro_alto}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
