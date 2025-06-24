input()
alturas = list(reversed([int(altura) for altura in input().split(" ")]))


maior_altura = alturas.pop(0)
alunos_colam = 0

for altura in alturas:
    if altura <= maior_altura:
        alunos_colam += 1
    else:
        maior_altura = altura

print(alunos_colam)