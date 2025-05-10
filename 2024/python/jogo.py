from copy import deepcopy

tamanho_matriz, geracoes = [int(n) for n in input().split(" ")]

presente = []
for i in range(tamanho_matriz):
    estado_linha = [int(estado) for estado in input()]
    presente.append(estado_linha)

futuro = deepcopy(presente)
for geracao in range(geracoes):
    for linha in range(tamanho_matriz):
        for coluna in range(tamanho_matriz):
            celula_viva = bool(presente[linha][coluna])
            vizinhos = 0

            for mod_linha in range(-1, 2):
                linha_vizinho = linha + mod_linha

                for mod_coluna in range(-1, 2):    
                    coluna_vizinho = coluna + mod_coluna
                    if not ((0 <= linha_vizinho < tamanho_matriz) and (0 <= coluna_vizinho < tamanho_matriz)):
                        continue
                    elif mod_linha == 0 and mod_coluna == 0:
                        continue

                    vizinhos += presente[linha_vizinho][coluna_vizinho]

            if (not celula_viva and vizinhos == 3) or (celula_viva and (vizinhos in [2, 3])):
                futuro[linha][coluna] = 1
            else:
                futuro[linha][coluna] = 0
            
    presente = deepcopy(futuro)

for linha in presente:
    print("".join([str(estado) for estado in linha]))
