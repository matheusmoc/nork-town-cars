get_template_docs = {
    'tags': ['Carros'],
    'responses': {
        200: {
            'description': 'Renderiza o template de gerenciamento de carros',
            'examples': {
                'text/html': '<html>...</html>'
            }
        }
    }
}

get_cars_docs = {
    'tags': ['Carros'],
    'responses': {
        200: {
            'description': 'Lista todos os carros',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'modelo': {'type': 'string'},
                        'cor': {'type': 'string'},
                        'nome_dono': {'type': 'string'},
                        'contato_dono': {'type': 'string'}
                    }
                }
            }
        }
    }
}

create_car_docs = {
    'tags': ['Carros'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'modelo': {'type': 'string'},
                    'cor': {'type': 'string'},
                    'owner_id': {'type': 'integer'}
                },
                'required': ['modelo', 'cor', 'owner_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Carro criado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'mensagem': {'type': 'string'},
                    'car_id': {'type': 'integer'}
                }
            }
        }
    }
}

update_car_docs = {
    'tags': ['Carros'],
    'parameters': [
        {
            'name': 'car_id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'modelo': {'type': 'string'},
                    'cor': {'type': 'string'},
                    'owner_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Carro atualizado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'mensagem': {'type': 'string'},
                    'car_id': {'type': 'integer'}
                }
            }
        },
        404: {
            'description': 'Carro não encontrado'
        }
    }
}

delete_car_docs = {
    'tags': ['Carros'],
    'parameters': [
        {
            'name': 'car_id',
            'in': 'path',
            'required': True,
            'type': 'integer'
        }
    ],
    'responses': {
        200: {
            'description': 'Carro excluído com sucesso'
        },
        404: {
            'description': 'Carro não encontrado'
        }
    }
}
