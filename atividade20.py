# crie um programa que solicite ao usuário um nome e uma senha. Se o nome for "admin" e a senha for "1234", mostre a mensagem “Login realizado com sucesso!”. Caso contrário, exiba “Usuário ou senha incorretos.”


# Solicita o nome e a senha do usuário
nome = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verifica se as credenciais estão corretas
if nome == "admin" and senha == "1234":
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")
