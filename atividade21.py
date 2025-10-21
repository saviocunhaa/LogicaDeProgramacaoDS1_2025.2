# Em um sistema de gestão, apenas usuários com o perfil "Administrador" podem acessar o painel de configurações. Peça ao usuário para digitar seu perfil e exiba se ele tem permissão ou não para acessar.

# Solicita o perfil do usuário
perfil = input("Digite seu perfil de usuário: ")

# Verifica se o usuário tem permissão
if perfil == "Administrador":
    print("Acesso permitido ao painel de configurações.")
else:
    print("Acesso negado. Apenas Administradores podem acessar.")


# ✅ Dica:
# Você pode usar perfil.capitalize() ou perfil.lower() para deixar a verificação mais flexível, por exemplo:
# if perfil.lower() == "administrador":
#     print("Acesso permitido ao painel de configurações.")
# else:
#     print("Acesso negado. Apenas Administradores podem acessar.")
