# Atividade 9 – Média de Notas
# Leia três notas de um aluno.
# Calcule e mostre a média final.



# Leitura das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição do resultado
print("A média final do aluno é:", media)

# dessa forma ele vai dar apenas 2 casas decimais apos a virgula gracas ao :.2f
# print(f"A média final do aluno é: {media:.2f}")

