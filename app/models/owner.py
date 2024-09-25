from . import db 

class Owner(db.Model):
    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(20))
    cars = db.relationship('Car', backref='owner', lazy=True)

    def __repr__(self):
        return f'<Proprietário: {self.name}>'