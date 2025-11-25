# 📹 GUIA PARA VÍDEO DEMONSTRATIVO

## Pré-requisitos
- MongoDB rodando em `mongodb://localhost:27017/`
- Python 3.9+
- Dependências instaladas: `pip install -r requirements.txt`

## Passo a Passo para Gravar o Vídeo

### 1️⃣ Limpar e Preparar o Banco
```powershell
python scripts/limpar_banco.py
python scripts/popular_exemplo.py
```

Isso criará dados de exemplo:
- **3 Usuários**: João, Maria, Pedro
- **4 Categorias**: Trabalho, Estudos, Pessoal, Projeto
- **4 Tarefas**: Com diferentes status (pendente, em andamento, concluída)
- **3 Comentários**: Nas tarefas
- **2 Anexos**: Documentos
- **5 Registros de Tempo**: Horas gastas

---

## 🎬 ROTEIRO DO VÍDEO

### CENA 1: INICIALIZAÇÃO (30 segundos)
```
1. Abra PowerShell
2. Navegue para o projeto
3. Execute: python main.py
4. Mostre a SPLASH SCREEN com informações do sistema
   - Nomes dos membros do grupo
   - Contagem de documentos no banco
5. Pressione ENTER para continuar
```

### CENA 2: MENU PRINCIPAL (1 minuto)
```
1. Mostre o MENU PRINCIPAL com 8 opções
2. Explique brevemente cada opção
3. Teste a VALIDAÇÃO: pressione ENTER sem digitar
4. Veja mensagem de erro: "Opção inválida!"
5. Digite 1 para acessar RELATÓRIOS
```

### CENA 3: RELATÓRIOS (2 minutos)
```
1. Acesse: Menu Principal → Relatório (opção 1)
2. EXECUTE RELATÓRIO 1: "Tarefas por Usuário"
   - Mostre: João com 2 tarefas (1 pendente, 1 em andamento)
   - Mostre: Maria com 1 tarefa (pendente)
   - Mostre: Pedro com 1 tarefa (pendente)
   - Demonstre: Agregação/Sumarização com $group

3. EXECUTE RELATÓRIO 2: "Tarefas por Categoria"
   - Mostre: Categoria "Projeto" com 3 tarefas
   - Demonstre: Agrupamento por categoria

4. EXECUTE RELATÓRIO 3: "Tarefas com Detalhes"
   - Mostre: Dados de usuário, categoria e comentários juntos
   - Demonstre: $lookup entre múltiplas coleções
```

### CENA 4: USUÁRIOS - LISTAR (30 segundos)
```
1. Volte ao Menu Principal
2. Acesse: Usuários (opção 2)
3. Escolha: Listar usuários (opção 2)
4. Mostre: 3 usuários criados
```

### CENA 5: USUÁRIOS - INSERIR (45 segundos)
```
1. Menu Principal → Usuários (opção 2)
2. Escolha: Inserir usuário (opção 1)
3. Digite:
   - Nome: "Ana Costa"
   - Email: "ana@email.com"
   - Senha: "senha789"
4. Mostre: "Usuário criado com id 4"
```

### CENA 6: USUÁRIOS - ATUALIZAR (1 minuto)
```
1. Menu Principal → Usuários (opção 2)
2. Escolha: Atualizar usuário (opção 4)
3. Selecione: ID 4 (Ana Costa)
4. Mostre dados atuais
5. Escolha campo: 1 (Nome)
6. Digite novo nome: "Ana Silva Costa"
7. Mostre: "Usuário atualizado"
```

### CENA 7: CATEGORIAS (45 segundos)
```
1. Menu Principal → Categorias (opção 3)
2. Escolha: Listar (opção 2)
3. Mostre: 4 categorias
4. Escolha: Inserir (opção 1)
5. Digite:
   - Nome: "Urgente"
   - Descrição: "Tarefas urgentes"
6. Mostre: "Categoria criada"
```

### CENA 8: TAREFAS - LISTAR (30 segundos)
```
1. Menu Principal → Tarefas (opção 4)
2. Escolha: Listar tarefas (opção 2)
3. Mostre: 4 tarefas com status e relacionamentos
```

### CENA 9: TAREFAS - INSERIR (1 minuto)
```
1. Menu Principal → Tarefas (opção 4)
2. Escolha: Inserir (opção 1)
3. Digite:
   - Título: "Revisar código"
   - Descrição: "Fazer code review da API"
4. Selecione Usuário: 1 (João)
5. Selecione Categoria: 4 (Projeto)
6. Mostre: "Tarefa criada"
```

### CENA 10: TAREFAS - ATUALIZAR COM STATUS (1 minuto)
```
1. Menu Principal → Tarefas (opção 4)
2. Escolha: Atualizar (opção 4)
3. Selecione: ID 5 (tarefa recém criada)
4. Mostre dados atuais
5. Escolha campo: 3 (Status)
6. Digite: E (ou em_andamento)
7. Mostre: "✅ Validação aceita: P, E ou C"
8. Mostre: "Tarefa atualizada"
```

