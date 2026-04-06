#Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário,
#informe “Número inválido

numero = int(input("informe o valor"))

if numero > 0:
    raiz = numero ** 0.5
    print(raiz)
else:
    print("Número inválido")