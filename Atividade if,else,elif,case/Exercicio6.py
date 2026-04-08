# Exercício 6: Calculadora simples
operacao = input("Digite a operação (+, -, *, /): ")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
if operacao == '+':
    print(f"Resultado: {a + b}")
elif operacao == '-':
    print(f"Resultado: {a - b}")
elif operacao == '*':
    print(f"Resultado: {a * b}")
elif operacao == '/':
    if b != 0:
        print(f"Resultado: {a / b}")
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida.")