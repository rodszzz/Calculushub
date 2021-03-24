import math
text = ["SOMA FODA", "DIVISÃO FODA", "MULTIPLICAÇÃO FODA", "RAIZ NÃO REDONDA"]

def soma():
    nsoma = []

    print("="*25)
    print(f"{text[0]:^25}")
    print("="*25, "\n")

    qnt = int(input("Quantos numeros vc quer somar? "))

    for i in range(0, qnt):
        nsoma.append(float(input(f"{i+1} valor: ")))

    somafoda = sum(nsoma)
    print(f"A soma de todos os valores é {somafoda}")
    print("<", "-"*40, ">", "\n")
    nsoma.clear()

def divid():
    print("="*25)
    print(f"{text[1]:^25}")
    print("="*25, "\n")

    dividendo = float(input("Coloque aqui o dividendo: "))
    divisor = float(input("Coloque aqui o divisor: "))
    resul = dividendo / divisor

    print(f"O resultado da divisao enre {dividendo} e {divisor} eh {resul}")
    print("<", "-"*40, ">","\n")

def multi():
    nmulti = []
    produto = 1

    print("="*25)
    print(f"{text[2]:^25}")
    print("="*25, "\n")

    qnt = int(input("Quantos números vc quer multiplicar? "))

    for n in range(qnt):
        nmulti.append(float(input(f"Coloque o {n+1} valor: ")))

    for item in nmulti:
        produto = produto * item

    print(f"O resultado da multiplicação é: {produto}")
    print("<", "-"*40, ">", "\n")
    nmulti.clear()

def raiz():
    nraiz = []
    resul = []
    print("="*25)
    print(f"{text[3]:^25}")
    print("="*25, "\n")

    qnt = int(input("Vc quer saber a raiz de quantos numeros? "))

    for v in range(qnt):
        nraiz.append(float(input(f"Coloque o {v+1} numero: ")))

    for n in nraiz:
        cal = math.sqrt(n)
        resul.append(cal)

    print()
    for item in range(qnt):
        print(f"A raiz quadrada de {nraiz[item]} é {resul[item]}")
    print("<", "-"*40, ">", "\n")
