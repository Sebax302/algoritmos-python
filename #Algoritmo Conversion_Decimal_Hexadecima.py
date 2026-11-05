#Algoritmo Conversion_Decimal_Hexadecimal
numero = int(input("Ingrese el número decimal: "))

if numero == 0:
    hexadecimal = "0"
else:
    digitos = "0123456789ABCDEF"
    hexadecimal = ""
    valor = abs(numero)

    while valor > 0:
        residuo = valor % 16
        hexadecimal = digitos[residuo] + hexadecimal
        valor //= 16

    if numero < 0:
        hexadecimal = "-" + hexadecimal

print(f"El número hexadecimal es: {hexadecimal}")