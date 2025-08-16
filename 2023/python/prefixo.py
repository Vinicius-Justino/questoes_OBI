input()
palavra1 = input()
input()
palavra2 = input()

tamanho_prefixo = 0
for i in range(min(len(palavra1), len(palavra2))):
    if palavra1[i] != palavra2[i]:
        break

    tamanho_prefixo += 1

print(tamanho_prefixo)