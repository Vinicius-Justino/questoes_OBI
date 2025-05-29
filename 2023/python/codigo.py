tamanho_sequencia = int(input())
sequencia = input()

letra_atual = sequencia[0]
cont_letra = 1

saida = ""
for i in range(1, tamanho_sequencia):
    if sequencia[i] == letra_atual:
        cont_letra += 1
    else:
        saida += f"{cont_letra} {letra_atual} "
        letra_atual = sequencia[i]
        cont_letra = 1

saida += f"{cont_letra} {letra_atual}"
print(saida)