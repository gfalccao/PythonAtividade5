#Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo”
#caso contrário.

numero = int(input())

if 0 <= numero <= 10:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")