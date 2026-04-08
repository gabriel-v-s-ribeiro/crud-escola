# Exercício 12: Ação do semáforo
cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ").lower()
if cor == "verde":
    print("Pode passar.")
elif cor == "amarelo":
    print("Atenção, prepare-se para parar.")
elif cor == "vermelho":
    print("Pare!")
else:
    print("Cor inválida.")