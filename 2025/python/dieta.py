quantidade_refeicoes, max_calorias = [int(n) for n in input().split(" ")]

calorias_consumidas = 0
for lasanha in range(quantidade_refeicoes):
    proteina, gordura, carboidrato = [int(n) for n in input().split(" ")]

    calorias_consumidas += 4 * proteina + 9 * gordura + 4 * carboidrato

print(max_calorias - calorias_consumidas)