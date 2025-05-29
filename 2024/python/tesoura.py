passos = int(input())

tesouras_passo = 1
tinta_gasta = 0
for passo in range(1, passos + 1):
    if passo % 2 == 0:
        tesouras_passo *= 2
    
    tinta_gasta += 2 * tesouras_passo - 1

print(tinta_gasta % 1000000007)
