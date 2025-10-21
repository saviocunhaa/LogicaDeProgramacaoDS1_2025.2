# Peça a média final de um aluno e exiba o resultado conforme as regras: média ≥ 7 → “Aprovado”, média entre 5 e 6.9 → “Recuperação”, média < 5 → “Reprovado.”

# Solicita a média final do aluno
media = float(input("Digite a média final do aluno: "))

# Verifica o resultado
if media >= 7:
    print("Aprovado.")
elif 5 <= media < 7:
    print("Recuperação.")
else:
    print("Reprovado.")
