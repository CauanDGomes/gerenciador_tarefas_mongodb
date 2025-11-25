from services.menu_ui import MenuUI
from services.relatorios import Relatorios
from controllers.usuario_controller import UsuarioController
from controllers.categoria_controller import CategoriaController
from controllers.tarefa_controller import TarefaController

class Menu:
    def __init__(self, db):
        self.ui = MenuUI()
        self.db = db
        self.usuario_ctrl = UsuarioController(db)
        self.categoria_ctrl = CategoriaController(db)
        self.tarefa_ctrl = TarefaController(db)
        self.relatorios = Relatorios(db)

    def run(self):
        while True:
            self.ui.header("SISTEMA DE GERENCIAMENTO DE TAREFAS")
            self.ui.option("1", "Relatórios")
            self.ui.option("2", "Usuários")
            self.ui.option("3", "Categorias")
            self.ui.option("4", "Tarefas")
            self.ui.option("5", "Sair")
            op = self.ui.prompt("Escolha: ").strip()
            if op == "1":
                self.relatorios.exibir_menu_relatorios()
            elif op == "2":
                self.menu_usuarios()
            elif op == "3":
                self.menu_categorias()
            elif op == "4":
                self.menu_tarefas()
            elif op == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    def menu_usuarios(self):
        self.ui.header("USUÁRIOS")
        self.ui.option("1", "Inserir usuário")
        self.ui.option("2", "Listar usuários")
        self.ui.option("3", "Remover usuário")
        self.ui.option("4", "Atualizar usuário")
        self.ui.option("5", "Voltar")
        op = self.ui.prompt("Escolha: ").strip()
        if op == "1":
            nome = self.ui.prompt("Nome: ")
            email = self.ui.prompt("Email: ")
            senha = self.ui.prompt("Senha: ")
            doc = self.usuario_ctrl.create(nome, email, senha)
            print(f"Usuário criado com id {doc['id']}")
        elif op == "2":
            for u in self.usuario_ctrl.list_all():
                print(f"{u['id']} - {u['nome']} ({u['email']})")
        elif op == "3":
            print("\n-- Usuários cadastrados no banco --")
            usuarios = list(self.usuario_ctrl.list_all())
            if usuarios:
                for u in usuarios:
                    print(f"{u['id']} - {u['nome']} ({u['email']})")
                print()
                idu = int(self.ui.prompt("ID do usuário a remover: "))
                usuario = self.usuario_ctrl.find(idu)
                if usuario:
                    print("\n-- Usuário a ser removido --")
                    print(f"ID: {usuario['id']}")
                    print(f"Nome: {usuario['nome']}")
                    print(f"Email: {usuario['email']}")
                    print()
                    qt = self.tarefa_ctrl.count_by_usuario(idu)
                    if qt > 0:
                        print(f"Usuário possui {qt} tarefa(s). Remova ou reatribua antes.")
                    else:
                        confirmar = self.ui.prompt("Tem certeza que deseja remover? (s/n): ").strip().lower() == "s"
                        if confirmar:
                            deleted = self.usuario_ctrl.delete(idu)
                            if deleted:
                                print("Usuário removido.")
                            else:
                                print("Nenhum usuário encontrado.")
                        else:
                            print("Remoção cancelada.")
                else:
                    print("Usuário não encontrado.")
            else:
                print("Nenhum usuário cadastrado.")
        elif op == "4":
            print("\n-- Usuários cadastrados no banco --")
            usuarios = list(self.usuario_ctrl.list_all())
            if usuarios:
                for u in usuarios:
                    print(f"{u['id']} - {u['nome']} ({u['email']})")
                print()
                idu = int(self.ui.prompt("ID do usuário a atualizar: "))
                usuario = self.usuario_ctrl.find(idu)
                if usuario:
                    print("\n-- Usuário atual --")
                    print(f"ID: {usuario['id']}")
                    print(f"Nome: {usuario['nome']}")
                    print(f"Email: {usuario['email']}")
                    print()
                    print("Qual campo deseja alterar?")
                    print("1. Nome")
                    print("2. Email")
                    print("3. Senha")
                    campo_op = self.ui.prompt("Escolha: ").strip()
                    
                    if campo_op == "1":
                        novo_valor = self.ui.prompt("Novo nome: ")
                        self.usuario_ctrl.update(idu, {"nome": novo_valor})
                        print("Usuário atualizado.")
                    elif campo_op == "2":
                        novo_valor = self.ui.prompt("Novo email: ")
                        self.usuario_ctrl.update(idu, {"email": novo_valor})
                        print("Usuário atualizado.")
                    elif campo_op == "3":
                        novo_valor = self.ui.prompt("Nova senha: ")
                        self.usuario_ctrl.update(idu, {"senha": novo_valor})
                        print("Usuário atualizado.")
                    else:
                        print("Opção inválida.")
                else:
                    print("Usuário não encontrado.")
            else:
                print("Nenhum usuário cadastrado.")
        elif op == "5":
            return

    def menu_categorias(self):
        self.ui.header("CATEGORIAS")
        self.ui.option("1", "Inserir categoria")
        self.ui.option("2", "Listar categorias")
        self.ui.option("3", "Remover categoria")
        self.ui.option("4", "Atualizar categoria")
        self.ui.option("5", "Voltar")
        op = self.ui.prompt("Escolha: ").strip()
        if op == "1":
            nome = self.ui.prompt("Nome: ")
            desc = self.ui.prompt("Descrição: ")
            doc = self.categoria_ctrl.create(nome, desc)
            print(f"Categoria criada com id {doc['id']}")
        elif op == "2":
            for c in self.categoria_ctrl.list_all():
                print(f"{c['id']} - {c['nome']} - {c.get('descricao','')}")
        elif op == "3":
            print("\n-- Categorias cadastradas no banco --")
            categorias = list(self.categoria_ctrl.list_all())
            if categorias:
                for c in categorias:
                    print(f"{c['id']} - {c['nome']} - {c.get('descricao','')}")
                print()
                idc = int(self.ui.prompt("ID da categoria a remover: "))
                categoria = self.categoria_ctrl.find(idc)
                if categoria:
                    print("\n-- Categoria a ser removida --")
                    print(f"ID: {categoria['id']}")
                    print(f"Nome: {categoria['nome']}")
                    print(f"Descrição: {categoria.get('descricao', 'N/A')}")
                    print()
                    qt = self.tarefa_ctrl.count_by_categoria(idc)
                    if qt > 0:
                        print(f"Categoria possui {qt} tarefa(s). Remova ou recategorize antes.")
                    else:
                        confirmar = self.ui.prompt("Tem certeza que deseja remover? (s/n): ").strip().lower() == "s"
                        if confirmar:
                            deleted = self.categoria_ctrl.delete(idc)
                            if deleted:
                                print("Categoria removida.")
                            else:
                                print("Nenhuma categoria encontrada.")
                        else:
                            print("Remoção cancelada.")
                else:
                    print("Categoria não encontrada.")
            else:
                print("Nenhuma categoria cadastrada.")
        elif op == "4":
            print("\n-- Categorias cadastradas no banco --")
            categorias = list(self.categoria_ctrl.list_all())
            if categorias:
                for c in categorias:
                    print(f"{c['id']} - {c['nome']} - {c.get('descricao','')}")
                print()
                idc = int(self.ui.prompt("ID da categoria a atualizar: "))
                categoria = self.categoria_ctrl.find(idc)
                if categoria:
                    print("\n-- Categoria atual --")
                    print(f"ID: {categoria['id']}")
                    print(f"Nome: {categoria['nome']}")
                    print(f"Descrição: {categoria.get('descricao', 'N/A')}")
                    print()
                    print("Qual campo deseja alterar?")
                    print("1. Nome")
                    print("2. Descrição")
                    campo_op = self.ui.prompt("Escolha: ").strip()
                    
                    if campo_op == "1":
                        novo_valor = self.ui.prompt("Novo nome: ")
                        self.categoria_ctrl.update(idc, {"nome": novo_valor})
                        print("Categoria atualizada.")
                    elif campo_op == "2":
                        novo_valor = self.ui.prompt("Nova descrição: ")
                        self.categoria_ctrl.update(idc, {"descricao": novo_valor})
                        print("Categoria atualizada.")
                    else:
                        print("Opção inválida.")
                else:
                    print("Categoria não encontrada.")
            else:
                print("Nenhuma categoria cadastrada.")
        elif op == "5":
            return

    def menu_tarefas(self):
        self.ui.header("TAREFAS")
        self.ui.option("1", "Inserir tarefa")
        self.ui.option("2", "Listar tarefas")
        self.ui.option("3", "Remover tarefa")
        self.ui.option("4", "Atualizar tarefa")
        self.ui.option("5", "Voltar")
        op = self.ui.prompt("Escolha: ").strip()
        if op == "1":
            titulo = self.ui.prompt("Título: ")
            descricao = self.ui.prompt("Descrição: ")
            print("-- Usuários cadastrados --")
            for u in self.usuario_ctrl.list_all():
                print(f"{u['id']} - {u['nome']}")
            id_usuario = int(self.ui.prompt("ID do usuário responsável: "))
            print("-- Categorias cadastradas --")
            for c in self.categoria_ctrl.list_all():
                print(f"{c['id']} - {c['nome']}")
            id_categoria = int(self.ui.prompt("ID da categoria: "))
            t = self.tarefa_ctrl.create(titulo, descricao, id_usuario, id_categoria)
            print(f"Tarefa criada com id {t['id']}")
        elif op == "2":
            for t in self.tarefa_ctrl.list_all():
                print(f"{t['id']} - {t['titulo']} (status: {t['status']}) - usuario:{t.get('id_usuario', 'N/A')} categoria:{t.get('categoria_id', 'N/A')}")
        elif op == "3":
            print("\n-- Tarefas cadastradas no banco --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} (status: {t['status']}) - usuario:{t.get('id_usuario', 'N/A')} categoria:{t.get('categoria_id', 'N/A')}")
                print()
                idt = int(self.ui.prompt("ID da tarefa a remover: "))
                tarefa = self.tarefa_ctrl.find(idt)
                if tarefa:
                    print("\n-- Tarefa a ser removida --")
                    print(f"ID: {tarefa['id']}")
                    print(f"Título: {tarefa['titulo']}")
                    print(f"Descrição: {tarefa.get('descricao', 'N/A')}")
                    print(f"Status: {tarefa.get('status', 'N/A')}")
                    print(f"Usuário: {tarefa.get('id_usuario', 'N/A')}")
                    print(f"Categoria: {tarefa.get('categoria_id', 'N/A')}")
                    print()
                    confirmar = self.ui.prompt("Tem certeza que deseja remover? (s/n): ").strip().lower() == "s"
                    if confirmar:
                        cascade = self.ui.prompt("Remover em cascata comentários/anexos/tempos? (s/n): ").strip().lower() == "s"
                        deleted = self.tarefa_ctrl.delete(idt, cascade=cascade)
                        if deleted:
                            print("Tarefa removida.")
                        else:
                            print("Nenhuma tarefa removida.")
                    else:
                        print("Remoção cancelada.")
                else:
                    print("Tarefa não encontrada.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "4":
            print("\n-- Tarefas cadastradas no banco --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} (status: {t['status']}) - usuario:{t.get('id_usuario', 'N/A')} categoria:{t.get('categoria_id', 'N/A')}")
                print()
                idt = int(self.ui.prompt("ID da tarefa a atualizar: "))
                tarefa = self.tarefa_ctrl.find(idt)
                if tarefa:
                    print("\n-- Tarefa atual --")
                    print(f"ID: {tarefa['id']}")
                    print(f"Título: {tarefa['titulo']}")
                    print(f"Descrição: {tarefa.get('descricao', 'N/A')}")
                    print(f"Status: {tarefa.get('status', 'N/A')}")
                    print(f"Usuário: {tarefa.get('id_usuario', 'N/A')}")
                    print(f"Categoria: {tarefa.get('categoria_id', 'N/A')}")
                    print()
                    print("Qual campo deseja alterar?")
                    print("1. Título")
                    print("2. Descrição")
                    print("3. Status")
                    print("4. Usuário Responsável")
                    print("5. Categoria")
                    campo_op = self.ui.prompt("Escolha: ").strip()
                    
                    if campo_op == "1":
                        novo_valor = self.ui.prompt("Novo título: ")
                        self.tarefa_ctrl.update(idt, {"titulo": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "2":
                        novo_valor = self.ui.prompt("Nova descrição: ")
                        self.tarefa_ctrl.update(idt, {"descricao": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "3":
                        novo_valor = self.ui.prompt("Novo status (pendente, em_andamento, concluida): ")
                        self.tarefa_ctrl.update(idt, {"status": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "4":
                        print("-- Usuários disponíveis --")
                        for u in self.usuario_ctrl.list_all():
                            print(f"{u['id']} - {u['nome']}")
                        novo_valor = int(self.ui.prompt("Novo ID do usuário: "))
                        self.tarefa_ctrl.update(idt, {"id_usuario": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "5":
                        print("-- Categorias disponíveis --")
                        for c in self.categoria_ctrl.list_all():
                            print(f"{c['id']} - {c['nome']}")
                        novo_valor = int(self.ui.prompt("Novo ID da categoria: "))
                        self.tarefa_ctrl.update(idt, {"categoria_id": novo_valor})
                        print("Tarefa atualizada.")
                    else:
                        print("Opção inválida.")
                else:
                    print("Tarefa não encontrada.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "5":
            return
