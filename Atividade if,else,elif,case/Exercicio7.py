# Exercício 7: Categoria de idade
idade = int(input("Digite a idade: "))
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")