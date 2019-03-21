import unittest
from Prime import *

class TestStringMethods(unittest.TestCase):

  def test_zero(self):
      self.assertEqual(inst.check('0'), False)

  def test_neg(self):
      self.assertEqual(inst.check('-5'), False)

  def test_one(self):
      self.assertEqual(inst.check('1'), False)

  def test_str(self):
      self.assertEqual(inst.check('Tanya'), False)

  def test_frac(self):
      self.assertEqual(inst.check('1.5'), False)

  def test_dig(self):
      self.assertEqual(inst.check('5'), True)

  def test_prime(self):
      self.assertEqual(inst.is_prime(2), True)

  def test_notPrime(self):
      self.assertEqual(inst.is_prime(6), False)

  def test_2(self):
      self.assertEqual(inst.get_primes(2), [2])

  def test_6(self):
      self.assertEqual(inst.get_primes(6), [2, 3, 5])

  
      
inst=Prime()
if __name__ == '__main__':
    unittest.main()