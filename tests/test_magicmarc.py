# test_magicmarc.py

import unittest
from magicmarc import math

class TestMagicMarc(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_add(self):
		self.assertEqual(math.add(2,2), 4)


if __name__ == '__main__':
	unittest.main()
