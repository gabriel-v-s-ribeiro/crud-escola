# Exercício 16: Estação do ano
mes = int(input("Digite o mês (1-12): "))
if mes in [12, 1, 2]:
    print("Inverno")
elif mes in [3, 4, 5]:
    print("Primavera")
elif mes in [6, 7, 8]:
    print("Verão")
elif mes in [9, 10, 11]:
    print("Outono")
else:
    print("Mês inválido")