# Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou
#neutro

if numero == 0:
    print("neutro")
elif numero % 2 == 0 and numero > 0:
    print("par positivo")
elif numero % 2 == 0 and numero < 0:
    print("par negativo")
elif numero % 2 != 0 and numero > 0:
    print("impar positivo")
else:
    print("impar negativo")