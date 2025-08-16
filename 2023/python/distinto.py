sequencia = []
maior_tamanho = 0
for i in range(int(input())):
    numero = int(input())

    if numero in sequencia:
        maior_tamanho = max(maior_tamanho, len(sequencia))

        while sequencia.pop(0) != numero:
            pass
    
    sequencia.append(numero)

print(maior_tamanho)