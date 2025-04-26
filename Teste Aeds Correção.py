tentativas = 3
pinT = 1234

while tentativas > 0:
    try:
        pin = int(input("Digite os 4 dígitos para o PIN: "))
    except ValueError:
        print("Entrada inválida!")
        continue

    if pin == pinT:
        print("Login bem-sucedido!")
        break
    else:
        tentativas -= 1
        if tentativas == 0:
            print("Número máximo de tentativas excedido. Tente mais tarde.")
            exit()
        else:
            print(f"PIN incorreto. Tentativas restantes: {tentativas}")
while True:
    print("MENU")
    print("1 - Tabuada")
    print("2 - Par ou Ímpar")
    print("3 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Entrada inválida! Digite 1, 2 ou 3.")
        continue

    if opcao == 1:
        try:
            num = int(input("Digite um número para ver a tabuada: "))
            print(f"Tabuada do {num}:")
            for i in range(1, 10):
                print(f"{num} x {i} = {num * i}")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
    elif opcao == 2:
        try:
            num = int(input("Digite um número: "))
            if num % 2 == 0:
                print("O número é PAR.")
            else:
                print("O número é ÍMPAR.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
    else: 
        if opcao == 3:
            print("Sistema encerrado. Até logo!")
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")