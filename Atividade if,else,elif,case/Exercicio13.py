# Exercício 13: Força da senha (básico)
senha = input("Digite uma senha: ")
if len(senha) < 6:
    print("Senha fraca")
elif len(senha) < 10:
    print("Senha média")
else:
    print("Senha forte")