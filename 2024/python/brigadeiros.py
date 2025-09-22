quantidade_pratos, quantidade_amigos, limite_tempo = [int(n) for n in input().split(" ")]

mesa = [int(n) for n in input().split(" ")]
lugares_vazios = [mesa.index(lugar) for lugar in reversed(sorted(mesa))]
lugares_ocupados = [lugares_vazios.pop(0) for i in range(quantidade_amigos)]
cont_troca_permanente = quantidade_pratos - quantidade_amigos

posicao_inicial = [int(n) for n in input().split(" ")]
    
while True:
    posicao_ideal = [(1 if i in lugares_ocupados else 0) for i in range(quantidade_pratos)]
    resultado_xor = [(1 if [posicao_inicial[i], posicao_ideal[i]].count(1) == 1 else 0) for i in range(quantidade_pratos)]

    deslocamento_acontecendo = False
    distancia = 0
    for lugar in resultado_xor:
        if deslocamento_acontecendo:
            distancia += 1

        deslocamento_acontecendo = (lugar != int(deslocamento_acontecendo))
    
    if distancia <= limite_tempo:
        break
    
    if cont_troca_permanente > 0:
        lugares_vazios.append(lugares_ocupados.pop(-1))
        cont_troca_permanente -= 1
    else:
        lugares_ocupados.pop(-2)
        lugares_ocupados.insert(0, lugares_vazios.pop(0))
        cont_troca_permanente = len(lugares_vazios) - 1

    lugares_ocupados.append(lugares_vazios.pop(0))

print(sum([mesa[i] for i in lugares_ocupados]))