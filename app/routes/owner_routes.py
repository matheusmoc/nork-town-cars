from flask import Blueprint, request, jsonify, render_template
from app.services.owner_service import create_owner, get_all_owners, update_owner, delete_owner
from flask_login import login_required, current_user
from flasgger import swag_from
from app.docs.owner_docs import get_template_docs, get_owners_docs, create_owner_docs, update_owner_docs, delete_owner_docs

owner = Blueprint('owner', __name__)

@owner.route('/', methods=['GET'])
@login_required
@swag_from(get_template_docs)
def get_template():
    return render_template('owners.html', name=current_user.name)

@owner.route('list', methods=['GET'])
@login_required
@swag_from(get_owners_docs)
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
@login_required
@swag_from(create_owner_docs)
def api_create_owner():
    data = request.json
    owner = create_owner(data['name'], data.get('contact'))
    return jsonify({"message": "Proprietário cadastrado com sucesso!", "owner_id": owner.id}), 201

@owner.route('update/<int:owner_id>', methods=['PUT'])
@login_required
@swag_from(update_owner_docs)
def api_update_owner(owner_id):
    data = request.json
    owner = update_owner(owner_id, data['name'], data.get('contact'))
    if owner:
        return jsonify({"message": "Proprietário atualizado com sucesso!", "owner_id": owner.id}), 200
    return jsonify({"message": "Proprietário não encontrado."}), 404

@owner.route('delete/<int:owner_id>', methods=['DELETE'])
@login_required
@swag_from(delete_owner_docs)
def api_delete_owner(owner_id):
    success = delete_owner(owner_id)
    if success:
        return jsonify({"message": "Proprietário excluído com sucesso!"}), 200
    return jsonify({"message": "Proprietário não encontrado."}), 404
