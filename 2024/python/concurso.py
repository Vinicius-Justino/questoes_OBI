candidatos, minimo_aprovados = [int(n) for n in input().split(" ")]
notas = [int(nota) for nota in input().split(" ")]
print(sorted(notas)[candidatos - minimo_aprovados])