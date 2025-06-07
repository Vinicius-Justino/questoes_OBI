coordenadas_valor_apagado = [0, 0]
menor_soma = 0
maior_soma = 0
for i in range(int(input())):
    linha = [int(n) for n in input().split(" ")]

    if 0 in linha:
        coordenadas_valor_apagado = [i + 1, linha.index(0) + 1]
    
    soma_linha = sum(linha)
    if i == 0:
        menor_soma = soma_linha
        maior_soma = soma_linha
    elif soma_linha < menor_soma:
        menor_soma = soma_linha
    elif soma_linha > maior_soma:
        maior_soma = soma_linha

valor_apagado = maior_soma - menor_soma

print(f"{valor_apagado}\n{coordenadas_valor_apagado[0]}\n{coordenadas_valor_apagado[1]}")