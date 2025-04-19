import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        # Send GET request with valid parameters
        response = self.app.get('/calc?a=5&b=3&op=add')
        print("Response data (add):", response.data)  # for debugging
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json())
        self.assertEqual(response.get_json()['result'], 8)

    def test_invalid_operation(self):
        # Send GET request with invalid operation
        response = self.app.get('/calc?a=5&b=3&op=mod')
        print("Response data (mod):", response.data)  # for debugging
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()
