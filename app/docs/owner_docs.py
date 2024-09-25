# owner_docs.py

get_template_docs = {
    'tags': ['Proprietários'],
    'responses': {
        200: {
            'description': 'Página HTML de proprietários renderizada com sucesso.'
        }
    }
}

get_owners_docs = {
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
}

create_owner_docs = {
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
}

update_owner_docs = {
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
}

delete_owner_docs = {
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
}
