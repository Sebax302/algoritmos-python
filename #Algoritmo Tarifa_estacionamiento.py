#Algoritmo Tarifa_estacionamiento
horas = float(input("Ingrese las horas trabajadas: "))
nocturno = input("¿Es horario nocturno? (S/N): ").strip().upper()

tarifa = 1.50
total = horas * tarifa

if horas > 8:
    total *= 1.25

if nocturno == "S":
    total *= 1.30

print(f"El total a pagar es: ${total:.2f}")