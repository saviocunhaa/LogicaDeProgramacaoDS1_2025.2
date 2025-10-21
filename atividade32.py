# O sistema deve ler a média e a frequência do aluno. Ele será aprovado se tiver média ≥ 7 e frequência ≥ 75%. Caso contrário, estará reprovado. Mostre a situação final.

# Solicita a média e a frequência do aluno
media = float(input("Digite a média final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

# Verifica as condições para aprovação
if media >= 7 and frequencia >= 75:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")
