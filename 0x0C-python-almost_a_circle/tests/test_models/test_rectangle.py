#!/usr/bin/python3
"""Module for test Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test for rectangle.
    """

    def setUp(self):
        """
        """
        Base._Base__nb_objects = 0

    def test_Check_r(self):
        """Check for r if it's instance of Rectangle.
        """        
        r = Rectangle(10, 10, 0, 0, 10)
        self.assertIsInstance(r, Rectangle)

    def test_Check_r2(self):
        """Check for r if it's instance of Base.
        """        
        r = Rectangle(10, 10, 0, 0, 10)
        self.assertIsInstance(r, Base)

    def test_Check_R(self):
        """Check for Rectangle if it's sub of Base.
        """        
        self.assertTrue(issubclass(Rectangle, Base))

    def test_Check_id(self):
        """Check for id without parameter.
        """        
        r = Rectangle(10, 10, x=0, y=0)
        self.assertEqual(r.id, 1)

    def test_Check_id2(self):
        """Check for id with parameter.
        """        
        r = Rectangle(10, 10, 0, 0, 10)
        self.assertEqual(r.id, 10)


    def test_Check_id3(self):
        """Check for id with negative parameter.
        """        
        r = Rectangle(10, 10, 0, 0, -10)
        self.assertEqual(r.id, -10)

    def test_Check_id4(self):
        """Check for id with more than one instance, with and without parameter.
        """        
        r1 = Rectangle(10, 10, 0, 0)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(20, 20, 0, 0)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(20, 20, 0, 0, 20)
        self.assertEqual(r3.id, 20)
        r4 = Rectangle(20, 20, 0, 0)
        self.assertEqual(r4.id, 3)

    def test_Check_y(self):
        """Check for y without parameter.
        """        
        r = Rectangle(10, 10, 10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.x, 10)

    def test_Check_x(self):
        """Check for x without parameter.
        """        
        r = Rectangle(10, 10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_check_xy2(self):
        """Check for x and y with positive number.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.x, 10)

    def test_checky3(self):
        """Check for x and y with negative number.
        """
        r = Rectangle(10, 10, -10, -10, 10)
        self.assertEqual(r.y, -10)
        self.assertEqual(r.x, -10)

    def test_checky4(self):
        """Check for x and y with float.
        """
        r = Rectangle(10, 10, 10.6, 10.5, 10)
        self.assertEqual(r.y, 10.5)
        self.assertEqual(r.x, 10.6)

    def test_checkxy5(self):
        """Check for x and y with list.
        """
        r = Rectangle(10, 10, [1, 2], [1, 2], 10)
        self.assertEqual(r.y, [1, 2])
        self.assertEqual(r.x, [1, 2])

    def test_checkxy6(self):
        """Check for x and y with tuple.
        """
        r = Rectangle(10, 10, (1, 2), (1, 2), 10)
        self.assertEqual(r.y, (1, 2))
        self.assertEqual(r.x, (1, 2))

    def test_checkxy7(self):
        """Check for x and y with set.
        """
        r = Rectangle(10, 10, {1, 2}, {1, 2}, 10)
        self.assertEqual(r.y, {1, 2})
        self.assertEqual(r.x, {1, 2})

    def test_checkxy8(self):
        """Check for x and y with dict.
        """
        r = Rectangle(10, 10, {1: 123, 2: 456}, {1: 123, 2: 456}, 10)
        self.assertEqual(r.y, {1: 123, 2: 456})
        self.assertEqual(r.x, {1: 123, 2: 456})

    def test_check_setter(self):
        """Check for setter for all attributes.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 10)
        r.width = 1
        self.assertEqual(r.width, 1)
        r.height = 2
        self.assertEqual(r.height, 2)
        r.x = 3
        self.assertEqual(r.x, 3)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_check_width_height6(self):
        """Check for width and height with normal number.
        """
        r = Rectangle(10, 20, 10, 10, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)


if __name__ == '__main__':
    unittest.main()