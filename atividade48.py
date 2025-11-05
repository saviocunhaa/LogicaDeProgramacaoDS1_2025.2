# Verificação de Senhas Fortes
# Permita que o usuário insira senhas até digitar uma com pelo menos 8 caracteres.
# Quando isso ocorrer, exiba “Senha válida, cadastro permitido.”

# Verificação de Senhas Fortes
while True: #O while True mantém o programa pedindo a senha até atender ao requisito.
    senha = input("Digite uma senha: ")
    if len(senha) >= 8:
        print("Senha válida, cadastro permitido.")
        break
    else:
        print("Senha muito curta! Digite pelo menos 8 caracteres.")
