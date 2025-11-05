# Controle de Temperatura de Servidores
# Leia 5 temperaturas e mostre a média delas.
# Use um laço para fazer as leituras e cálculos.

# Controle de Temperatura de Servidores
soma = 0

for i in range(1, 6):
    temp = float(input(f"Digite a temperatura {i}: "))
    soma += temp

media = soma / 5
print(f"\nMédia das temperaturas: {media:.2f}°C")
