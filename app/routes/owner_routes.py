from flask import Blueprint, request, jsonify, render_template
from app.services.owner_service import create_owner, get_all_owners, update_owner, delete_owner
from flask_login import login_required, current_user
from flasgger import swag_from

#API
owner = Blueprint('owner', __name__)

@owner.route('/', methods=['GET'])
@login_required
@swag_from({
    'tags': ['Proprietários'],
    'responses': {
        200: {
            'description': 'Página HTML de proprietários renderizada com sucesso.'
        }
    }
})
def get_template():
    return render_template('owners.html', name=current_user.name)

@owner.route('list', methods=['GET'])
@login_required
@swag_from({
    'tags': ['Proprietários'],
    'responses': {
        200: {
            'description': 'Lista de proprietários retornada com sucesso.',
            'schema': {
                'type': 'array',
                'items': {
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'description': 'ID do proprietário.'
                        },
                        'name': {
                            'type': 'string',
                            'description': 'Nome do proprietário.'
                        },
                        'contact': {
                            'type': 'string',
                            'description': 'Contato do proprietário.'
                        },
                        'cars': {
                            'type': 'array',
                            'items': {
                                'properties': {
                                    'id': {
                                        'type': 'integer',
                                        'description': 'ID do carro.'
                                    },
                                    'model': {
                                        'type': 'string',
                                        'description': 'Modelo do carro.'
                                    },
                                    'color': {
                                        'type': 'string',
                                        'description': 'Cor do carro.'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
})
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
@swag_from({
    'tags': ['Proprietários'],
    'parameters': [{
        'name': 'body',
        'description': 'Dados do proprietário a serem criados.',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Nome do proprietário.'
                },
                'contact': {
                    'type': 'string',
                    'description': 'Contato do proprietário.'
                }
            }
        }
    }],
    'responses': {
        201: {
            'description': 'Proprietário criado com sucesso.',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string'
                    },
                    'owner_id': {
                        'type': 'integer'
                    }
                }
            }
        },
        400: {
            'description': 'Dados inválidos.'
        }
    }
})
def api_create_owner():
    data = request.json
    owner = create_owner(data['name'], data.get('contact'))
    return jsonify({"message": "Proprietário cadastrado com sucesso!", "own er_id": owner.id}), 201

@owner.route('update/<int:owner_id>', methods=['PUT'])
@login_required
@swag_from({
    'tags': ['Proprietários'],
    'parameters': [
        {
            'name': 'owner_id',
            'description': 'ID do proprietário a ser atualizado.',
            'in': 'path',
            'required': True,
            'type': 'integer'
        },
        {
            'name': 'body',
            'description': 'Dados do proprietário a serem atualizados.',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Nome do proprietário.'
                    },
                    'contact': {
                        'type': 'string',
                        'description': 'Contato do proprietário.'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Proprietário atualizado com sucesso.',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string'
                    },
                    'owner_id': {
                        'type': 'integer'
                    }
                }
            }
        },
        404: {
            'description': 'Proprietário não encontrado.'
        }
    }
})
def api_update_owner(owner_id):
    data = request.json
    owner = update_owner(owner_id, data['name'], data.get('contact'))
    if owner:
        return jsonify({"message": "Proprietário atualizado com sucesso!", "owner_id": owner.id}), 200
    return jsonify({"message": "Proprietário não encontrado."}), 404

@owner.route('delete/<int:owner_id>', methods=['DELETE'])
@login_required
@swag_from({
    'tags': ['Proprietários'],
    'parameters': [{
        'name': 'owner_id',
        'description': 'ID do proprietário a ser excluído.',
        'in': 'path',
        'required': True,
        'type': 'integer'
    }],
    'responses': {
        200: {
            'description': 'Proprietário excluído com sucesso.',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string'
                    }
                }
            }
        },
        404: {
            'description': 'Proprietário não encontrado.'
        }
    }
})
def api_delete_owner(owner_id):
    success = delete_owner(owner_id)
    if success:
        return jsonify({"message": "Proprietário excluído com sucesso!"}), 200
    return jsonify({"message": "Proprietário não encontrado."}), 404
