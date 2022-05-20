opcao = 0
while opcao != 6:
    try:
        opcao = int(input("1. Opção 1\n2. Opção 2\n3. Opção 3\n4. Opção 4\n5. Opção 5\n6. Sair\nDigite qual opção você quer abaixo:\n"))
        if opcao == 1:
            print("Essa é a opção 1\n" + "---" * 10)
        elif opcao == 2:
            print("Essa é a opção 2\n" + "---" * 10)
        elif opcao == 3:
            print("Essa é a opção 3\n" + "---" * 10)
        elif opcao == 4:
            print("Essa é a opção 4\n" + "---" * 10)
        elif opcao == 5:
            print("Essa é a opção 5\n" + "---" * 10)
        elif opcao == 6:
            print("Você saiu.")
        else:
            print("Opção inválida. Digite uma opção dentre:")
    except ValueError:
        print("Por favor, insira um número entre as opções abaixo:")