# Controle de Tarefas de Desenvolvimento
# Peça ao usuário quantas tarefas ele precisa realizar hoje.
# Com um for, exiba “Tarefa X concluída” até todas estarem finalizadas.

# Controle de Tarefas de Desenvolvimento
qtd_tarefas = int(input("Quantas tarefas você precisa realizar hoje? "))

for i in range(1, qtd_tarefas + 1):
    print(f"Tarefa {i} concluída.")

print("✅ Todas as tarefas foram finalizadas com sucesso!")
