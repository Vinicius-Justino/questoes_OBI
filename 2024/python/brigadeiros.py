quantidade_pratos, quantidade_amigos, max_segundos = [int(n) for n in input().split(" ")]
pratos = [int(n) for n in input().split(" ")]
disposicao_mesa = [int(n) for n in input().split(" ")]
posicoes_amigos = [i for i in range(quantidade_pratos) if disposicao_mesa[i] == 1]

max_segundos = min(max_segundos, (quantidade_pratos - quantidade_amigos) * quantidade_amigos)

max_brigadeiros = [[], []]
for prato in range(quantidade_pratos):
    max_brigadeiros[0].append([0] * (max_segundos+1))
    max_brigadeiros[1].append([0] * (max_segundos+1))

for amigo in range(quantidade_amigos):
    tabela_amigo = (amigo+1) % 2

    for prato in range(amigo, quantidade_pratos - quantidade_amigos + amigo + 1):
        tempo_troca = abs(prato - posicoes_amigos[amigo])
        
        for tempo_limite in range(max_segundos+1):
            if tempo_limite < tempo_troca:
                max_brigadeiros[tabela_amigo][prato][tempo_limite] = (max_brigadeiros[tabela_amigo][prato-1][tempo_limite] if prato-1 >= amigo else 0)
                continue

            max_brigadeiros[tabela_amigo][prato][tempo_limite] = max(
                pratos[prato] + max_brigadeiros[1-tabela_amigo][prato-1][tempo_limite-tempo_troca],
                (max_brigadeiros[tabela_amigo][prato-1][tempo_limite] if prato-1 >= amigo else 0)
            )

print(max_brigadeiros[quantidade_amigos%2][quantidade_pratos-1][max_segundos])
# for tabela in range(2):
#     print(f"tabela {tabela}:")
#     print("\t" + "\t".join([str(tempo) for tempo in range(max_segundos+1)]))
#     for prato in range(quantidade_pratos):
#         print(f"{prato}\t" + "\t".join([str(max_brigadeiros[tabela][prato][tempo]) for tempo in range(max_segundos+1)]))
#     print()