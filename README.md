# Lista de tarefas em Python

Projeto simples para praticar funções, listas e dicionários em Python.
As tarefas possuem um título e um status, que pode ser `pendente` ou
`concluido`.

## Funcionalidades

- Adicionar uma tarefa sem alterar a lista original.
- Listar as tarefas em formato de texto.
- Concluir uma tarefa pelo título.

## Estrutura do projeto

```text
.
├── tarefas.py       # Funções e exemplos de uso
├── test_tarefas.py  # Teste automatizado da função adicionar
├── dict.py          # Exemplo de uma lista de tarefas com dicionários
└── README.md
```

## Requisitos

- Python 3.8 ou superior
- `pytest` para executar os testes

## Como executar

```bash
python tarefas.py
```

O arquivo contém exemplos de chamada e imprime os resultados no terminal.

Para executar os testes:

```bash
python -m pytest
```

Caso o `pytest` ainda não esteja instalado:

```bash
python -m pip install pytest
```

## Exemplo de uso

```python
from tarefas import adicionar, concluir, listar

tarefas = [{"titulo": "estudar SQL", "status": "pendente"}]

tarefas = adicionar(tarefas, "revisar PR")
tarefas = concluir(tarefas, "estudar SQL")

print(listar(tarefas))
```

Saída esperada:

```text
estudar SQL - concluido
revisar PR - pendente
```
