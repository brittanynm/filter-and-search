from unittest import TestCase
from model import Customer, Company, connect_to_db, db
from server import app
import server

class FlaskTests(TestCase):
    def setUp(self):
        """To do before every test."""

        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
        connect_to_db(app)
        db.create_all()

    def test_homepage(self):
        result = self.client.get("/customers")
        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        # db.drop_all()

    def test_find_customer(self):

        brittany = Customer.query.filter(Customer.last_name == "Morton").first()
        self.assertEqual(brittany.last_name, "Morton")

    def test_find_company(self):

        tinfoil = Company.query.filter(Company.name == "Tinfoil").first()
        self.assertEqual(tinfoil.name, "Tinfoil")

if __name__ == "__main__":
    import unittest

    unittest.main()
