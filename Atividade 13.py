#Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro

numero = int(input())

if numero > 100:
    print(numero / 2)
else:
    print(numero * 2)