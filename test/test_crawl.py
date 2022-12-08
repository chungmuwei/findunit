import unittest
import sys

sys.path.insert(0, "..")

from crawl import *

class test_get_unit_outline_url(unittest.TestCase):
    """
    Unit tests for get_unit_outline_url function in crawl.py
    """
    
    def test_no_matched_unit_outline(self):
        """
        Test whether the function returns empty list if there is no unit outline for 
        the given year and mode of attendance
        """
        expected = []
        actual = get_unit_outline_url("comp2922", 2022, False)
        self.assertEqual(actual, expected, msg=f"Expected {expected}, got {actual}")

    def test_one_matched_unit_outline(self):
        """
        Test whether the function returns correct list if there is one matched unit outline for 
        the given year and mode of attendance
        """
        expected = ["https://www.sydney.edu.au/units/COMP2022/2022-S2C-ND-CC"]
        actual = get_unit_outline_url("comp2022", 2022, False)
        self.assertEqual(actual, expected, msg=f"Expected {expected}, got {actual}")
    
    def test_one_matched_unit_outline(self):
        """
        Test whether the function returns correct list if there are multiple matched unit outlines for 
        the given year and mode of attendance
        """
        expected = ["https://www.sydney.edu.au/units/MATH1002/2022-S1CIJA-BM-CC", "https://www.sydney.edu.au/units/MATH1002/2022-S1C-ND-CC"]
        actual = get_unit_outline_url("math1002", 2022, False)
        print(actual)
        self.assertEqual(actual, expected, msg=f"Expected {expected}, got {actual}")
