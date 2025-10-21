# Peça o valor que o usuário deseja sacar. O sistema só deve permitir saques múltiplos de 10. Caso contrário, exiba “Valor inválido para saque.” Se o valor for válido, exiba “Saque autorizado.”

# Solicita o valor do saque
valor = int(input("Digite o valor que deseja sacar: R$ "))

# Verifica se o valor é múltiplo de 10
if valor % 10 == 0:
    print("Saque autorizado.")
else:
    print("Valor inválido para saque.")
