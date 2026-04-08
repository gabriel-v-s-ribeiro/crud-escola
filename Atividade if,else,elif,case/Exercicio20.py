# Exercício 20: Menu de seleção
opcao = input("Escolha uma opção (1: Café, 2: Chá, 3: Suco): ")
match opcao:
    case "1":
        print("Você escolheu Café.")
    case "2":
        print("Você escolheu Chá.")
    case "3":
        print("Você escolheu Suco.")
    case _:
        print("Opção inválida.")