import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_exponent(self):
		result = rpn.calculate('5 2 ^')
		self.assertEqual(25, result)
	def test_multiply(self):
		result = rpn.calculate('1 1 *')
		self.assertEqual(1, result)
		result = rpn.calculate('1 2 *')
		self.assertEqual(2, result)
		result = rpn.calculate('5 6 *')
		self.assertEqual(30, result)
		result = rpn.calculate('6 5 *')
		self.assertEqual(30, result)
	def test_divide(self):
		result = rpn.calculate('30 5 _')
		self.assertEqual(6, result)
		result = rpn.calculate('5 5 _')
		self.assertEqual(1, result)
		result = rpn.calculate('0 9 _')
		self.assertEqual(0, result)
