# Sistema de Avaliação de Software
# Peça três notas (usabilidade, desempenho e segurança).
# O sistema será Aprovado se todas as notas forem ≥ 7.
# Se pelo menos uma for menor que 5, exiba “Reprovado”.
# Caso contrário, exiba “Necessita melhorias”.

# Solicita as notas do sistema
usabilidade = float(input("Digite a nota de usabilidade: "))
desempenho = float(input("Digite a nota de desempenho: "))
seguranca = float(input("Digite a nota de segurança: "))

# Verifica as condições
if usabilidade >= 7 and desempenho >= 7 and seguranca >= 7:
    print("Sistema Aprovado.")
elif usabilidade < 5 or desempenho < 5 or seguranca < 5:
    print("Reprovado.")
else:
    print("Necessita melhorias.")
