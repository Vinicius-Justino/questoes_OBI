gols_paulo = [int(n) for n in input().split(" ")]
gols_camila = [int(n) for n in input().split(" ")]

ordem_gols = []
for i in range(gols_paulo.pop(0) + gols_camila.pop(0)):
    if len(gols_paulo) == 0:
        ordem_gols.append("C")
        gols_camila.pop(0)
    elif len(gols_camila) == 0:
        ordem_gols.append("P")
        gols_paulo.pop(0)
    elif gols_paulo[0] < gols_camila[0]:
        ordem_gols.append("P")
        gols_paulo.pop(0)
    else:
        ordem_gols.append("C")
        gols_camila.pop(0)

placar = {"P": 0, "C": 0}
print("0 0")
for marcador in ordem_gols:
    placar[marcador] += 1
    print(f"{placar['P']} {placar['C']}")
