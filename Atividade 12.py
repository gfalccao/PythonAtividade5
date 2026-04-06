#Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.

a = int(input("informe o valor"))
b = int(input("informe o valor"))

print(a + b)

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("iguais")