# Classificação de Temperatura de CPU com Risco
# Receba a temperatura da CPU e mostre o status:

# Até 50°C → “Normal”

# De 51°C a 70°C → “Atenção”

# Acima de 70°C → “Crítico”
# E se o valor for negativo ou acima de 150°C, exiba “Erro: leitura inválida.”

# Solicita a temperatura da CPU
temperatura = float(input("Digite a temperatura da CPU em °C: "))

# Classifica a temperatura
if temperatura < 0 or temperatura > 150:
    print("Erro: leitura inválida.")
elif temperatura <= 50:
    print("Normal.")
elif temperatura <= 70:
    print("Atenção.")
else:
    print("Crítico.")
