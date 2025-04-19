import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.get('/calc?a=5&b=3&op=add')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 8)

    def test_invalid_operation(self):
        response = self.app.get('/calc?a=5&b=3&op=mod')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()
