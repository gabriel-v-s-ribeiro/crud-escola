# Exercício 19: Saudação baseada na hora
hora = int(input("Digite a hora (0-23): "))
if hora < 12:
    print("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")