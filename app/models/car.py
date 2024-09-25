from . import db 
from sqlalchemy import event
from sqlalchemy.orm import validates
from app.models.owner import Owner

class Car(db.Model):
    __tablename__ = 'car'

    MODEL_CHOICES = ['Hatch', 'Sedan', 'Convertible']
    COLOR_CHOICES = ['Yellow', 'Blue', 'Gray']

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __repr__(self):
        return f'<Carro {self.model} - {self.color}>'
    
    @validates('model')
    def validate_model(self, key, model):
        if model not in self.MODEL_CHOICES:
            raise ValueError(f"O modelo '{model}' não é permitido. Escolha entre {self.MODEL_CHOICES}.")
        return model

    @validates('color')
    def validate_color(self, key, color):
        if color not in self.COLOR_CHOICES:
            raise ValueError(f"A cor '{color}' não é permitida. Escolha entre {self.COLOR_CHOICES}.")
        return color

    @validates('owner_id')
    def validate_owner(self, key, owner_id):
        owner = Owner.query.get(owner_id)
        if owner is None:
            raise ValueError("O carro deve ter um proprietário válido.")
        
        if len(owner.cars) >= 3:
            raise ValueError("O proprietário já possui 3 carros.")

        if any(car.color == self.color for car in owner.cars):
            raise ValueError("O proprietário já possui um carro com a mesma cor.")

        if any(car.model == self.model for car in owner.cars):
            raise ValueError("O proprietário já possui um carro com o mesmo modelo.")
        
        return owner_id
