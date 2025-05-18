colunas, linhas, quantidade_cameras = [int(n) for n in input().split(" ")]

sala = []
for linha in range(linhas):
    sala.append([])

    for coluna in range(colunas):
        sala[linha].append(True)

def avanca_fov_camera(coordenadas, direcao):
    for i in range(2):
        if not (0 <= coordenadas[i] < [linhas, colunas][i]):
            return
    
    sala[coordenadas[0]][coordenadas[1]] = False

    if direcao == "N":
        coordenadas[0] -= 1
    elif direcao == "S":
        coordenadas[0] += 1
    elif direcao == "L":
        coordenadas[1] += 1
    else:
        coordenadas[1] -= 1
    
    avanca_fov_camera(coordenadas, direcao)

for camera in range(quantidade_cameras):
    coluna, linha, direcao = [n for n in input().split(" ")]
    avanca_fov_camera([int(linha) - 1, int(coluna) - 1], direcao)

possivel_contornar_cameras = False
def caminha(coordenadas, direcao_anterior):
    global possivel_contornar_cameras

    if possivel_contornar_cameras:
        return
    elif coordenadas == [linhas - 1, colunas - 1]:
        possivel_contornar_cameras = True
        return

    for i in range(2):
        if not (0 <= coordenadas[i] < [linhas, colunas][i]):
            return
    
    if not sala[coordenadas[0]][coordenadas[1]]:
        return
    
    if direcao_anterior != "N":
        caminha([coordenadas[0] + 1, coordenadas[1]], "S")
    if direcao_anterior != "O":
        caminha([coordenadas[0], coordenadas[1] + 1], "L")
    if direcao_anterior != "L":
        caminha([coordenadas[0], coordenadas[1] - 1], "O")
    if direcao_anterior != "S":
        caminha([coordenadas[0] - 1, coordenadas[1]], "N")

try:
    caminha([0, 0], "L")
except RecursionError:
    pass

print("S" if possivel_contornar_cameras else "N")