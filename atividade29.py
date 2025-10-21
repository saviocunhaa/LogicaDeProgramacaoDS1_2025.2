# Simule um sistema que solicita uma senha e, em seguida, um código de verificação. O login só deve ser autorizado se ambos estiverem corretos. Caso contrário, exiba uma mensagem de erro.

# Solicita senha e código de verificação
senha = input("Digite sua senha: ")
codigo = input("Digite o código de verificação: ")

# Verifica se ambos estão corretos
if senha == "admin123" and codigo == "9876":
    print("Login autorizado com sucesso!")
else:
    print("Erro: senha ou código incorreto.")
