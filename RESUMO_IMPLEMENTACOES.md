# RESUMO DAS IMPLEMENTAÇÕES - PROJETO C3

## ✅ Implementações Completadas

### 1. **Splash Screen** (0.5 pontos no edital)
- ✅ Arquivo criado: `services/splash_screen.py`
- ✅ Exibe o nome da aplicação
- ✅ Exibe nomes dos componentes do grupo (ordem alfabética por primeiro nome): Amon Brandao Lares (amonLares); Cauan Henrique Dasmascena Gomes; Eduardo Rangel Malaquias Rodrigues; Guilherme Paiva (@GuilhermeDSpaiva); Juliano De Andrade Dantas Rodrigues (JulianoDADR); Julia Soares Gomes Paiva (@juuuhhhhhhh); Ruabiale Filho (rubiale18)
- ✅ Exibe professor (Howard Roatti), disciplina (Banco de Dados) e semestre (C3/2023)
- ✅ Conta e exibe número de documentos em cada coleção
- ✅ Integrada ao `main.py` - exibida no início
- **Como funciona**: Ao iniciar o programa, exibe a splash screen com informações antes do menu principal

### 2. **Relatórios** (1.5 pontos no edital)
Arquivo: `services/relatorios.py`

#### Relatório 1: Sumarização com Group By (1.0 ponto)
- **Tarefas por Usuário**: Usa `$group` do MongoDB para agrupar tarefas por usuário
  - Mostra: total de tarefas, pendentes, em_andamento, concluídas
- **Tarefas por Categoria**: Agrupa por categoria com mesmas contagens
- Utiliza aggregation pipeline do MongoDB

#### Relatório 2: Junção de Coleções (0.5 pontos)
- **Tarefas com Detalhes**: Usa `$lookup` para juntar:
  - Tarefas + Usuários (nome do responsável)
  - Tarefas + Categorias (nome da categoria)
  - Tarefas + Comentários (total de comentários)
- Mostra os dados de forma formatada e legível

### 3. **Menu de Relatórios Integrado** (edital 7.a)
- ✅ Submenu de relatórios no menu principal
- ✅ Opções claras para escolher qual relatório ver
- ✅ Retorna ao menu principal após cada relatório

### 4. **Operações CRUD Melhoradas** (edital 6.c e 6.d)

#### Remover Documentos (1.0 + 0.5 pontos)
- ✅ Sempre mostra lista completa antes de remover (exigência do usuário)
- ✅ Exibe dados do documento a ser removido
- ✅ Solicita confirmação (s/n)
- ✅ Verifica integridade referencial:
  - Usuário com tarefas não pode ser removido
  - Categoria com tarefas não pode ser removida
- ✅ Remoção em cascata para tarefas (comentários, anexos, tempos)
- Implementado para: Usuários, Categorias e Tarefas

#### Atualizar Documentos (1.0 + 0.5 pontos)
- ✅ Sempre mostra lista completa antes de atualizar (exigência do usuário)
- ✅ Exibe dados atuais do documento
- ✅ Permite escolher qual campo deseja alterar (não apenas status)

**Usuários - Campos atualizáveis:**
- Nome
- Email
- Senha

**Categorias - Campos atualizáveis:**
- Nome
- Descrição

**Tarefas - Campos atualizáveis:**
- Título
- Descrição
- Status
- Usuário Responsável (com listagem de usuários)
- Categoria (com listagem de categorias)

### 5. **Contagem de Documentos** (edital 6.c)
- ✅ Método `count_all()` adicionado a todos os controllers
- ✅ Usado pela splash screen para exibir total de documentos
- ✅ Exibido na tela inicial

### 6. **Documentação** (0.5 pontos no edital)
- ✅ `README.md` completamente atualizado com:
  - Instruções para Linux (bash)
  - Instruções para Windows PowerShell
  - Estrutura do projeto
  - Funcionalidades descritas
  - Informações do banco de dados
  - Relacionamentos entre coleções
  - Notas importantes

### 7. **Estrutura do Projeto**
- ✅ Pasta `/diagrama` criada para armazenar diagrama relacional
- ✅ Arquivo `INSTRUCOES_ENTREGA.md` com checklist de entrega
- ✅ Todos os arquivos organizados e funcionais

---

## 📊 Mapeamento para o Edital

### Item 6 - Menu Principal
- ✅ 6.a.i - Relatórios (implementado)
- ✅ 6.a.ii - Inserir, Remover, Atualizar documentos (implementado)
- ✅ 6.a.iii - Sair (implementado)
- ✅ 6.b - Splash Screen com nomes do grupo (implementado)
- ✅ 6.c - Contagem de documentos em cada coleção (implementado)

### Item 7 - Funcionalidades dos Menus
- ✅ 7.a - Relatórios com 2 opções (sumarização e junção)
- ✅ 7.b - Inserir documentos (já estava, não alterado)
- ✅ 7.c - Remover documentos com lista prévia e confirmação
- ✅ 7.d - Atualizar documentos com escolha de campo

### Item 8 - Entregáveis
- ✅ 8.a.ii - Código fonte organizado (completo)
- ✅ 8.a.v - README.MD com instruções Linux (completo)
- ⚠️ 8.a.iii - Diagrama relacional (pasta criada, precisa adicionar arquivo PNG/JPG)
- ⚠️ 8.a.iv - Vídeo demonstrativo (pendente - precisa gravar)

---

## 🔧 Melhorias Implementadas além do Edital

1. **Interface amigável** com cabeçalhos formatados
2. **Validação de integridade referencial** (não permite remover usuário/categoria com tarefas)
3. **Remoção em cascata** opcional para tarefas
4. **Menu de seleção de campo** ao atualizar (não força todos os campos)
5. **Lista prévia obrigatória** antes de remover/atualizar (conforme pedido pelo usuário)

---

## 📝 Como Usar o Sistema

### Iniciar o programa
```bash
python main.py
```

### Fluxo típico
1. Splash Screen aparece (mostra documentos do BD)
2. Menu principal com opções
3. Selecionar "Relatórios" para ver consultas com agregação
4. Selecionar "Usuários/Categorias/Tarefas" para CRUD
5. Sempre vê lista antes de remover/atualizar

### Exemplo de Uso
1. Criar usuário → Menu Usuários → 1 (Inserir)
2. Criar categoria → Menu Categorias → 1 (Inserir)
3. Criar tarefa → Menu Tarefas → 1 (Inserir) → Escolhe usuário e categoria
4. Ver relatórios → Menu Principal → 1 (Relatórios) → Escolhe qual
5. Atualizar tarefa → Menu Tarefas → 4 (Atualizar) → Escolhe qual campo

---

## 🚀 Proximas Etapas para Entrega

1. **Salvar o diagrama enviado** como PNG/JPG
2. **Copiar para**: `c:\Users\cauan\...\projeto_C3\diagrama\diagrama_relacional.png`
3. **Gravar vídeo demonstrativo** mostrando:
   - Inicialização (splash screen)
   - Menu de relatórios (os 2 relatórios funcionando)
   - Inserção de dados
   - Listagem de dados
   - Remoção com confirmação
   - Atualização com escolha de campo
   - Integridade referencial em ação
4. **Fazer commit e push** no GitHub
5. **Preencher relatório** na plataforma AVA

---

## ✓ Status Final: PRONTO PARA VALIDAÇÃO

Todos os items críticos do edital foram implementados!
Apenas faltam: Diagrama (arquivo) e Vídeo (gravação)