### CENA 11: TAREFAS - REMOVER (1 minuto)
```
1. Menu Principal → Tarefas (opção 4)
2. Escolha: Remover (opção 3)
3. Selecione: ID 2 (qualquer tarefa)
4. Mostre dados completos
5. Escolha: s (Sim, remover)
6. Escolha: s (Remover em cascata)
7. Mostre: "Tarefa removida"
```

### CENA 12: COMENTÁRIOS (1 minuto)
```
1. Menu Principal → Comentários (opção 5)
2. Escolha: Listar (opção 2)
3. Selecione: ID 1 (primeira tarefa)
4. Mostre: Comentários existentes
5. Escolha: Inserir (opção 1)
6. Selecione: Tarefa 1, Usuário 1
7. Digite: "Ótimo progresso!"
8. Mostre: "Comentário criado"
```

### CENA 13: ANEXOS (1 minuto)
```
1. Menu Principal → Anexos (opção 6)
2. Escolha: Listar (opção 2)
3. Selecione: ID 1
4. Mostre: Anexos
5. Escolha: Inserir (opção 1)
6. Selecione: Tarefa 1
7. Digite:
   - Nome: "documento.pdf"
   - Tipo: ".pdf"
   - Caminho: "/docs/documento.pdf"
8. Mostre: "Anexo criado"
```

### CENA 14: TEMPOS GASTOS (1 minuto)
```
1. Menu Principal → Tempos Gastos (opção 7)
2. Escolha: Listar (opção 2)
3. Selecione: ID 1
4. Mostre: Tempos e total de horas
5. Escolha: Inserir (opção 1)
6. Selecione: Tarefa 1
7. Digite: 3.5 horas
8. Mostre: Total atualizado
```

### CENA 15: VALIDAÇÃO DE INTEGRIDADE (1 minuto)
```
1. Menu Principal → Usuários (opção 2)
2. Escolha: Remover (opção 3)
3. Selecione: ID 1 (João - tem tarefas)
4. Mostre: Mensagem de erro
   "Usuário possui X tarefa(s). Remova ou reatribua antes."
5. Isso demonstra validação de integridade referencial
```

### CENA 16: FINALIZAÇÃO (30 segundos)
```
1. Menu Principal → Sair (opção 8)
2. Mostre: "Saindo..."
3. Programa encerra
```

---

## ⏱️ TEMPO TOTAL: ~15 minutos

## 📊 PONTOS A DEMONSTRAR

✅ **Relatórios (1.5 pontos)**
- Sumarização: Tarefas por Usuário
- Sumarização: Tarefas por Categoria
- Junção de Coleções: Usuário + Categoria + Comentários

✅ **CRUD (4.5 pontos)**
- Inserir (Usuários, Categorias, Tarefas, Comentários, Anexos, Tempos)
- Listar (Todas as entidades)
- Atualizar (Escolha de campo)
- Remover (Com confirmação e cascata)

✅ **Interface (0.5 pontos)**
- Menus formatados
- Cores com colorama
- Validação com mensagens claras

✅ **Integridade (0.5 pontos)**
- Não remove usuário/categoria com tarefas
- Remoção em cascata de dados relacionados

✅ **Validação (Bônus)**
- Rejeita Enter vazio
- Rejeita opções inválidas
- Aceita abreviações (P/E/C para status)

---

## 🎥 DICAS PARA GRAVAÇÃO

1. Use zoom de tela (150-175%) para melhor visualização
2. Deixe background calmo/branco
3. Fale claramente sobre o que está fazendo
4. Pause 2 segundos antes de mudança de cena
5. Mostre a validação de entrada algumas vezes
6. Demonstre os 3 tipos de relatório completamente
7. Tempo ideal: 10-15 minutos

---

## 📝 SCRIPT DE NARRAÇÃO (EXEMPLO)

```
"Bem-vindos à demonstração do Sistema de Gerenciamento de Tarefas
desenvolvido em Python com MongoDB. Este sistema oferece uma interface
amigável para gerenciar usuários, categorias, tarefas, comentários,
anexos e tempos gastos.

Primeiro, vemos a tela de splash com informações dos membros do grupo
e documentação no banco de dados...

Agora acessamos o menu principal com 8 opções diferentes...

Vamos começar explorando os RELATÓRIOS que utilizam agregação
MongoDB ($group) e junção de coleções ($lookup)...

Depois vamos testar o CRUD completo com inserção, listagem,
atualização e remoção, demonstrando validação de integridade...

Finalmente, vamos explorar comentários, anexos e tempos gastos,
mostrando como tudo está conectado e funcionando em conjunto."
```

---

Bom vídeo! 🎬
