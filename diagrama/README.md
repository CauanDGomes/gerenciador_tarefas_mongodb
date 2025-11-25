# Diagrama Relacional

Este diretório deve conter o diagrama relacional do projeto em formato PNG ou JPG.

## Descrição do Modelo

O projeto possui as seguintes entidades:

### USUÁRIO
- **id** (int, PK)
- **nome** (string)
- **email** (string)
- **senha** (string)
- **data_cadastro** (date)

### CATEGORIA
- **id** (int, PK)
- **nome** (string)
- **descricao** (string)

### TAREFA
- **id** (int, PK)
- **titulo** (string)
- **descricao** (string)
- **status** (string): pendente, em_andamento, concluida
- **prioridade** (int)
- **data_criacao** (date)
- **data_limite** (date)
- **data_conclusao** (date)
- **id_usuario** (int, FK) → USUÁRIO.id
- **categoria_id** (int, FK) → CATEGORIA.id

### COMENTARIO
- **id** (int, PK)
- **texto** (string)
- **data_comentario** (date)
- **tarefa_id** (int, FK) → TAREFA.id
- **usuario_id** (int, FK) → USUÁRIO.id

### ANEXO
- **id** (int, PK)
- **nome_arquivo** (string)
- **tipo_arquivo** (string)
- **caminho** (string)
- **tarefa_id** (int, FK) → TAREFA.id

### TEMPO_GASTO
- **id** (int, PK)
- **horas** (float)
- **data_registro** (date)
- **tarefa_id** (int, FK) → TAREFA.id

## Relacionamentos

- USUÁRIO (1) ----< (N) TAREFA
- USUÁRIO (1) ----< (N) COMENTARIO
- CATEGORIA (1) ----< (N) TAREFA
- TAREFA (1) ----< (N) COMENTARIO
- TAREFA (1) ----< (N) ANEXO
- TAREFA (1) ----< (N) TEMPO_GASTO
