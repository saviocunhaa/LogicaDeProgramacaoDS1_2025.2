# Sistema de Pedidos Online
# Peça o valor total do pedido e o método de entrega: "retirada" ou "entrega".

# Se for entrega e o valor for menor que R$ 50, cobre taxa de R$ 10.

# Caso contrário, o frete é grátis.
# Mostre o valor final a pagar.

# Solicita o valor do pedido e o método de entrega
valor_pedido = float(input("Digite o valor total do pedido: R$ "))
metodo = input("Digite o método de entrega (retirada ou entrega): ").lower()

# Calcula o valor final
if metodo == "entrega" and valor_pedido < 50:
    valor_final = valor_pedido + 10
    print("Taxa de entrega aplicada: R$ 10,00")
else:
    valor_final = valor_pedido
    print("Frete grátis!")

# Mostra o valor total a pagar
print(f"Valor final a pagar: R$ {valor_final:.2f}")
