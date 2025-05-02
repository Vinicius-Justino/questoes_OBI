input()

sequenciaA = [numero for numero in input().split(" ")]
sequenciaB = [numero for numero in input().split(" ")]

for i in range(len(sequenciaA)):
    if (len(sequenciaB) == 0):
        break

    if sequenciaA[i] == sequenciaB[0]:
        sequenciaB.pop(0)

print("S" if len(sequenciaB) == 0 else "N")