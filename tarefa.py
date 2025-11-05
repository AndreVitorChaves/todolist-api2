from flask import jsonify
from conexao import get_conexao
from psycopg2.extras import RealDictCursor

def buscar_tarefas():
    #conecta no banco de dados
    con = get_conexao()
    cursor = con.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos;"
    )

    #busca os dados e armazena na variável
    todos = cursor.fetchall()

    #fecha as conexões
    cursor.close()
    con.close()

    return jsonify(todos)

def buscar_tarefa(id):
    #conecta no banco de dados
    con = get_conexao()
    cursor = con.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos WHERE id = %s", (id,)
    )

    #busca os dados e armazena na variável
    todo = cursor.fetchone()

    #fecha as conexões
    cursor.close()
    con.close()

    return jsonify(todo)