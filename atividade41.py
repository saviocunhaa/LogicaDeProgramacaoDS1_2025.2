# Validação de Login com While
# Permita que o usuário tente fazer login até digitar a senha correta ("1234"). Mostre uma mensagem de erro a cada tentativa incorreta.

# Validação de Login com While
senha_correta = "1234"
senha = input("digite a senha")

while senha != senha_correta:
    senha = input("Digite a senha: ")
    if senha != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("Login realizado com sucesso!")
