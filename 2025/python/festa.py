escola = int(input())
mercado = int(input())
loja = int(input())

distancia = 0
if abs(mercado - escola) < abs(loja - escola):
    distancia = abs(mercado - escola) + abs(loja - mercado) + abs(escola - loja)
    
else:
    distancia = abs(loja - escola) + abs(mercado - loja) + abs(escola - mercado)

print(distancia)