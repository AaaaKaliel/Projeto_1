def adicionar(tarefas,titulo):       
        novas_tarefas = tarefas.copy()
        novas_tarefas.append(titulo)
        return novas_tarefas



def test_adicionar_nao_altera_original():
    original = ["kaliel"]
    copia = original.copy()

    resultado = adicionar(original, "mickael")

    assert resultado == ["kaliel", "mickael"]
    assert original == copia