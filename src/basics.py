# lembrar de substituir tudo por loops
text = ["SOMA FODA", "MULTIPLICAÇÃO FODA"]
nsoma = []
nmulti = []

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

def multi():
    print("="*25)
    print(f"{text[1]:^25}")
    print("="*25, "\n")

    m1 = float(input("primeiro valor: "))
    m2 = float(input("segundo valor: "))

    r = m1 * m2

    print(f"O resultado da multiplicação entre {m1} e {m2} é igual a {r}")
