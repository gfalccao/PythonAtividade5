#Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par
#negativo”; Caso contrário → “impar”

numero = int(input("informe o valor"))

if numero % 2 == 0 and numero > 0:
    print("Par positivo")
elif numero % 2 == 0 and numero < 0:
    print("Par negativo")
else:
    print("impar")