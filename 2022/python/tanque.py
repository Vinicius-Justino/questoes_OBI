quilometros_por_litro = int(input())
distancia = int(input())
litros_no_tanque = int(input())

litros_necessarios = distancia / quilometros_por_litro
if litros_no_tanque >= litros_necessarios:
    print("0.0")
else:
    print(f"{(litros_necessarios - litros_no_tanque):.1f}")