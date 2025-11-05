# Sistema de Avaliação Contínua
# Permita que o usuário digite notas enquanto desejar (perguntando se quer continuar).
# Ao final, exiba a média geral e quantas notas foram informadas.

# Sistema de Avaliação Contínua
soma = 0
contador = 0

while True: #aqui ele força um loop ate ele chegar no if e for aceito a condicao elel nao entra no break
    nota = float(input("Digite a nota: "))
    soma += nota
    contador += 1

    continuar = input("Deseja adicionar outra nota? (s/n): ").lower()
    if continuar != 's':
        break

media = soma / contador
print(f"\nTotal de notas: {contador}")
print(f"Média geral: {media:.2f}")
