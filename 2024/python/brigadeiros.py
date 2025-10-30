quantidade_pratos, quantidade_amigos, max_segundos = [int(n) for n in input().split(" ")]
pratos = [int(n) for n in input().split(" ")]
disposicao_mesa = [int(n) for n in input().split(" ")]
amigos = [i for i in range(quantidade_pratos) if disposicao_mesa[i] == 1]

melhor_escolha = {}
def melhor_prato(amigo, inicio, segundos_restantes):
    global pratos, amigos, melhor_escolha

    try:
        return melhor_escolha[amigo][inicio][segundos_restantes]
    except KeyError:
        pass

    max_brigadeiros = 0
    for i in range(inicio, len(pratos) - len(amigos) + amigo + 1):
        tempo_troca = abs(i - amigos[amigo])
        if tempo_troca > segundos_restantes:
            continue
        
        max_brigadeiros = max(max_brigadeiros, pratos[i] + (melhor_prato(amigo+1, i+1, segundos_restantes - tempo_troca) if amigo < len(amigos) - 1 else 0))
    
    if not amigo in melhor_escolha:
        melhor_escolha[amigo] = {}
    if not inicio in melhor_escolha[amigo]:
        melhor_escolha[amigo][inicio] = {}
    
    melhor_escolha[amigo][inicio][segundos_restantes] = max_brigadeiros
    return melhor_escolha[amigo][inicio][segundos_restantes]

print(melhor_prato(0, 0, max_segundos))