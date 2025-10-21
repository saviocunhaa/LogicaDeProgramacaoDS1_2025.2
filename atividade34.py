# Peça ao usuário um ano e verifique se ele é bissexto. (Um ano é bissexto se for divisível por 4 e não for por 100, ou se for divisível por 400.)

# Solicita o ano ao usuário
ano = int(input("Digite um ano: "))

# Verifica se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
