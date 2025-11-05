# Tabuada Automática
# Peça um número e exiba a tabuada de 1 a 10 usando for.

# Tabuada Automática
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
