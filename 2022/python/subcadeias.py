tamanho_entrada = int(input())
entrada = input()

for tamanho_cadeia in range(tamanho_entrada, -1, -1):
    maior_tamanho = False

    for inicio in range(tamanho_entrada - tamanho_cadeia + 1):
        cadeia = list(entrada[inicio : inicio + tamanho_cadeia])

        palindromo = True
        while palindromo and len(cadeia) > 1:
            palindromo = cadeia.pop(0) == cadeia.pop(-1)
        
        if palindromo:
            maior_tamanho = True
            break
    
    if maior_tamanho:
        print(tamanho_cadeia)
        break