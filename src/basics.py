# lembrar de substituir tudo o que precisar loops
import math
text = ["SOMA FODA", "DIVISÃO FODA", "MULTIPLICAÇÃO FODA", "RAIZ NÃO REDONDA"]

def soma():
    nsoma = []

    print("-"*25)
    print(f"{text[0]:^25}")
    print("-"*25, "\n")

    qnt = int(input("Quantos numeros vc quer somar? "))

    for i in range(0, qnt):
        nsoma.append(float(input(f"{i+1} valor: ")))

    somafoda = sum(nsoma)
    print(f"A soma de todos os valores é {somafoda}\n")
    nsoma.clear()

def divid():
    print("-"*25)
    print(f"{text[1]:^25}")
    print("-"*25, "\n")

    dividendo = float(input("Coloque aqui o dividendo: "))
    divisor = float(input("Coloque aqui o divisor: "))
    resul = dividendo / divisor

    print(f"O resultado da divisao enre {dividendo} e {divisor} eh {resul}\n")

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

# se nao der certo poe uma var pra ser o segundo numero que vai trocando ate o n ser o ultimo valor aew da certo tbm :)

    print(f"O resultado da multiplicação é: {produto}")
    nmulti.clear()

def raiz():
    print("="*25)
    print(f"{text[3]:^25}")
    print("="*25, "\n")

    num = float(input("digite o valor a ser calculada a raiz quadrada: "))
    resul = math.sqrt(num)

    print(f"A raiz quadrada de {num} eh {resul}\n")
