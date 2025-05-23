def verifica_placa(placa, mascara):
    if len(placa) != len(mascara):
        return False
    
    tipos = "LNH"
    caracteres = [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "0123456789",
        "-"
    ]

    for i in range(len(mascara)):
        tipo = mascara[i]
        caractere = placa[i]

        if not caractere in caracteres[tipos.index(tipo)]:
            return False
    
    return True

entrada = input()
if verifica_placa(entrada, "LLLHNNNN"):
    print(1)
elif verifica_placa(entrada, "LLLNLNN"):
    print(2)
else:
    print(0)