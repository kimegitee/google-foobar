import unittest
import hey, staircase, staircase2, fuel, find

class HeyTest(unittest.TestCase):

	def test_int2base(self):
		self.assertEqual(hey.int2base(484, 3), '122221')

	def test_getnext(self):
		self.assertEqual(hey.getnext('210111', 3), '122221')
		self.assertEqual(hey.getnext('122221', 3), '102212')

	def test_answer(self):
		self.assertEqual(hey.answer('1211', 10), 1)
		self.assertEqual(hey.answer('210022', 3), 3)

class StairTest(unittest.TestCase):

	def test_answer(self):
		self.assertEqual(staircase.answer(3), 1)
		self.assertEqual(staircase.answer(4), 1)
		self.assertEqual(staircase.answer(5), 2)
		self.assertEqual(staircase.answer(200), 487067745)

class StairTest2(unittest.TestCase):
	
	def test_answer(self):
		self.assertEqual(staircase2.answer(3), 1)
		self.assertEqual(staircase2.answer(4), 1)
		self.assertEqual(staircase2.answer(5), 2)
		self.assertEqual(staircase2.answer(200), 487067745)

class FuelTest(unittest.TestCase):
	
	def test_answer(self):
		self.assertEqual(fuel.answer('1'), 0)
		self.assertEqual(fuel.answer('4'), 2)
		self.assertEqual(fuel.answer('15'), 5)
		self.assertEqual(fuel.answer('50'), 7)

class FindTest(unittest.TestCase):

	def test_answer(self):
		self.assertEqual(find.answer([1, 1, 1]), 1)
		self.assertEqual(find.answer([1, 2, 3, 4, 5, 6]), 3)
		self.assertEqual(find.answer([int(i) for i in '1'*1900]), 1141362300)
