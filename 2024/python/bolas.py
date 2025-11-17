total_bolas = int(input())
tamanhos_agrupamentos = [1, 2, 3]

maneiras_recolher = [0] * (total_bolas+1)
maneiras_recolher[0] = 1
for quantidade_bolas in range(1, total_bolas+1):
    for tamanho_agrupamento in tamanhos_agrupamentos:
        if tamanho_agrupamento > quantidade_bolas:
            continue

        maneiras_recolher[quantidade_bolas] += maneiras_recolher[quantidade_bolas - tamanho_agrupamento]

print(maneiras_recolher[total_bolas])