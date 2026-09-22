def adicionar(tarefas,titulo):       
        novas_tarefas = tarefas.copy()
        novas_tarefas.append({"titulo" : titulo, "status": "pendente"})
        return novas_tarefas

tarefas = [{"titulo":"estudar SQL","status" : "pendente"}, {"titulo": "revisar PR", "status" : "pendente"}]

def listar(tarefas):
        lista = []
        for tarefa in tarefas:
                lista.append(tarefa["titulo"] + " - " + tarefa["status"])
        return '\n'.join(lista)

def concluir(tarefas, titulo):
        tarefas_concluidas = []
        for tarefa in tarefas:
                if tarefa["titulo"] == titulo:
                        tarefas_concluidas.append({"titulo" : titulo, "status": "concluido"})
                else:
                        tarefas_concluidas.append(tarefa)
        return tarefas_concluidas


print(adicionar(tarefas,"mickael"))
print(tarefas)
print(concluir(tarefas,"estudar SQL"))
print(listar(tarefas))