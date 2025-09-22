quantidade_pratos, quantidade_amigos, limite_tempo = [int(n) for n in input().split(" ")]
mesa = [int(n) for n in input().split(" ")]
copia_mesa = mesa.copy()

lugares_vazios = []
for prato in reversed(sorted(mesa)):
    lugar = copia_mesa.index(prato)
    lugares_vazios.append(lugar)
    copia_mesa[lugar] = -1

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
    
    lugares_vazios.append(lugares_ocupados.pop(-1))

    if cont_troca_permanente == 0:
        lugares_ocupados.pop(-1)
        lugares_ocupados.insert(0, lugares_vazios.pop(0))
        cont_troca_permanente = len(lugares_vazios)   
        
    
    lugares_ocupados.append(lugares_vazios.pop(0))
    cont_troca_permanente -= 1

print(sum([mesa[i] for i in lugares_ocupados]))
