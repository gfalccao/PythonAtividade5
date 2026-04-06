# Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é
#múltiplo”

numero = int(input("informe o valor"))

if numero % 3 == 0:
    print("Multiplo de 3")
else:
    print("Não é multiplo")