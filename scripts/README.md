# 🧹 SCRIPTS DE LIMPEZA E POPULAÇÃO

## Para Limpar o Banco de Dados

Execute este comando para **REMOVER TODOS OS DADOS**:

```powershell
python scripts/limpar_banco.py
```

**O que faz:**
- ✅ Remove todos os usuários
- ✅ Remove todas as categorias
- ✅ Remove todas as tarefas
- ✅ Remove todos os comentários
- ✅ Remove todos os anexos
- ✅ Remove todos os tempos gastos
- ✅ Reseta os contadores

---

## Para Popular com Dados de Exemplo

Depois de limpar, execute:

```powershell
python scripts/popular_exemplo.py
```

**O que cria:**
- **3 Usuários:**
  - João Silva (joao@email.com)
  - Maria Santos (maria@email.com)
  - Pedro Oliveira (pedro@email.com)

- **4 Categorias:**
  - Trabalho
  - Estudos
  - Pessoal
  - Projeto

- **4 Tarefas:**
  - "Implementar API REST" - EM ANDAMENTO (João, Projeto)
  - "Estudar MongoDB" - PENDENTE (Maria, Estudos)
  - "Fazer apresentação" - CONCLUÍDA (João, Projeto)
  - "Reunião com cliente" - PENDENTE (Pedro, Trabalho)

- **3 Comentários:**
  - Nas tarefas 1 e 2

- **2 Anexos:**
  - requisitos_api.pdf
  - slides_c3.pptx

- **5 Registros de Tempo:**
  - Distribuídos nas tarefas

---

## Sequência Recomendada

```powershell
# 1. Limpar banco
python scripts/limpar_banco.py

# 2. Popular com exemplos
python scripts/popular_exemplo.py

# 3. Rodar o programa
python main.py
```

---

## Para Vídeo Demonstrativo

Veja o arquivo `GUIA_VIDEO_DEMO.md` para:
- ✅ Roteiro completo
- ✅ Exemplos de dados
- ✅ Pontos a demonstrar
- ✅ Dicas de gravação
- ✅ Script de narração

---

**Nota:** Certifique-se de que MongoDB está rodando antes de executar os scripts!
