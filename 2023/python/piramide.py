cubos = [int(peso) for peso in input().split(" ")]

peso_topo = max(cubos)
cubos.remove(peso_topo)
peso_total = sum(cubos)

piramide_balanceavel = False
for i in range(5):
    for j in range(i+1, 5):
        peso_andar2 = cubos[i] + cubos[j]
        peso_andar1 = peso_total - peso_andar2

        piramide_balanceavel = (peso_andar1 == peso_andar2 == peso_topo)
        if piramide_balanceavel:
            break
    
    if piramide_balanceavel:
        break

print("S" if piramide_balanceavel else "N")
