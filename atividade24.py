# Validação de Acesso a um Sistema Interno
# Peça o cargo e o turno do funcionário.
# Apenas administradores que trabalham no turno da manhã podem acessar o painel de controle.
# Use operadores lógicos para validar.
# Use operadores lógicos para validar.

# Solicita o cargo e o turno do funcionário
cargo = input("Digite seu cargo: ").lower()
turno = input("Digite seu turno (manhã, tarde ou noite): ").lower()

# Valida o acesso com operadores lógicos
if cargo == "administrador" and turno == "manhã":
    print("Acesso permitido ao painel de controle.")
else:
    print("Acesso negado. Apenas administradores do turno da manhã podem acessar.")
