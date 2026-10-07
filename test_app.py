import unittest
import app

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5,3),15)

    def test_dividir(self):
        self.assertEqual(dividir(4,2),2)

if __name__ == '__main__':
    unittest.main()
