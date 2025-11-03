quantidade_linhas, quantidade_colunas = [int(n) for n in input().split(" ")]

valores_variaveis = {}
tabela = []
somas = [[]]
for i in range(quantidade_linhas):
    linha = input().split(" ")
    tabela.append([linha[j] for j in range(quantidade_colunas)])
    somas[0].append(int(linha[-1]))
    
somas.append([int(soma) for soma in input().split(" ")])

celulas_preenchidas = 0
while celulas_preenchidas < (quantidade_linhas * quantidade_colunas):
    for i in range(quantidade_linhas):
        linha = tabela[i]
        cont_variaveis = {}
        soma_conhecida = 0
        for celula in linha:
            if type(celula) == int:
                soma_conhecida += celula
            else:
                cont_variaveis[celula] = linha.count(celula)
        
        if len(cont_variaveis) == 1:
            variavel = list(cont_variaveis.keys())[0]
            valor_variavel = (somas[0][i] - soma_conhecida) // cont_variaveis[variavel]
            valores_variaveis[variavel] = valor_variavel

            for j in range(quantidade_linhas):
                while variavel in tabela[j]:
                    tabela[j][tabela[j].index(variavel)] = valor_variavel
                    celulas_preenchidas += 1
    
    for j in range(quantidade_colunas):
        coluna = [tabela[i][j] for i in range(quantidade_linhas)]
        cont_variaveis = {}
        soma_conhecida = 0
        for celula in coluna:
            if type(celula) == int:
                soma_conhecida += celula
            else:
                cont_variaveis[celula] = coluna.count(celula)
        
        if len(cont_variaveis) == 1:
            variavel = list(cont_variaveis.keys())[0]
            valor_variavel = (somas[1][j] - soma_conhecida) // cont_variaveis[variavel]
            valores_variaveis[variavel] = valor_variavel

            for i in range(quantidade_linhas):
                while variavel in tabela[i]:
                    tabela[i][tabela[i].index(variavel)] = valor_variavel
                    celulas_preenchidas += 1

for letra1 in range(ord("a"), ord("z")+1):
    for letra2 in range(ord("a"), ord("z")+1):
        try:
            var = chr(letra1) + chr(letra2)
            print(f"{var} {valores_variaveis[var]}")
        except KeyError:
            pass