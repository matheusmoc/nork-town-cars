from flask import Blueprint, request, jsonify, render_template
from app.services.car_service import create_car, get_all_cars, update_car, delete_car
from flask_login import login_required, current_user

#API
car = Blueprint('car', __name__)

@car.route('/', methods=['GET'])
@login_required
def get_template():
    return render_template('cars.html', name=current_user.name)

@car.route('list', methods=['GET'])
@login_required
def api_get_cars():
    cars = get_all_cars()
    return jsonify([{"id": c.id, "model": c.model, "color": c.color, "owner_name": c.owner.name, "owner_contact": c.owner.contact} for c in cars]), 200

@car.route('create', methods=['POST'])
@login_required
def api_create_car():
    data = request.json
    car = create_car(data['model'], data['color'], data['owner_id'])
    return jsonify({"message": "Carro cadastrado com sucesso!", "car_id": car.id,}), 201

@car.route('update/<int:car_id>', methods=['PUT'])
@login_required
def api_update_car(car_id):
    data = request.json
    car = update_car(car_id, data['model'], data['color'], data.get('owner_id'))
    if car:
        return jsonify({"message": "Carro atualizado com sucesso!", "car_id": car.id}), 200
    return jsonify({"message": "Carro não encontrado."}), 404

@car.route('delete/<int:car_id>', methods=['DELETE'])
@login_required
def api_delete_car(car_id):
    success = delete_car(car_id)
    if success:
        return jsonify({"message": "Carro excluído com sucesso!"}), 200
    return jsonify({"message": "Carro não encontrado."}), 404
