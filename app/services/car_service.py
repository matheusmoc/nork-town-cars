from app.models import db
from app.models.car import Car
from sqlalchemy import asc, desc

def create_car(model, color, owner_id):
    new_car = Car(model=model, color=color, owner_id=owner_id)
    db.session.add(new_car)
    db.session.commit()
    return new_car

def get_all_cars():
    return Car.query.order_by(desc(Car.id)).all()

def get_car_by_id(car_id):
    return Car.query.get(car_id)

def update_car(car_id, model=None, color=None):
    car = get_car_by_id(car_id)
    if car:
        if model:
            car.model = model
        if color:
            car.color = color
        db.session.commit()
    return car

def delete_car(car_id):
    car = get_car_by_id(car_id)
    if car:
        db.session.delete(car)
        db.session.commit()
        return True
    return False
