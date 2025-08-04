quantidade_linhas, quantidade_colunas = [int(n) for n in input().split(" ")]

tabuleiro = []
for linha in range(quantidade_linhas):
    tabuleiro.append([int(poder) for poder in input().split(" ")])

DIRECOES = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for heroi_y in range(quantidade_linhas):
    for heroi_x in range(quantidade_colunas):
        poder_heroi = tabuleiro[heroi_y][heroi_x]

        conquistados = [[heroi_y, heroi_x]]
        vizinhos = []
        for direcao in DIRECOES:
            vizinho_y = heroi_y + direcao[0]
            if not 0 <= vizinho_y < quantidade_linhas:
                continue

            vizinho_x = heroi_x + direcao[1]
            if not 0 <= vizinho_x < quantidade_colunas:
                continue

            vizinhos.append([vizinho_y, vizinho_x])
        
        while len(vizinhos) > 0:
            vizinho_mais_fraco = poder_heroi + 1
            indice_mais_fraco = 0

            for i in range(len(vizinhos)):
                posicao = vizinhos[i]
                if tabuleiro[posicao[0]][posicao[1]] < vizinho_mais_fraco:
                    vizinho_mais_fraco = tabuleiro[posicao[0]][posicao[1]]
                    indice_mais_fraco = i
            
            if vizinho_mais_fraco > poder_heroi:
                break

            poder_heroi += vizinho_mais_fraco

            posicao = vizinhos.pop(indice_mais_fraco)
            conquistados.append(posicao)
            for direcao in DIRECOES:
                vizinho_y = posicao[0] + direcao[0]
                if not 0 <= vizinho_y < quantidade_linhas:
                    continue

                vizinho_x = posicao[1] + direcao[1]
                if not 0 <= vizinho_x < quantidade_colunas:
                    continue
                
                if [vizinho_y, vizinho_x] in vizinhos:
                    continue
                if [vizinho_y, vizinho_x] in conquistados:
                    continue

                vizinhos.append([vizinho_y, vizinho_x])
    
        print(f"{poder_heroi}{'\n' if heroi_x == quantidade_colunas - 1 else ' '}", end="")
            
