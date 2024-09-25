import unittest
from app.main import create_app, db
from app.models.owner import Owner
from app.models.car import Car  

class OwnerModelTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """Set up the application and the database for testing."""
        self.app = create_app('app.config.TestingConfig') 
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Tear down the database after tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_create_owner(self):
        """Test creating an owner."""
        owner = Owner(name='John Doe', contact='123-456-7890')
        db.session.add(owner)
        db.session.commit()

        self.assertIsNotNone(owner.id)  
        self.assertEqual(owner.name, 'John Doe')
        self.assertEqual(owner.contact, '123-456-7890')

    def test_owner_repr(self):
        """Test the __repr__ method of the Owner model."""
        owner = Owner(name='Jane Doe')
        self.assertEqual(repr(owner), '<Proprietário: Jane Doe>')

    def test_owner_cars_relationship(self):
        """Test the relationship between Owner and Car."""
        owner = Owner(name='John Doe')
        car1 = Car(model='Hatch', color='Yellow', owner=owner)
        car2 = Car(model='Sedan', color='Blue', owner=owner)

        db.session.add(owner)
        db.session.add(car1)
        db.session.add(car2)
        db.session.commit()

        self.assertEqual(len(owner.cars), 2)
        self.assertIn(car1, owner.cars)
        self.assertIn(car2, owner.cars)

if __name__ == '__main__':
    unittest.main()
