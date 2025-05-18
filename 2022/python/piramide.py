dimensao_inicial = int(input())
dimensao_atual = dimensao_inicial

altura_nivel = 1
saidas = []
while dimensao_atual > 0:
    nivel_atual = f"{altura_nivel} " * dimensao_atual
    nivel_atual = nivel_atual[0 : len(nivel_atual) - 1]
    for i in range(0, dimensao_inicial - dimensao_atual, 2):
        altura_nivel_anterior = int(altura_nivel - (i / 2) - 1)
        nivel_atual = f"{altura_nivel_anterior} {nivel_atual} {altura_nivel_anterior}"
    
    print(nivel_atual)

    altura_nivel += 1
    dimensao_atual -= 2
    if (dimensao_atual >= 0):
        saidas.append(nivel_atual)

for saida in reversed(saidas):
    print(saida)