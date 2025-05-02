numeros = []
for i in range(int(input())):
    numero = int(input())

    if numero == 0:
        numeros.pop(-1)
    else:
        numeros.append(numero)
    
print(sum(numeros))