# Exercício 17: Som do animal
animal = input("Digite o nome do animal (cachorro, gato, vaca): ").lower()
match animal:
    case "cachorro":
        print("Au au")
    case "gato":
        print("Miau")
    case "vaca":
        print("Muu")
    case _:
        print("Animal desconhecido")