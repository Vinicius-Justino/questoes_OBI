quantidade_nobres = int(input())
chefes = [int(n) for n in input().split(" ")]
chefes.insert(0, 0)

for _ in range(int(input())):
    operacao = [int(n) for n in input().split(" ")]

    if operacao[0] == 1:
        subordinado = operacao[1]
        niveis_acima = operacao[2]
        chefe = chefes[subordinado - 1]
        for _ in range(niveis_acima - 1):
            chefe = chefes[chefe - 1]
        
        print(chefe)
        continue

    novo_chefe = operacao[1]
    subordinados = [i for i in range(novo_chefe - 1, quantidade_nobres) if chefes[i] == novo_chefe]
    while len(subordinados) > 0:
        subordinado = subordinados.pop(0)
        chefes[subordinado] = novo_chefe

        for i in range(subordinado, quantidade_nobres):
            if chefes[i] == (subordinado + 1):
                subordinados.append(i)