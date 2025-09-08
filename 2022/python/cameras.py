colunas, linhas, quantidade_cameras = [int(n) for n in input().split(" ")]
salao = [[0] * colunas for i in range(linhas)]

ORIENTACOES = {
    "N": [-1, 0],
    "L": [0, 1],
    "S": [1, 0],
    "O": [0, -1]
}

for camera in range(quantidade_cameras):
    coluna, linha, orientacao = input().split(" ")
    coluna = int(coluna) - 1
    linha = int(linha) - 1

    visao_camera = [linha, coluna]
    progressao = ORIENTACOES[orientacao]
    while 0 <= visao_camera[0] < linhas and 0 <= visao_camera[1] < colunas:
        salao[visao_camera[0]][visao_camera[1]] = -1
        visao_camera[0] += progressao[0]
        visao_camera[1] += progressao[1]

bordas_territorio = []
if salao[0][0] == 0:
    salao[0][0] = 1
    bordas_territorio.append([0, 0])

while salao[linhas - 1][colunas - 1] != 1:
    if len(bordas_territorio) == 0:
        break

    for i in range(len(bordas_territorio)):
        quadrado_atual = bordas_territorio.pop(0)

        for orientacao in ORIENTACOES.values():
            potencial_vizinho = [quadrado_atual[0] + orientacao[0], quadrado_atual[1] + orientacao[1]]
            if not (0 <= potencial_vizinho[0] < linhas and 0 <= potencial_vizinho[1] < colunas):
                continue
            elif salao[potencial_vizinho[0]][potencial_vizinho[1]] != 0:
                continue

            salao[potencial_vizinho[0]][potencial_vizinho[1]] = 1
            bordas_territorio.append(potencial_vizinho)

print("S" if salao[linhas - 1][colunas - 1] == 1 else "N")