import unittest
from main import *

class Test(unittest.TestCase):
  def test_factorise(self):
    self.assertEqual(factorise(0), {}, 'Failed with 0')
    self.assertEqual(factorise(24), {2:3, 3:1}, 'Failed with 24')
    self.assertEqual(factorise(100), {2:2, 5:2}, 'Failed with 100')

  def test_drs(self):
    self.assertEqual(drs(24), 6, 'Failed with 24')
    self.assertEqual(drs(12), 3, 'Failed with 12')
    self.assertEqual(drs(3), 3, 'Failed with 3')
    self.assertEqual(drs(10), 1, 'Failed with 10')
  
  def test_factor_combinations(self):
    self.assertEqual(len(factor_combinations(24)), 7, 'Failed with 24')
    self.assertEqual(len(factor_combinations(4)), 2, 'Failed with 4')
    self.assertEqual(len(factor_combinations(1)), 1, 'Failed with 1')
    self.assertEqual(len(factor_combinations(0)), 0, 'Failed with 0')

if __name__ == "__main__":
  unittest.main()