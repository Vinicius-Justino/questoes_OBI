from math import ceil

chao, teto = int(input()), int(input())

raiz = ceil(chao**(1/6))

cont_raizes = 0
while chao <= raiz**6 <= teto:
    cont_raizes += 1
    raiz += 1

print(cont_raizes)