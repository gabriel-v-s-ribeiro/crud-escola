# Exercício 18: Conversão de nota para GPA
nota = input("Digite a nota (A, B, C, D, F): ").upper()
if nota == "A":
    print("GPA: 4.0")
elif nota == "B":
    print("GPA: 3.0")
elif nota == "C":
    print("GPA: 2.0")
elif nota == "D":
    print("GPA: 1.0")
elif nota == "F":
    print("GPA: 0.0")
else:
    print("Nota inválida")