# Peça ao usuário que digite uma linguagem de programação (Python, Java ou C#). Exiba uma breve descrição sobre o uso dessa linguagem, como “Python é muito usado em IA e análise de dados.”

# Solicita a linguagem de programação
linguagem = input("Digite uma linguagem de programação (Python, Java ou C#): ").lower()

# Exibe a descrição de acordo com a linguagem
if linguagem == "python":
    print("Python é muito usado em IA, automação e análise de dados.")
elif linguagem == "java":
    print("Java é amplamente usado em sistemas corporativos e aplicativos Android.")
elif linguagem == "c#":
    print("C# é muito utilizado no desenvolvimento de jogos e aplicações Windows.")
else:
    print("Linguagem não reconhecida.")
