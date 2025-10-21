# Solicite ao usuário que escolha um método de pagamento: "pix", "cartão" ou "dinheiro". Mostre uma mensagem diferente para cada opção, como “Pagamento instantâneo via Pix” ou “Pagamento processado no cartão.”

# Solicita o método de pagamento
metodo = input("Escolha o método de pagamento (pix, cartão ou dinheiro): ").lower()

# Verifica a opção escolhida
if metodo == "pix":
    print("💸 Pagamento instantâneo via Pix.")
elif metodo == "cartão":
    print("💳 Pagamento processado no cartão.")
elif metodo == "dinheiro":
    print("💵 Pagamento realizado em dinheiro.")
else:
    print("Método de pagamento inválido.")
