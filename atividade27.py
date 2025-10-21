# Em um sistema de vendas, o cliente deve receber 10% de desconto se for cadastrado como “VIP”. Caso contrário, se o valor da compra for maior que R$ 500, receba 5% de desconto. Em outros casos, não há desconto.

# Solicita os dados do cliente
tipo_cliente = input("Digite o tipo de cliente (VIP ou comum): ").lower()
valor_compra = float(input("Digite o valor da compra: R$ "))

# Aplica as regras de desconto
if tipo_cliente == "vip":
    desconto = valor_compra * 0.10
elif valor_compra > 500:
    desconto = valor_compra * 0.05
else:
    desconto = 0

# Calcula o valor final
valor_final = valor_compra - desconto

# Exibe o resultado
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")
