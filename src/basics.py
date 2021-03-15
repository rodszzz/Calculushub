# lembrar de substituir tudo por loops
import math
text = ["SOMA FODA", "DIVISÃO FODA", "MULTIPLICAÇÃO FODA", "RAIZ NÃO REDONDA"]
nsoma = []

def soma():
    print("-"*25)
    print(f"{text[0]:^25}")
    print("-"*25, "\n")

    qnt = int(input("Quantos numeros vc quer somar? "))

    for i in range(0, qnt):
        nsoma.append(float(input(f"{i+1} valor: ")))

    somafoda = sum(nsoma)
    print(f"A soma de todos os valores é {somafoda}")
    nsoma.clear()

def divid():
    print("-"*25)
    print(f"{text[1]:^25}")
    print("-"*25)

    dividendo = float(input("Coloque aqui o dividendo: "))
    divisor = float(input("Coloque aqui o divisor: "))
    resul = dividendo / divisor

    print(f"O resultado da divisao enre {dividendo} e {divisor} eh {resul}")

def multi():
    print("="*25)
    print(f"{text[2]:^25}")
    print("="*25, "\n")

    m1 = float(input("primeiro valor: "))
    m2 = float(input("segundo valor: "))

    resul = m1 * m2

    print(f"O resultado da multiplicação entre {m1} e {m2} é igual a {resul}")

def raiz():
    print("="*25)
    print(f"{text[2]:^25}")
    print("="*25)

    num = float(input("digite o valor a ser calculada a raiz quadrada: "))
    resul = math.sqrt(num)

    print(f"A raiz quadrada de {num} eh {resul}")
