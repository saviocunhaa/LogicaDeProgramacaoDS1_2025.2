# Converta a tupla (5, 8, 12) em uma lista, adicione o número 20 e converta de volta em tupla.


# Tupla inicial
tupla = (5, 8, 12)

# Conversão para lista
lista = list(tupla)

# Adicionando o número 20 usamo o metodo .append
lista.append(20)

# Convertendo de volta para tupla
tupla = tuple(lista)

# Exibição do resultado
print("Tupla final:", tupla)
