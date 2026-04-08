# Exercício 15: Desconto baseado no valor da compra
valor = float(input("Digite o valor da compra: "))
if valor > 100:
    desconto = valor * 0.1
    print(f"Desconto: R$ {desconto:.2f}")
elif valor > 50:
    desconto = valor * 0.05
    print(f"Desconto: R$ {desconto:.2f}")
else:
    print("Sem desconto.")