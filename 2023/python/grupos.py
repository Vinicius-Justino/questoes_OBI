quantidade_estudantes, quantidade_pares_almejados, quantidade_pares_evitados = [int(n) for n in input().split(" ")]

pares_almejados = []
for i in range(quantidade_pares_almejados):
    pares_almejados.append([int(aluno) for aluno in input().split(" ")])

pares_evitados = []
for i in range(quantidade_pares_evitados):
    pares_evitados.append([int(aluno) for aluno in input().split(" ")])

for i in range(quantidade_estudantes // 3):
    trio = [int(aluno) for aluno in input().split(" ")]

    restricoes_violadas = []
    for par in pares_almejados:
        if par[0] in trio and par[1] in trio:
            restricoes_violadas.append(par.copy())
    
    for par in restricoes_violadas:
        pares_almejados.remove(par)
    
    restricoes_violadas = []
    for par in pares_evitados:
        if par[0] in trio and par[1] in trio:
            restricoes_violadas.append(par.copy())
    
    for par in restricoes_violadas:
        pares_evitados.remove(par)
    


print(len(pares_almejados) + quantidade_pares_evitados - len(pares_evitados))