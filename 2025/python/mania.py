linhas, colunas = [int(n) for n in input().split(" ")]

gotas_adicionadas_par, gotas_adicionadas_impar = 0, 0
paridade = 0

bandeja_par, bandeja_impar = [], []
for i in range(linhas):
    linha_atual = [int(gotas) for gotas in input().split(" ")]
    
    bandeja_par.append([])
    bandeja_impar.append([])
    for j in range(colunas):
        gotas = linha_atual.pop(0)
        if gotas % 2 == paridade:
            bandeja_par[i].append(gotas)

            bandeja_impar[i].append(gotas + 1)
            gotas_adicionadas_impar += 1
        else:
            bandeja_impar[i].append(gotas)

            bandeja_par[i].append(gotas + 1)
            gotas_adicionadas_par += 1
        
        paridade = (paridade + 1) % 2

if gotas_adicionadas_par < gotas_adicionadas_impar:
    print(gotas_adicionadas_par)
    for linha in bandeja_par:
        print(" ".join([str(gotas) for gotas in linha]))
else:
    print(gotas_adicionadas_impar)
    for linha in bandeja_impar:
        print(" ".join([str(gotas) for gotas in linha]))