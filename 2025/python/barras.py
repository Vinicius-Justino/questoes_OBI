quantidade_brinquedos = int(input())
avaliacoes = [int(n) for n in input().split(" ")]

altura_grafico = max(avaliacoes)
for nivel in range(altura_grafico, 0, -1):
    linha_saida = ""

    for avaliacao in avaliacoes:
        linha_saida += "1" if avaliacao >= nivel else "0"
        linha_saida += " "
    
    print(linha_saida[ : len(linha_saida) - 1])