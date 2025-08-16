pontuacoes = []
for pontuacao in range(5):
    pontuacoes.append(int(input()))

pontos_trofeu = max(pontuacoes)
cont_trofeus = 0
while pontos_trofeu in pontuacoes:
    cont_trofeus += 1
    pontuacoes.remove(pontos_trofeu)

cont_placas = 0
try:
    pontos_placa = max(pontuacoes)
    while pontos_placa in pontuacoes:
        cont_placas += 1
        pontuacoes.remove(pontos_placa)
except:
    pass

print(f"{cont_trofeus} {cont_placas}")