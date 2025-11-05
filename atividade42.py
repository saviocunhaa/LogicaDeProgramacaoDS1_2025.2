# Cadastro de Produtos
# Peça o nome e preço de 5 produtos usando um laço for.
# Ao final, exiba o nome de todos e a soma total dos preços.

# Cadastro de Produtos
produtos = []
total = 0

for i in range(1, 6):
    nome = input(f"Digite o nome do produto {i}: ")
    preco = float(input(f"Digite o preço do produto {i}: R$ "))
    produtos.append(nome)
    total += preco

print("\nProdutos cadastrados:")
for p in produtos:
    print("-", p)

print(f"\nSoma total dos preços: R$ {total:.2f}")
