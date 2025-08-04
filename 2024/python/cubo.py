N = int(input())

zero_faces = (N - 2) ** 3
uma_face = ((N - 2) ** 2) * 6
duas_faces = (N - 2) * 12
tres_faces = 8

print(zero_faces, uma_face, duas_faces, tres_faces, sep="\n")