# Um sistema de monitoramento deve ler a temperatura de um servidor e classificar assim: até 60°C → “Normal”; entre 61°C e 80°C → “Atenção”; acima de 80°C → “Crítico — risco de superaquecimento!”.

# Solicita a temperatura do servidor
temperatura = float(input("Digite a temperatura do servidor em °C: "))

# Classifica o nível de temperatura
if temperatura <= 60:
    print("Normal.")
elif 61 <= temperatura <= 80:
    print("Atenção.")
else:
    print("Crítico — risco de superaquecimento!")
