from basics import soma, multi
lista = ["[0] soma", "[1] multiplicação"]
funcs = [soma, multi]
# listas com todas funções de cálculo

print("Bem vindo ao Calculushub!")

while True:
    print("Suas opções de contas são essas:")
    for p in range(0, len(lista)):
        print(lista[p])
    escolha = int(input(f"Deseja fazer qual operação? "))
    if escolha >= 2:
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
        cont = input("Deseja continuar? [S/n] ").strip().upper()
        if cont in 'SN':
            break
            print("Opção inválida! Tente novamente ")
    if cont == 'N':
        print("<<< Volte sempre! >>>")
        break
