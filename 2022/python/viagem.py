custo_maximo, quantidade_ilhas, quantidade_navios = [int(n) for n in input().split(" ")]

navios = {}
for navio in range(quantidade_navios):
    ilha1, ilha2, tempo, custo = [int(n) for n in input().split(" ")]

    try:
        for i in range(len(navios[ilha1])):
            if tempo < navios[ilha1][i][1]:
                navios[ilha1].insert(i, [ilha2, tempo, custo])
            elif i == len(navios[ilha1]) - 1:
                navios[ilha1].append([ilha2, tempo, custo])
    except KeyError:
        navios[ilha1] = [[ilha2, tempo, custo]]
    
    try:
        for i in range(len(navios[ilha2])):
            if tempo < navios[ilha2][i][1]:
                navios[ilha2].insert(i, [ilha1, tempo, custo])
            elif i == len(navios[ilha2]) - 1:
                navios[ilha2].append([ilha1, tempo, custo])
    except KeyError:
        navios[ilha2] = [[ilha1, tempo, custo]]

tempo_total = 0
menor_tempo = -1
custo_total = 0
origem, destino = [int(n) for n in input().split(" ")]
caminho = [origem]
def encontra_melhor_caminho():
    global caminho, destino, tempo_total, menor_tempo, custo_total
    ilha_atual = caminho[-1]

    if custo_total > custo_maximo:
        return
    if ilha_atual == destino:
        menor_tempo = min(menor_tempo, tempo_total) if menor_tempo != -1 else tempo_total
        return

    for navio in navios[ilha_atual]:
        if navio[0] in caminho:
            continue

        caminho.append(navio[0])
        tempo_total += navio[1]
        custo_total += navio[2]
        
        encontra_melhor_caminho()
        
        caminho.pop(-1)
        tempo_total -= navio[1]
        custo_total -= navio[2]

encontra_melhor_caminho()
print(menor_tempo)