class Tarefa:
    def __init__(self, id, descricao, concluido=False):
        self.id = id
        self.descricao = descricao
        self.concluido = concluido

tarefas = []


def addTarefa(descricao):
    id = len(tarefas) + 1
    nova_tarefa = Tarefa(id, descricao)
    tarefas.append(nova_tarefa)
    