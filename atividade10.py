# Atividade 10 – Conversão de Unidades
# Peça ao usuário um valor em metros.
# Converta e mostre o resultado em centímetros e milímetros.


# Entrada de dados
metros = float(input("Digite o valor em metros: "))

# Conversões
centimetros = metros * 100
milimetros = metros * 1000

# Exibição dos resultados
print(f"{metros} metros equivalem a {centimetros} centímetros e {milimetros} milímetros.")
