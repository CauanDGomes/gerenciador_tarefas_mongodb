from database.database import Database
from controllers.usuario_controller import UsuarioController
from controllers.categoria_controller import CategoriaController
from controllers.tarefa_controller import TarefaController
from controllers.comentario_controller import ComentarioController
from controllers.anexo_controller import AnexoController
from controllers.tempo_gasto_controller import TempoGastoController

class SplashScreen:
    def __init__(self, db: Database):
        self.db = db
        self.usuario_ctrl = UsuarioController(db)
        self.categoria_ctrl = CategoriaController(db)
        self.tarefa_ctrl = TarefaController(db)
        self.comentario_ctrl = ComentarioController(db)
        self.anexo_ctrl = AnexoController(db)
        self.tempo_ctrl = TempoGastoController(db)

    def display(self):
        """Exibe a tela inicial do sistema"""
        print("\n" + "=" * 70)
        print(" " * 15 + "SISTEMA DE GERENCIAMENTO DE TAREFAS")
        print("=" * 70)
        print()
        print(f"  Professor: Howard Roatti")
        print(f"  Disciplina: Banco de Dados")
        print(f"  Semestre: C3 (2025)")
        print()
        print("-" * 70)
        print("  MEMBROS DO GRUPO:")
        print("  - Amon Brandao Lares ")
        print("  - Cauan Henrique Dasmascena Gomes")
        print("  - Eduardo Rangel Malaquias Rodrigues")
        print("  - Guilherme Paiva ")
        print("  - Juliano De Andrade Dantas Rodrigues ")
        print("  - Julia Soares Gomes Paiva ")
        print("  - Ruabiale Filho")
        print("-" * 70)
        print()
        print("  DOCUMENTOS NO BANCO DE DADOS:")
        print()
        
        # Contar documentos em cada coleção
        count_usuarios = self.usuario_ctrl.count_all()
        count_categorias = self.categoria_ctrl.count_all()
        count_tarefas = self.tarefa_ctrl.count_all()
        count_comentarios = self.comentario_ctrl.count_all()
        count_anexos = self.anexo_ctrl.count_all()
        count_tempos = self.tempo_ctrl.count_all()
        
        print(f"    • Usuários:        {count_usuarios} documento(s)")
        print(f"    • Categorias:      {count_categorias} documento(s)")
        print(f"    • Tarefas:         {count_tarefas} documento(s)")
        print(f"    • Comentários:     {count_comentarios} documento(s)")
        print(f"    • Anexos:          {count_anexos} documento(s)")
        print(f"    • Tempos Gastos:   {count_tempos} documento(s)")
        print()
        print("=" * 70)
        print("  Pressione ENTER para continuar...")
        print("=" * 70)
        input()
