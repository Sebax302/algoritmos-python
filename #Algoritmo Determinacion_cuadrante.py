#Algoritmo Determinacion_cuadrante
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

if x == 0 and y == 0:
    print("El punto está en el origen.")
elif x == 0:
    print("El punto está sobre el eje Y.")
elif y == 0:
    print("El punto está sobre el eje X.")
elif x > 0 and y > 0:
    print("El punto está en el primer cuadrante.")
elif x < 0 and y > 0:
    print("El punto está en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("El punto está en el tercer cuadrante.")
else:
    print("El punto está en el cuarto cuadrante.")