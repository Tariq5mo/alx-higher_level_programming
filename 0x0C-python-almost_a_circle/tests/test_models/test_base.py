#!/usr/bin/python3
"""Test module for Base class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test for base class.
    """
    def setUp(self):
        """Set up for coming tsets.
        """
        Base._Base__nb_objects = 0

    def test_first_value_of_nb_objects(self):
        """Check if it's zero
        """
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_b1_nb_objects(self):
        """For __nb_objects. with one instance, without parameter.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(1, Base._Base__nb_objects)
        self.assertEqual(b1.id, Base._Base__nb_objects)

    def test_check_nb_objects(self):
        """Check for nb_objects
        _Base__nb_objects = 2
        """
        b2 = Base()
        self.assertIs(b2._Base__nb_objects, Base._Base__nb_objects)

    def test_b_isnot_base(self):
        """Check if b is not or equal to Base
        """
        b = Base()
        self.assertIsNot(b, Base)
        self.assertNotEqual(b, Base)

    def test_check_from(self):
        """Check if b is class of Base
        """
        b = Base()
        self.assertIsInstance(b, Base)

    def test_check(self):
        """Ckeck for several cases
        """
        b1 = Base()
        b2 = Base(10)
        b3 = Base(-10)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, -10)
        self.assertEqual(b4.id, 2)

    def test_check_b(self):
        """Check if b != __nb_objects
        """
        b = Base(10)
        self.assertNotEqual(b.id, Base._Base__nb_objects)

    def test_check_instnces(self):
        """Check if b1 is not or not Equal to b2
        """
        b1 = Base(10)
        b2 = Base(20)
        self.assertNotEqual(b1, b2)
        self.assertIsNot(b1, b2)

if __name__ == '__main__':
    unittest.main()
