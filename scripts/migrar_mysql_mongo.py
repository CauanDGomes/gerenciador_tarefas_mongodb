import mysql.connector
from pymongo import MongoClient

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "mysql",
    "database": "maindb"
}

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "sistema_tarefas"

def migrate_table(mysql_cursor, table_name, mongo_db):
    try:
        mysql_cursor.execute(f"SELECT * FROM {table_name}")
    except Exception as e:
        print(f"Erro lendo {table_name}: {e}")
        return
    cols = [d[0] for d in mysql_cursor.description]
    rows = mysql_cursor.fetchall()
    docs = []
    for r in rows:
        doc = {}
        for c, v in zip(cols, r):
            doc[c] = v
        docs.append(doc)
    if docs:
        mongo_db[table_name].insert_many(docs)
    print(f"Migrated {table_name}: {len(docs)} docs")

def main():
    my = mysql.connector.connect(**MYSQL_CONFIG)
    cur = my.cursor()
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    tables = ['usuario','categoria','tarefa','comentario','anexo','tempo_gasto']
    for t in tables:
        migrate_table(cur, t, db)
    cur.close()
    my.close()
    print("Migration completed.")

if __name__ == "__main__":
    main()
