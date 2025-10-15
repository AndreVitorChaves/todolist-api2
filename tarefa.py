from flask import jsonify

def buscar_tarefas():
    tarefas = [
        {
            'id': 1,
            'nome': 'Aprender digitacao',
            'descricao': 'Vamos aumentar o zoom para nao errar a digitacao',
            'status': 'Pendente'
        },
        
        {
            'id': 2,
            'nome': 'Aprender Python',
            'descricao': 'Aprender Python para programar apis',
            'status': 'Pendente'
        }
    ]
    return jsonify(tarefas)