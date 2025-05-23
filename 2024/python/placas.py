def encaixa_padrao(placa, padrao):
    if len(placa) != len(padrao):
        return False
    
    caracteres_validos = {
        "L" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "D" : "0123456789",
        "-" : "-"
    }

    for i in range(len(placa)):
        caractere = placa[i]
        placeholder = padrao[i]

        if not caractere in caracteres_validos[placeholder]:
            return False
    
    return True


entrada = input()
if encaixa_padrao(entrada, "LLL-DDDD"):
    print(1)
elif encaixa_padrao(entrada, "LLLDLDD"):
    print(2)
else:
    print(0)