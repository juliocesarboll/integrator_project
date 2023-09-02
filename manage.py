from app import app, db
from app.models import Equipamento
from flask import jsonify, request, render_template


@app.route('/')
@app.route('/index')
def hello():
   return render_template('home.html')

# @app.route('/equipamentos', methods=['GET'])
# def get_equipamentos():
#     equipamentos = Equipamento.query.all()
#     output = []

#     for equipamento in equipamentos:
#         equipamento_data = {
#             'id': equipamento.id,
#             'nome': equipamento.nome,
#             'descricao': equipamento.descricao,
#             'preco': equipamento.preco
#         }
#         output.append(equipamento_data)

#     return jsonify({'equipamentos': output})


# @app.route('/equipamentos/<int:id>', methods=['GET'])
# def get_equipamento(id):
#     equipamento = Equipamento.query.get(id)

#     if equipamento:
#         equipamento_data = {
#             'id': equipamento.id,
#             'nome': equipamento.nome,
#             'descricao': equipamento.descricao,
#             'preco': equipamento.preco
#         }
#         return jsonify(equipamento_data)

#     return jsonify({'message': 'Equipamento não encontrado'}), 404


# @app.route('/equipamentos', methods=['POST'])
# def create_equipamento():
#     data = request.get_json()

#     equipamento = Equipamento(data['nome'], data['descricao'], data['preco'])
#     db.session.add(equipamento)
#     db.session.commit()

#     return jsonify({'message': 'Equipamento criado com sucesso'}), 201


# @app.route('/equipamentos/<int:id>', methods=['PUT'])
# def update_equipamento(id):
#     equipamento = Equipamento.query.get(id)

#     if equipamento:
#         data = request.get_json()
#         equipamento.nome = data['nome']
#         equipamento.descricao = data['descricao']
#         equipamento.preco = data['preco']

#         db.session.commit()

#         return jsonify({'message': 'Equipamento atualizado com sucesso'})

#     return jsonify({'message': 'Equipamento não encontrado'}), 404


# @app.route('/equipamentos/<int:id>', methods=['DELETE'])
# def delete_equipamento(id):
#     equipamento = Equipamento.query.get(id)

#     if equipamento:
#         db.session.delete(equipamento)
#         db.session.commit()

#         return jsonify({'message': 'Equipamento excluído com sucesso'})

#     return jsonify({'message': 'Equipamento não encontrado'}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')