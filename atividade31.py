# Crie um programa que permita até 3 tentativas de login. Se o usuário errar o nome ou senha três vezes, o acesso deve ser bloqueado e o programa exibirá “Usuário bloqueado por excesso de tentativas.”

# Define as credenciais corretas
usuario_correto = "admin"
senha_correta = "1234"

# Permite até 3 tentativas
tentativas = 0

while tentativas < 3:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas += 1
        print(f"Usuário ou senha incorretos. Tentativa {tentativas}/3.")

# Bloqueia após 3 erros
if tentativas == 3:
    print("Usuário bloqueado por excesso de tentativas.")
