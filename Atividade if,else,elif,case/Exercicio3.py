# Exercício 3: Classificar nota em letra (A, B, C, D, F)
nota = float(input("Digite a nota (0-100): "))
if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
elif nota >= 60:
    print("Nota: D")
else:
    print("Nota: F")