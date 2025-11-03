quantidade_senhas = int(input())
senhas = [input() for _ in range(quantidade_senhas)]

cont_pares = -quantidade_senhas
for i in range(quantidade_senhas):
    for j in range(quantidade_senhas):
        cont_pares += int((senhas[i] in senhas[j]))

print(cont_pares)