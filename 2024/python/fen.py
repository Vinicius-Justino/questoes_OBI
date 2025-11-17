tabuleiro = input().split("/")

for notacao in tabuleiro:
    linha = ""
    for caracter in notacao:
        try:
            linha += " " * int(caracter)
        except ValueError:
            linha += caracter
    
    print(f"|{'|'.join(list(linha))}|")