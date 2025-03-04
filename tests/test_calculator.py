from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
	def setUp(self):
		self.calc = Calculator()

	def test_sum(self):
		self.assertEqual(self.calc.mysum(1, 2), 3)


	def test_min(self):
		self.assertEqual(self.calc.mymin(3, 5), 3)

	def test_max(self):
		self.assertEqual(self.calc.mymax(3, 5), 5)
    
    
if __name__ == '__main__':
    unittest.main()
