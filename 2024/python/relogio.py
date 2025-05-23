horas = int(input())
minutos = int(input())
segundos = int(input())

segundos += int(input())

minutos += segundos // 60
segundos %= 60

horas += minutos // 60
minutos %= 60

horas %= 24

print(f"{horas}\n{minutos}\n{segundos}")