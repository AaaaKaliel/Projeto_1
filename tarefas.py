def adicionar(tarefas,titulo):       
        novas_tarefas = tarefas.copy()
        novas_tarefas.append(titulo)
        return novas_tarefas

l = ["kaliel"]

print(adicionar(l,"mickael"))
print(l)