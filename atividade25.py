# Crie um programa que pergunte a quantidade de um produto em estoque. Se for igual a 0, exiba “Produto esgotado.” Se for até 5, exiba “Estoque baixo.” Caso contrário, exiba “Estoque normal.”

# Solicita a quantidade em estoque
quantidade = int(input("Digite a quantidade do produto em estoque: "))

# Verifica a situação do estoque
if quantidade == 0:
    print("Produto esgotado.")
elif quantidade <= 5:
    print("Estoque baixo.")
else:
    print("Estoque normal.")
