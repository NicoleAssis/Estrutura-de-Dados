alturas = []
mulheres = []
num_homens = 0

qtd = int(input("Digite a quantidade de pessoas: "))

for _ in range(qtd):
    altura = float(input("Digite a altura da pessoa (em metros): "))
    sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()

    alturas.append(altura)

    if sexo == "F":
        mulheres.append(altura)
    elif sexo == "M":
        num_homens += 1

maior_altura = max(alturas)
menor_altura = min(alturas)
media_altura_mulheres = sum(mulheres) / len(mulheres) if mulheres else 0

print(f"\nMaior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura das mulheres: {media_altura_mulheres:.2f} m")
print(f"Número de homens: {num_homens}")
