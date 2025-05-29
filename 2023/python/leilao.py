vencedor = ["ninguém", 0]
for i in range(int(input())):
    lance = [input(), int(input())]
    vencedor = lance.copy() if lance[1] > vencedor[1] else vencedor

print(f"{vencedor[0]}\n{vencedor[1]}")