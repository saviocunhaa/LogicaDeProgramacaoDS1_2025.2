# Validação de CPF Simples
# Peça ao usuário para digitar um CPF (apenas números). Se ele tiver exatamente 11 dígitos, exiba “CPF válido.” Caso contrário, exiba “CPF inválido.”

# Solicita o CPF ao usuário
cpf = input("Digite seu CPF (apenas números): ")

# Verifica se o CPF tem exatamente 11 dígitos numéricos
if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido.")
else:
    print("CPF inválido.")
