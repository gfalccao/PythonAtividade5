#Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.

a = int(input())
b = int(input())

# soma
print(a + b)

# comparação
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("iguais")