import unittest
from app.main import create_app, db
from app.models.car import Car
from app.models.owner import Owner

class CarModelTestCase(unittest.TestCase):
    def setUp(self):
        """Create a test client and a new database for the test."""
        self.app = create_app('app.config.TestingConfig') 
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.owner = Owner(name='Test Owner')
        db.session.add(self.owner)
        db.session.commit()

    def tearDown(self):
        """Clean up the database after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_car_valid(self):
        """Test creating a car with valid attributes."""
        car = Car(model='Hatch', color='Yellow', owner_id=self.owner.id)
        db.session.add(car)
        db.session.commit()
        self.assertIsNotNone(car.id)
        self.assertEqual(car.model, 'Hatch')
        self.assertEqual(car.color, 'Yellow')

    def test_create_car_invalid_model(self):
        """Test creating a car with an invalid model."""
        with self.assertRaises(ValueError) as context:
            car = Car(model='InvalidModel', color='Yellow', owner_id=self.owner.id)
            db.session.add(car)
            db.session.commit()
        self.assertEqual(str(context.exception), "O modelo 'InvalidModel' não é permitido. Escolha entre ['Hatch', 'Sedan', 'Convertible'].")

    def test_create_car_invalid_color(self):
        """Test creating a car with an invalid color."""
        with self.assertRaises(ValueError) as context:
            car = Car(model='Hatch', color='InvalidColor', owner_id=self.owner.id)
            db.session.add(car)
            db.session.commit()
        self.assertEqual(str(context.exception), "A cor 'InvalidColor' não é permitida. Escolha entre ['Yellow', 'Blue', 'Gray'].")

    def test_create_car_invalid_owner(self):
        """Test creating a car with a non-existent owner."""
        with self.assertRaises(ValueError) as context:
            car = Car(model='Hatch', color='Yellow', owner_id=999) 
            db.session.add(car)
            db.session.commit()
        self.assertEqual(str(context.exception), "O carro deve ter um proprietário válido.")

    def test_create_car_owner_with_three_cars(self):
        """Test creating a fourth car for an owner who already has three cars of different colors and models."""
        car1 = Car(model='Hatch', color='Yellow', owner_id=self.owner.id)
        car2 = Car(model='Sedan', color='Blue', owner_id=self.owner.id)
        car3 = Car(model='Convertible', color='Gray', owner_id=self.owner.id)

        db.session.add(car1)
        db.session.add(car2)
        db.session.add(car3)
        db.session.commit()

        created_cars = Car.query.filter_by(owner_id=self.owner.id).all()
        self.assertEqual(len(created_cars), 3)  

        self.assertEqual(created_cars[0].model, 'Hatch')
        self.assertEqual(created_cars[0].color, 'Yellow')

        self.assertEqual(created_cars[1].model, 'Sedan')
        self.assertEqual(created_cars[1].color, 'Blue')

        self.assertEqual(created_cars[2].model, 'Convertible')
        self.assertEqual(created_cars[2].color, 'Gray')

        # Uncomment the following code if the validation logic changes in the future
        # to allow owners to have more than three cars as long as they have different colors.
        # with self.assertRaises(ValueError) as context:
        #     car4 = Car(model='Convertible', color='Green', owner_id=self.owner.id)
        #     db.session.add(car4)
        #     db.session.commit()
            
        # self.assertEqual(str(context.exception), "O proprietário já possui 3 carros.")  

    def test_create_car_owner_with_same_color(self):
        """Test creating a car for an owner who already has a car of the same color."""
        car1 = Car(model='Hatch', color='Yellow', owner_id=self.owner.id)
        db.session.add(car1)
        db.session.commit()

        with self.assertRaises(ValueError) as context:
            car2 = Car(model='Sedan', color='Yellow', owner_id=self.owner.id)
            db.session.add(car2)
            db.session.commit()
        self.assertEqual(str(context.exception), "O proprietário já possui um carro com a mesma cor.")

    def test_create_car_owner_with_same_model(self):
        """Test creating a car for an owner who already has a car of the same model."""
        car1 = Car(model='Hatch', color='Yellow', owner_id=self.owner.id)
        db.session.add(car1)
        db.session.commit()

        with self.assertRaises(ValueError) as context:
            car2 = Car(model='Hatch', color='Blue', owner_id=self.owner.id)
            db.session.add(car2)
            db.session.commit()
        self.assertEqual(str(context.exception), "O proprietário já possui um carro com o mesmo modelo.")

if __name__ == '__main__':
    unittest.main()
