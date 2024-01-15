#!/usr/bin/python3
"""Define Base Test Cases"""
import unittest
from models.base import Base


class TestBase_id(unittest.TestCase):
    """Test Cases for identefier"""
    def test_NoArg(self):
        id1 = Base()
        id2 = Base()
        self.assertEqual(id1.id, id2.id - 1)

    def test_Arg(self):
        id1 = Base(12)
        self.assertEqual(id1.id, 12)

    def test_Mix(self):
        id1 = Base()
        id2 = Base()
        id3 = Base()
        id12 = Base(12)
        id4 = Base()
        self.assertEqual(id1.id, id4.id - 3)

    def test_id_public(self):
        id1 = Base()
        id1.id = 10
        self.assertEqual(id1.id, 10)

    def test_nb_objects(self):
        id1 = Base()
        with self.assertRaises(AttributeError):
            print(id1.__nb_objects)
