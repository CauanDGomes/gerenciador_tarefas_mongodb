# Gerenciador de Tarefas - MongoDB (C3)

Sistema de Gerenciamento de Tarefas desenvolvido em Python com MongoDB, integrando linguagem de programação com banco de dados não relacional.

## Requisitos
- Python 3.8 ou superior
- MongoDB 4.0 ou superior
- pip (gerenciador de pacotes Python)

## Como rodar no Linux

### 1. Instale as dependências do sistema
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv mongodb

# Fedora/CentOS
sudo dnf install python3 python3-pip python3-venv mongodb

# Arch
sudo pacman -S python pip mongodb
```

### 2. Inicie o MongoDB (em um terminal separado)
```bash
# Se MongoDB está instalado como serviço
sudo systemctl start mongodb
# ou
sudo service mongodb start

# Ou inicie manualmente
mongod
```

### 3. Configure o ambiente Python
```bash
# Navegue até a pasta do projeto
cd projeto_C3

# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows PowerShell
```

### 4. Instale as dependências do projeto
```bash
pip install -r requirements.txt
```

### 5. Crie as coleções no MongoDB
```bash
# Use mongosh para executar o script
mongosh < scripts/create_collections.js

# Ou copie e cole os comandos do script no mongosh interativo
mongosh
# Depois copie o conteúdo de scripts/create_collections.js
```

### 6. Execute a aplicação
```bash
python main.py
```

## Como rodar no Windows PowerShell

1. Instale Python: https://www.python.org/downloads/
2. Instale MongoDB: https://www.mongodb.com/try/download/community
3. Inicie o MongoDB (geralmente como serviço do Windows)
4. No PowerShell:
```powershell
cd projeto_C3
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Estrutura do Projeto

```
projeto_C3/
├── main.py                          # Arquivo principal
├── requirements.txt                 # Dependências
├── README.md                        # Documentação
├── controllers/                     # Controladores (interface com BD)
│   ├── usuario_controller.py
│   ├── categoria_controller.py
│   ├── tarefa_controller.py
│   ├── comentario_controller.py
│   ├── anexo_controller.py
│   └── tempo_gasto_controller.py
├── models/                          # Modelos de dados
│   ├── usuario.py
│   ├── categoria.py
│   ├── tarefa.py
│   ├── comentario.py
│   ├── anexo.py
│   └── tempo_gasto.py
├── database/                        # Configuração do banco
│   └── database.py
├── services/                        # Serviços (menu, relatórios, etc)
│   ├── menu.py
│   ├── menu_ui.py
│   ├── splash_screen.py
│   └── relatorios.py
└── scripts/                         # Scripts de inicialização
    └── create_collections.js        # Script para criar coleções
```

## Funcionalidades

### Menu Principal
- **Relatórios**: Consultas com sumarização e junção de coleções
- **Usuários**: Inserir, listar, remover e atualizar usuários
- **Categorias**: Inserir, listar, remover e atualizar categorias
- **Tarefas**: Inserir, listar, remover e atualizar tarefas

### Relatórios Disponíveis
1. **Tarefas por Usuário**: Sumarização com contagem de tarefas por status
2. **Tarefas por Categoria**: Sumarização com contagem de tarefas por status
3. **Tarefas com Detalhes**: Junção de coleções (Tarefas + Usuários + Categorias + Comentários)

### Operações CRUD
- **Inserir**: Cria novos documentos nas coleções
- **Listar**: Exibe todos os documentos de uma coleção
- **Remover**: Deleta documentos com confirmação e remoção em cascata (para tarefas)
- **Atualizar**: Modifica campos específicos de documentos

## Banco de Dados

### Coleções
- **usuarios**: Usuários do sistema
- **categorias**: Categorias de tarefas
- **tarefas**: Tarefas com relacionamento usuário e categoria
- **comentarios**: Comentários em tarefas
- **anexos**: Anexos de tarefas
- **tempos_gastos**: Registro de horas gastas em tarefas

### Relacionamentos
- Usuário → Tarefas (um usuário pode ter várias tarefas)
- Categoria → Tarefas (uma categoria pode ter várias tarefas)
- Tarefa → Comentários (uma tarefa pode ter vários comentários)
- Tarefa → Anexos (uma tarefa pode ter vários anexos)
- Tarefa → Tempos Gastos (uma tarefa pode ter vários registros de tempo)

## Informações do Projeto

- **Disciplina**: Banco de Dados
- **Professor**: Howard Roatti
- **Semestre**: C3 (2023)
- **Banco de Dados**: MongoDB
- **Linguagem**: Python 3.8+

## Notas Importantes

- O MongoDB deve estar rodando antes de executar a aplicação
- O arquivo `create_collections.js` deve ser executado uma única vez para criar as coleções
- O banco de dados padrão é `sistema_tarefas` e pode ser modificado em `database/database.py`
- Todas as operações de remoção pedem confirmação do usuário
- Tarefas podem ser removidas em cascata com seus comentários, anexos e tempos gastos
