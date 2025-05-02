consoantes = "bcdfghjklmnpqrstvxzz"
vogais = "aeiou"

for letra in input():
    if letra in vogais:
        print(letra, end="")
        continue

    print(letra, end="")

    distancias_vogais = [abs(ord(letra) - ord(vogal)) for vogal in vogais]
    print(vogais[distancias_vogais.index(min(distancias_vogais))], end="")
    print(consoantes[consoantes.index(letra) + 1], end="")

print()