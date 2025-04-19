import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_addition(self):
        response = self.client.get('/calc?a=5&b=3&op=add')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['result'], 8)

    def test_invalid_operation(self):
        response = self.client.get('/calc?a=5&b=3&op=xyz')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
