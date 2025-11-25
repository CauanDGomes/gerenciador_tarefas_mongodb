use sistema_tarefas;
db.usuarios.drop();
db.categorias.drop();
db.tarefas.drop();
db.comentarios.drop();
db.anexos.drop();
db.tempos_gastos.drop();
db.counters.drop();

db.createCollection("counters");
db.counters.insertMany([
  { _id: "usuarios", seq: 0 },
  { _id: "categorias", seq: 3 },
  { _id: "tarefas", seq: 0 },
  { _id: "comentarios", seq: 0 },
  { _id: "anexos", seq: 0 },
  { _id: "tempos_gastos", seq: 0 }
]);
db.createCollection("usuarios");
db.createCollection("categorias");
db.createCollection("tarefas");
db.createCollection("comentarios");
db.createCollection("anexos");
db.createCollection("tempos_gastos");
db.categorias.insertMany([
  { id: 1, nome: "trabalho", descricao: "Profissional" },
  { id: 2, nome: "estudo", descricao: "materia" },
  { id: 3, nome: "pessoal", descricao: "privado" }
]);
db.usuarios.createIndex({ email: 1 }, { unique: true });
db.tarefas.createIndex({ id_usuario: 1 });
db.tarefas.createIndex({ categoria_id: 1 });
db.comentarios.createIndex({ tarefa_id: 1 });
db.anexos.createIndex({ tarefa_id: 1 });
db.tempos_gastos.createIndex({ tarefa_id: 1 });
