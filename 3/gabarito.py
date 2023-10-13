n = int(input())
alunos = []
for i in range(n):
    nome, notas = input().split(' ', 1)
    notas = list(map(float, notas.split()))
    media = sum(notas) / 5
    alunos.append((nome, media))
for aluno in alunos:
    print(aluno[0], aluno[1])
