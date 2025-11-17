quantidade_maneiras = int(input())
tamanhos_agrupamentos = [1, 2, 3]

maneiras_recolher = [1]

quantidade_bolas = 0
while maneiras_recolher[-1] < quantidade_maneiras:
    quantidade_bolas += 1
    maneiras_recolher.append(0)
    for tamanho_agrupamento in tamanhos_agrupamentos:
        if tamanho_agrupamento > quantidade_bolas:
            continue

        maneiras_recolher[quantidade_bolas] += maneiras_recolher[quantidade_bolas - tamanho_agrupamento]

print(f"({quantidade_bolas-1}: {maneiras_recolher[-2]}) <= ({quantidade_bolas if maneiras_recolher[-1] == quantidade_maneiras else '?'}: {quantidade_maneiras}) <= ({quantidade_bolas}: {maneiras_recolher[-1]})")