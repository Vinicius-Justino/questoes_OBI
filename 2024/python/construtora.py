quantidade_predios = int(input())
antigas_alturas = [int(n) for n in input().split(" ")]
novas_alturas = antigas_alturas.copy()

predio_anterior, predio_atual = 0, 1
cont_fases = 0

for _ in range(quantidade_predios - 1):
    diferenca = antigas_alturas[predio_atual] - novas_alturas[predio_anterior]
    if diferenca < 0 and antigas_alturas[predio_atual] >= antigas_alturas[predio_anterior]:
        pass
    else:
        cont_fases += abs(diferenca)
    
    novas_alturas[predio_atual] = max(antigas_alturas[predio_atual], novas_alturas[predio_anterior])
    predio_anterior = predio_atual
    predio_atual += 1

print(cont_fases)
