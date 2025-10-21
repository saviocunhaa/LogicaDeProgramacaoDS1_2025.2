# Peça ao usuário para digitar 3 notas e armazene em uma lista. Depois, calcule a média dessas notas.


# Solicita 3 notas ao usuário e armazena em uma lista
notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Calcula a média
media = sum(notas) / len(notas)

# Exibe o resultado
print(f"A média das notas é: {media:.2f}")
