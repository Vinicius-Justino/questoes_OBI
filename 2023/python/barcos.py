quantidade_ilhas, quantidade_barcos = [int(n) for n in input().split(" ")]

barcos = {}
for barco in range(quantidade_barcos):
    ilha1, ilha2, custo = [int(n) for n in input().split(" ")]
    custo = int(custo)

    try:
        for i in range(len(barcos[ilha1])):
            if custo >= barcos[ilha1][i][1]:
                barcos[ilha1].insert(i, [ilha2, custo])
            elif i == len(barcos[ilha1]) - 1:
                barcos[ilha1].append([ilha2, custo])
    except KeyError:
        barcos[ilha1] = [[ilha2, custo]]
    
    try:
        for i in range(len(barcos[ilha2])):
            if custo >= barcos[ilha2][i][1]:
                barcos[ilha2].insert(i, [ilha1, custo])
            elif i == len(barcos[ilha2]) - 1:
                barcos[ilha2].append([ilha1, custo])
    except KeyError:
        barcos[ilha2] = [[ilha1, custo]]

def encontra_melhor_caminho(caminho, destino):
    ilha_atual = caminho[-1]
    if ilha_atual == destino:
        return True
    
    for barco in barcos[ilha_atual]:
        proxima_ilha = barco[0]
        if proxima_ilha in caminho:
            continue

        caminho.append(proxima_ilha)
        if encontra_melhor_caminho(caminho, destino):
            return True
        
        caminho.pop(-1)
    
    return False


for consulta in range(int(input())):
    origem, destino = [int(n) for n in input().split(" ")]

    caminho = [origem]
    encontra_melhor_caminho(caminho, destino)
    
    gargalo = 0
    for i in range(len(caminho) - 1):
        ilha_atual = caminho[i]
        proxima_ilha = caminho[i + 1]

        for barco in barcos[ilha_atual]:
            if barco[0] == proxima_ilha:
                gargalo = min(gargalo, barco[1]) if i > 0 else barco[1]
    
    print(gargalo)