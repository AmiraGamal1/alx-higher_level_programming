#!/usr/bin/python3
"""Test cases rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """unittests"""
    def test_NoArg(self):
        with self.assertRaises(TypeError):
            Rectangle()
    
    def test_Base(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_valueId(self):
        self.assertEqual(Rectangle(5, 10, 10, 1, 1).id, 5)
    
    def test_valueWidth(self):
        
         