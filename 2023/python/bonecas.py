quantidade_bonecas, quantidade_trios = [int(n) for n in input().split(" ")]
tamanhos = sorted([int(n) for n in input().split()], reverse=True)

IMPOSSIVEL = (tamanhos[0] - tamanhos[-1])**2 * quantidade_trios
melhores_agrupamentos = []
for _ in range(3):
    melhores_agrupamentos.append([IMPOSSIVEL] * quantidade_trios)
    melhores_agrupamentos[-1].insert(0, 0)

for boneca in range(3, quantidade_bonecas+1):
    melhores_agrupamentos.append([0])
    
    for trios_formados in range(1, quantidade_trios+1):
        if 3*trios_formados > boneca:
            melhores_agrupamentos[boneca].append(IMPOSSIVEL)
            continue

        melhores_agrupamentos[boneca].append(min(
            melhores_agrupamentos[boneca-1][trios_formados],
            melhores_agrupamentos[boneca-2][trios_formados-1] + (tamanhos[boneca-2] - tamanhos[boneca-1])**2
        ))

print(melhores_agrupamentos[quantidade_bonecas][quantidade_trios])
