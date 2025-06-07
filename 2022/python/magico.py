coordenadas_incognita = [0, 0]
soma_verdadeira = 0
soma_defazada = 0

for i in range(int(input())):
    linha = [int(n) for n in input().split(" ")]

    if 0 in linha:
        soma_defazada = sum(linha)
        coordenadas_incognita = [i + 1, linha.index(0) + 1]
    else:
        soma_verdadeira = sum(linha)

valor_incognita = soma_verdadeira - soma_defazada

print(valor_incognita)
print(coordenadas_incognita[0])
print(coordenadas_incognita[1])