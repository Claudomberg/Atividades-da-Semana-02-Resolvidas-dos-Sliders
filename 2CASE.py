print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
x = int(input("Escolha uma operação: "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

match x:
    case 1:
        r = n1 + n2
        print(f"Resultado: {r}")
    case 2:
        r = n1 - n2
        print(f"Resultado: {r}")
    case 3:
        r = n1 * n2
        print(f"Resultado: {r}")
    case 4:
        r = n1 / n2 if n2 != 0 else "Erro: Divisão por zero"
        print(f"Resultado: {r}")
    case _:
        print("Opção inválida")