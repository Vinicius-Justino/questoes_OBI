input()

alfabeto_alienigena = input()
mensagem = input()

mensagem_alienigena = True
for letra in mensagem:
    mensagem_alienigena = (letra in alfabeto_alienigena)

    if not mensagem_alienigena:
        break

print("S" if mensagem_alienigena else "N")