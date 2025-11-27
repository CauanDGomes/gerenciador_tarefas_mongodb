from services.menu_ui import MenuUI
from services.relatorios import Relatorios
from controllers.usuario_controller import UsuarioController
from controllers.categoria_controller import CategoriaController
from controllers.tarefa_controller import TarefaController
from controllers.comentario_controller import ComentarioController
from controllers.anexo_controller import AnexoController
from controllers.tempo_gasto_controller import TempoGastoController

# Menu para o controle das funções
class Menu:
    def __init__(self, db):
        self.ui = MenuUI()
        self.db = db
        self.usuario_ctrl = UsuarioController(db)
        self.categoria_ctrl = CategoriaController(db)
        self.tarefa_ctrl = TarefaController(db)
        self.comentario_ctrl = ComentarioController(db)
        self.anexo_ctrl = AnexoController(db)
        self.tempo_ctrl = TempoGastoController(db)
        self.relatorios = Relatorios(db)

    def run(self):
        while True:
            self.ui.header("SISTEMA DE GERENCIAMENTO DE TAREFAS")
            self.ui.option("1", "Relatórios")
            self.ui.option("2", "Usuários")
            self.ui.option("3", "Categorias")
            self.ui.option("4", "Tarefas")
            self.ui.option("5", "Comentários")
            self.ui.option("6", "Anexos")
            self.ui.option("7", "Tempos Gastos")
            self.ui.option("8", "Sair")
            op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4", "5", "6", "7", "8"])
            if op == "1":
                self.relatorios.exibir_menu_relatorios()
            elif op == "2":
                self.menu_usuarios()
            elif op == "3":
                self.menu_categorias()
            elif op == "4":
                self.menu_tarefas()
            elif op == "5":
                self.menu_comentarios()
            elif op == "6":
                self.menu_anexos()
            elif op == "7":
                self.menu_tempos_gastos()
            elif op == "8":
                print("Saindo...")
                break

    def menu_usuarios(self):
        self.ui.header("USUÁRIOS")
        self.ui.option("1", "Inserir usuário")
        self.ui.option("2", "Listar usuários")
        self.ui.option("3", "Remover usuário")
        self.ui.option("4", "Atualizar usuário")
        self.ui.option("5", "Voltar")
        op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4", "5"])
        if op == "1":
            nome = self.ui.prompt_required("Nome: ")
            email = self.ui.prompt_required("Email: ")
            senha = self.ui.prompt_required("Senha: ")
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
                idu = int(self.ui.prompt_required("ID do usuário a remover: "))
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
                        confirmar = self.ui.prompt_choice("Tem certeza que deseja remover? (s/n): ", ["s", "n"]) == "s"
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
                idu = int(self.ui.prompt_required("ID do usuário a atualizar: "))
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
                    campo_op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3"])
                    
                    if campo_op == "1":
                        novo_valor = self.ui.prompt_required("Novo nome: ")
                        self.usuario_ctrl.update(idu, {"nome": novo_valor})
                        print("Usuário atualizado.")
                    elif campo_op == "2":
                        novo_valor = self.ui.prompt_required("Novo email: ")
                        self.usuario_ctrl.update(idu, {"email": novo_valor})
                        print("Usuário atualizado.")
                    elif campo_op == "3":
                        novo_valor = self.ui.prompt_required("Nova senha: ")
                        self.usuario_ctrl.update(idu, {"senha": novo_valor})
                        print("Usuário atualizado.")
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
        op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4", "5"])
        if op == "1":
            nome = self.ui.prompt_required("Nome: ")
            desc = self.ui.prompt_optional_or_retry("Descrição: ")
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
                idc = int(self.ui.prompt_required("ID da categoria a remover: "))
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
                        confirmar = self.ui.prompt_choice("Tem certeza que deseja remover? (s/n): ", ["s", "n"]) == "s"
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
                idc = int(self.ui.prompt_required("ID da categoria a atualizar: "))
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
                    campo_op = self.ui.prompt_choice("Escolha: ", ["1", "2"])
                    
                    if campo_op == "1":
                        novo_valor = self.ui.prompt_required("Novo nome: ")
                        self.categoria_ctrl.update(idc, {"nome": novo_valor})
                        print("Categoria atualizada.")
                    elif campo_op == "2":
                        novo_valor = self.ui.prompt_optional_or_retry("Nova descrição: ")
                        self.categoria_ctrl.update(idc, {"descricao": novo_valor})
                        print("Categoria atualizada.")
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
        op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4", "5"])
        if op == "1":
            titulo = self.ui.prompt_required("Título: ")
            descricao = self.ui.prompt_optional_or_retry("Descrição: ")
            print("-- Usuários cadastrados --")
            usuarios = list(self.usuario_ctrl.list_all())
            if usuarios:
                for u in usuarios:
                    print(f"{u['id']} - {u['nome']}")
                id_usuario = int(self.ui.prompt_required("ID do usuário responsável: "))
            else:
                print("Nenhum usuário cadastrado.")
                return
            print("-- Categorias cadastradas --")
            categorias = list(self.categoria_ctrl.list_all())
            if categorias:
                for c in categorias:
                    print(f"{c['id']} - {c['nome']}")
                id_categoria = int(self.ui.prompt_required("ID da categoria: "))
            else:
                print("Nenhuma categoria cadastrada.")
                return
            t = self.tarefa_ctrl.create(titulo, descricao, id_usuario, id_categoria)
            print(f"Tarefa criada com id {t['id']}")
        elif op == "2":
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} (status: {t['status']}) - usuario:{t.get('id_usuario', 'N/A')} categoria:{t.get('categoria_id', 'N/A')}")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "3":
            print("\n-- Tarefas cadastradas no banco --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} (status: {t['status']}) - usuario:{t.get('id_usuario', 'N/A')} categoria:{t.get('categoria_id', 'N/A')}")
                print()
                idt = int(self.ui.prompt_required("ID da tarefa a remover: "))
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
                    confirmar = self.ui.prompt_choice("Tem certeza que deseja remover? (s/n): ", ["s", "n"]) == "s"
                    if confirmar:
                        cascade = self.ui.prompt_choice("Remover em cascata comentários/anexos/tempos? (s/n): ", ["s", "n"]) == "s"
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
                idt = int(self.ui.prompt_required("ID da tarefa a atualizar: "))
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
                    campo_op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4", "5"])
                    
                    if campo_op == "1":
                        novo_valor = self.ui.prompt_required("Novo título: ")
                        self.tarefa_ctrl.update(idt, {"titulo": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "2":
                        novo_valor = self.ui.prompt_optional_or_retry("Nova descrição: ")
                        self.tarefa_ctrl.update(idt, {"descricao": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "3":
                        novo_valor = self.ui.prompt_status()
                        self.tarefa_ctrl.update(idt, {"status": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "4":
                        print("-- Usuários disponíveis --")
                        for u in self.usuario_ctrl.list_all():
                            print(f"{u['id']} - {u['nome']}")
                        novo_valor = int(self.ui.prompt_required("Novo ID do usuário: "))
                        self.tarefa_ctrl.update(idt, {"id_usuario": novo_valor})
                        print("Tarefa atualizada.")
                    elif campo_op == "5":
                        print("-- Categorias disponíveis --")
                        for c in self.categoria_ctrl.list_all():
                            print(f"{c['id']} - {c['nome']}")
                        novo_valor = int(self.ui.prompt_required("Novo ID da categoria: "))
                        self.tarefa_ctrl.update(idt, {"categoria_id": novo_valor})
                        print("Tarefa atualizada.")
                else:
                    print("Tarefa não encontrada.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "5":
            return

    def menu_comentarios(self):
        self.ui.header("COMENTÁRIOS")
        self.ui.option("1", "Inserir comentário")
        self.ui.option("2", "Listar comentários de uma tarefa")
        self.ui.option("3", "Remover comentários de uma tarefa")
        self.ui.option("4", "Voltar")
        op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4"])
        if op == "1":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                tarefa = self.tarefa_ctrl.find(tarefa_id)
                if tarefa:
                    print("-- Usuários cadastrados --")
                    usuarios = list(self.usuario_ctrl.list_all())
                    if usuarios:
                        for u in usuarios:
                            print(f"{u['id']} - {u['nome']}")
                        usuario_id = int(self.ui.prompt_required("ID do usuário: "))
                        texto = self.ui.prompt_required("Texto do comentário: ")
                        data = self.ui.prompt_optional_or_retry("Data do comentário (opcional): ")
                        c = self.comentario_ctrl.create(tarefa_id, usuario_id, texto, data)
                        print(f"Comentário criado com id {c['id']}")
                    else:
                        print("Nenhum usuário cadastrado.")
                else:
                    print("Tarefa não encontrada.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "2":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                comentarios = self.comentario_ctrl.list_by_tarefa(tarefa_id)
                if comentarios:
                    print(f"\n-- Comentários da tarefa {tarefa_id} --")
                    for com in comentarios:
                        print(f"ID: {com['id']}")
                        print(f"  Usuário: {com['usuario_id']}")
                        print(f"  Texto: {com['texto']}")
                        print(f"  Data: {com.get('data_comentario', 'N/A')}")
                        print()
                else:
                    print("Nenhum comentário encontrado para essa tarefa.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "3":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                comentarios = self.comentario_ctrl.list_by_tarefa(tarefa_id)
                if comentarios:
                    print(f"\n-- Comentários da tarefa {tarefa_id} --")
                    for com in comentarios:
                        print(f"ID: {com['id']} - {com['texto'][:50]}")
                    confirmar = self.ui.prompt_choice("Tem certeza que deseja remover todos os comentários? (s/n): ", ["s", "n"]) == "s"
                    if confirmar:
                        deleted = self.comentario_ctrl.delete_by_tarefa(tarefa_id)
                        print(f"{deleted} comentário(s) removido(s).")
                    else:
                        print("Remoção cancelada.")
                else:
                    print("Nenhum comentário para remover.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "4":
            return

    def menu_anexos(self):
        self.ui.header("ANEXOS")
        self.ui.option("1", "Inserir anexo")
        self.ui.option("2", "Listar anexos de uma tarefa")
        self.ui.option("3", "Remover anexos de uma tarefa")
        self.ui.option("4", "Voltar")
        op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4"])
        if op == "1":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                tarefa = self.tarefa_ctrl.find(tarefa_id)
                if tarefa:
                    nome_arquivo = self.ui.prompt_required("Nome do arquivo: ")
                    tipo_arquivo = self.ui.prompt_optional_or_retry("Tipo do arquivo (ex: .pdf, .docx): ")
                    caminho = self.ui.prompt_required("Caminho do arquivo: ")
                    a = self.anexo_ctrl.create(tarefa_id, nome_arquivo, tipo_arquivo, caminho)
                    print(f"Anexo criado com id {a['id']}")
                else:
                    print("Tarefa não encontrada.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "2":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                anexos = self.anexo_ctrl.list_by_tarefa(tarefa_id)
                if anexos:
                    print(f"\n-- Anexos da tarefa {tarefa_id} --")
                    for anx in anexos:
                        print(f"ID: {anx['id']}")
                        print(f"  Nome: {anx['nome_arquivo']}")
                        print(f"  Tipo: {anx.get('tipo_arquivo', 'N/A')}")
                        print(f"  Caminho: {anx['caminho']}")
                        print()
                else:
                    print("Nenhum anexo encontrado para essa tarefa.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "3":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                anexos = self.anexo_ctrl.list_by_tarefa(tarefa_id)
                if anexos:
                    print(f"\n-- Anexos da tarefa {tarefa_id} --")
                    for anx in anexos:
                        print(f"ID: {anx['id']} - {anx['nome_arquivo']}")
                    confirmar = self.ui.prompt_choice("Tem certeza que deseja remover todos os anexos? (s/n): ", ["s", "n"]) == "s"
                    if confirmar:
                        deleted = self.anexo_ctrl.delete_by_tarefa(tarefa_id)
                        print(f"{deleted} anexo(s) removido(s).")
                    else:
                        print("Remoção cancelada.")
                else:
                    print("Nenhum anexo para remover.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "4":
            return

    def menu_tempos_gastos(self):
        self.ui.header("TEMPOS GASTOS")
        self.ui.option("1", "Inserir tempo gasto")
        self.ui.option("2", "Listar tempos gastos de uma tarefa")
        self.ui.option("3", "Remover tempos gastos de uma tarefa")
        self.ui.option("4", "Voltar")
        op = self.ui.prompt_choice("Escolha: ", ["1", "2", "3", "4"])
        if op == "1":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                tarefa = self.tarefa_ctrl.find(tarefa_id)
                if tarefa:
                    try:
                        horas = float(self.ui.prompt_required("Horas gastas: "))
                        data = self.ui.prompt_optional_or_retry("Data do registro (opcional): ")
                        tg = self.tempo_ctrl.create(tarefa_id, horas, data)
                        print(f"Tempo gasto criado com id {tg['id']}")
                    except ValueError:
                        print("❌ Valor inválido para horas. Digite um número.")
                else:
                    print("Tarefa não encontrada.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "2":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                tempos = self.tempo_ctrl.list_by_tarefa(tarefa_id)
                if tempos:
                    print(f"\n-- Tempos gastos na tarefa {tarefa_id} --")
                    total_horas = 0
                    for tg in tempos:
                        print(f"ID: {tg['id']}")
                        print(f"  Horas: {tg['horas']}")
                        print(f"  Data: {tg.get('data_registro', 'N/A')}")
                        print()
                        total_horas += tg['horas']
                    print(f"Total de horas: {total_horas}")
                else:
                    print("Nenhum tempo gasto registrado para essa tarefa.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "3":
            print("-- Tarefas cadastradas --")
            tarefas = list(self.tarefa_ctrl.list_all())
            if tarefas:
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']}")
                tarefa_id = int(self.ui.prompt_required("ID da tarefa: "))
                tempos = self.tempo_ctrl.list_by_tarefa(tarefa_id)
                if tempos:
                    print(f"\n-- Tempos gastos na tarefa {tarefa_id} --")
                    for tg in tempos:
                        print(f"ID: {tg['id']} - {tg['horas']} horas")
                    confirmar = self.ui.prompt_choice("Tem certeza que deseja remover todos os tempos? (s/n): ", ["s", "n"]) == "s"
                    if confirmar:
                        deleted = self.tempo_ctrl.delete_by_tarefa(tarefa_id)
                        print(f"{deleted} registro(s) removido(s).")
                    else:
                        print("Remoção cancelada.")
                else:
                    print("Nenhum tempo para remover.")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif op == "4":
            return
