#Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença
#entre eles

a = int(input("informe o valor"))
b = int(input("informe o valor"))

if a == b:
    print("Iguais")
else:
    print("Diferentes")
    print(a - b)