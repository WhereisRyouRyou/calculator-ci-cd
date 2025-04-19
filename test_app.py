import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_addition(self):
        response = self.app.get('/calc?a=5&b=3&op=add')
        data = response.data.decode('utf-8')
        print("Response data (add):", response.data)
        self.assertIn("Result: 8.0", data)

    def test_invalid_operation(self):
        response = self.app.get('/calc?a=5&b=3&op=mod')
        data = response.data.decode('utf-8')
        print("Response data (mod):", response.data)
        self.assertIn("Error: Invalid operation", data)
