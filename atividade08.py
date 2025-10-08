# Atividade 08

# Peça ao usuário:
# Nome
# Ano de nascimento
# Calcule sua idade aproximada e mostre a mensagem:
# ___, você tem ___ anos.


# Entrada de dados
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Cálculo da idade aproximada
ano_atual = 2025
idade = ano_atual - ano_nascimento

# Exibição da mensagem
print(f"{nome}, você tem aproximadamente {idade} anos.")


# #dica, existe uma chamada de biblioteca que pode ser usada dentro do python onde ja pega a data ou ano atual automatico

#essa linha adiciona no inicio do codigo 
# from datetime import date 

#essa linha seria para pegar o ano atual automaticamente 
# ano_atual = date.today().year


