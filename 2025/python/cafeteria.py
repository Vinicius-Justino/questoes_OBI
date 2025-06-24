min_leite = int(input())
max_leite = int(input())
volume_copo = int(input())
dose_cafe = int(input())

possivel_fazer = False
for volume_leite in range(min_leite, max_leite + 1):
    volume_cafe = volume_copo - volume_leite

    possivel_fazer = (volume_cafe % dose_cafe == 0)
    if possivel_fazer:
        break

print("S" if possivel_fazer else "N")