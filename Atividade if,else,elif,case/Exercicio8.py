# Exercício 8: Conselho baseado na temperatura
temperatura = float(input("Digite a temperatura em Celsius: "))
if temperatura < 0:
    print("Está congelando!")
elif temperatura < 15:
    print("Está frio, vista um casaco.")
elif temperatura < 25:
    print("Clima agradável.")
else:
    print("Está quente!")