# Faça um dicionário com 3 frutas e seus respectivos preços. Depois, peça ao usuário para digitar o nome de uma fruta e exiba o preço correspondente.

# Atividade – Dicionário de Frutas e Preços

# Criação do dicionário
frutas = {
    "maçã": 3.50,
    "banana": 2.00,
    "laranja": 4.00
}

# Entrada do usuário
fruta_escolhida = input("Digite o nome de uma fruta: ").lower()

# Exibição do preço
# aqui ele faz um processo de comparacao do que a pessoa digitou dentro do que ja existe no dicionario 
if fruta_escolhida in frutas:
    print(f"O preço da {fruta_escolhida} é R$ {frutas[fruta_escolhida]:.2f}")
else:
    print("Desculpe, essa fruta não está na lista.")
