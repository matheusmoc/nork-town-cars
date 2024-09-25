from flask import Blueprint, Flask, request, jsonify, render_template
from app.services.owner_service import create_owner, get_all_owners, update_owner, delete_owner

#API
owner = Blueprint('owner', __name__)

@owner.route('/', methods=['GET'])
def get_template():
    return render_template('owners.html')

@owner.route('list', methods=['GET'])
def api_get_owners():
    owners = get_all_owners()
    return jsonify([
        {
            "id": o.id,
            "name": o.name,
            "contact": o.contact,
            "cars": [
                {
                    "id": car.id,
                    "model": car.model,
                    "color": car.color
                }
                for car in o.cars
            ]
        }
        for o in owners
    ]), 200


@owner.route('create', methods=['POST'])
def api_create_owner():
    data = request.json
    owner = create_owner(data['name'], data.get('contact'))
    return jsonify({"message": "Proprietário cadastrado com sucesso!", "own er_id": owner.id}), 201

@owner.route('update/<int:owner_id>', methods=['PUT'])
def api_update_owner(owner_id):
    data = request.json
    owner = update_owner(owner_id, data['name'], data.get('contact'))
    if owner:
        return jsonify({"message": "Proprietário atualizado com sucesso!", "owner_id": owner.id}), 200
    return jsonify({"message": "Proprietário não encontrado."}), 404

@owner.route('delete/<int:owner_id>', methods=['DELETE'])
def api_delete_owner(owner_id):
    success = delete_owner(owner_id)
    if success:
        return jsonify({"message": "Proprietário excluído com sucesso!"}), 200
    return jsonify({"message": "Proprietário não encontrado."}), 404
