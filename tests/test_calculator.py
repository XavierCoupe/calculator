from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
	def setUp(self):
  		self.calc = Calculator()

	def test_sum(self):
  		self.assertEqual(self.calc.mysum(1, 2), 3)
      
	def test_mean(self):
			self.assertEqual(self.calc.mymean(2,6),4)

    
    
if __name__ == '__main__':
	unittest.main()
