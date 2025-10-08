# Crie um dicionário chamado notas com as chaves: Matemática, Português, História. Atribua valores (notas) e exiba a média.



# Criação do dicionário
notas = {
    "Matemática": 8.5,
    "Português": 7.0,
    "História": 9.0
}

# Cálculo da média, 
# esse sum() e uma funcao do payton que faz a soma automatica 
# esse .values() e uma funcao que tras somente os valores das chaves
# esse len() e uma funcao que tras o tamanho da lista, tupla ou dicionario (quantidade de itens dentro) nesse caso o len() 
media = sum(notas.values()) / len(notas)

# Exibição dos resultados
print("Notas:", notas)
print(f"Média das notas: {media:.2f}")
