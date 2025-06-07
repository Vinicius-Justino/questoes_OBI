quantidade_medicoes = int(input())
soma_desejada = int(input())
medicoes = [int(n) for n in input().split(" ")]

intervalos_adequados = 0
for tamanho_intervalo in range(1, quantidade_medicoes + 1):
    for inicio_intervalo in range(quantidade_medicoes - tamanho_intervalo + 1):
        intervalos_adequados += int((sum(medicoes[inicio_intervalo : inicio_intervalo + tamanho_intervalo]) == soma_desejada))

print(intervalos_adequados)