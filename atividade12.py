# Crie uma lista de números de 1 a 10 e mostre apenas os números pares.

# Cria a lista de números de 1 a 10
numeros = list(range(1, 11))

# Exibe apenas os números pares
print("Números pares:")
for n in numeros:
    if n % 2 == 0:
        print(n)
