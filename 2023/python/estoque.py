tipos, tamanhos = [int(n) for n in input().split(" ")]

estoque = []
for i in range(tipos):
    estoque.append([int(quantidade) for quantidade in input().split(" ")])

pedidos_efetivados = 0
for i in range(int(input())):
    tipo, tamanho = [int(n) - 1 for n in input().split()]
    if estoque[tipo][tamanho] == 0:
        continue

    estoque[tipo][tamanho] -= 1
    pedidos_efetivados += 1

print(pedidos_efetivados)