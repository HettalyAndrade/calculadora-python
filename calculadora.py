def calculadora():
    while True:
        print("Escolha uma operação:\n")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        opcao = int(input("Digite aqui..."))
        if opcao in [1,2,3,4]: #ao inves de escrever (opcao == 1 or ==2 or ==3 or ==4)
            num1 = float(input("Digite o primeiro número:\n"))
            num2 = float(input("Digite o segundo número:\n"))
            if opcao == 1:
                calc = num1 + num2
                print(f"Resultado:{calc}")
            elif opcao == 2:
                calc = num1 - num2
                print(f"Resultado:{calc}")
            elif opcao == 3:
                calc = num1 * num2
                print(f"Resultado:{calc}")
            elif opcao == 4:
                if num2 !=0:
                    calc = num1 / num2
                    print(f"Resultado:{calc}")
                else: 
                    print("Erro: Divisão por zero") #evitar erros de calculo com zero
        elif opcao == 0:
            print("Encerrando o programa...")
            break
        else:
            print("Opção Inválida! Tente novamente")
calculadora()