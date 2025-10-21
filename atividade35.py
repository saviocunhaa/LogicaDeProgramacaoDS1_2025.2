# O usuário informa sua categoria de cliente (bronze, prata, ouro, diamante) e o valor da compra.

# Bronze: sem desconto

# Prata: 5%

# Ouro: 10%

# Diamante: 15%
# Calcule e mostre o valor final com desconto.

# Solicita os dados do cliente
categoria = input("Digite sua categoria (bronze, prata, ouro, diamante): ").lower()
valor_compra = float(input("Digite o valor da compra: R$ "))

# Define o percentual de desconto conforme a categoria
if categoria == "bronze":
    desconto = 0
elif categoria == "prata":
    desconto = 0.05
elif categoria == "ouro":
    desconto = 0.10
elif categoria == "diamante":
    desconto = 0.15
else:
    desconto = 0
    print("Categoria inválida. Nenhum desconto aplicado.")

# Calcula o valor final
valor_final = valor_compra - (valor_compra * desconto)

# Exibe o resultado
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor final da compra: R$ {valor_final:.2f}")
