N = int(input())

matriz = []

for i in range(N):
    dados = input().split()
    nome = dados[0]
    nota1 = float(dados[1])
    nota2 = float(dados[2])
    matriz.append([nome, nota1, nota2])

print("Alunos aprovados:")
for aluno in matriz:
    media = (aluno[1] + aluno[2]) / 2
    if media >= 6.0:
        print(aluno[0])
