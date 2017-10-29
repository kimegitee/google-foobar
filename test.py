import unittest
import hey

class HeyTest(unittest.TestCase):

	def test_int2base(self):
		self.assertEqual(hey.int2base(484, 3), '122221')

	def test_getnext(self):
		self.assertEqual(hey.getnext('210111', 3), '122221')
		self.assertEqual(hey.getnext('122221', 3), '102212')	

	def test_answer(self):
		self.assertEqual(hey.answer('1211', 10), 1)
		self.assertEqual(hey.answer('210022', 3), 3)
