import emoji
from basics import soma, divid, multi, raiz
lista = ["[0] soma","[1] divisao", "[2] multiplicação", "[3] raiz quadrada"]
funcs = [soma, divid, multi, raiz]
# listas com todas funções de cálculo

print(emoji.emojize("Bem vindo ao Calculushub! :party_popper:"))

while True:
    print("Suas opções de contas são essas:\n")
    for p in range(0, len(lista)):
        print(lista[p])
    escolha = int(input(f"\nDeseja fazer qual operação? "))
    print()
    if escolha >= 4:
        while True:
            print("Opa! Esse número está fora do meu alcance!\nTente de novo, por favor")
            print("Suas opções de contas são essas:")
            for p in range(0, len(lista)):
                print(lista[p])
            escolha = int(input(f"Deseja fazer qual operação? "))
            if escolha in range(0, len(lista)):
                break
    funcs[escolha]()
    while True:
        cont = input("Deseja fazer mais cálculos? [S/n] ").strip().upper()[0]
        if cont in 'SN':
            break
            print("Opção inválida! Tente novamente ")
    if cont == 'N':
        print("<<< Volte sempre! >>>")
        break
