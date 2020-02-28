from PythonSimpleCalc.Calculator import Calculator
import pytest
import unittest


class test_PythonSimpleCalc(unittest.TestCase):
    def test_calc(self):
        c = Calculator()
        assert c

    def test_calc_add(self):
        c = Calculator()
        assert c.add(1, 2) == 3

    def test_calc_subtract(self):
        c = Calculator()
        assert c.subtract(0, 7) == -7

    def test_calc_multiply(self):
        c = Calculator()
        assert c.multiply(5, 2) == 10

    def test_calc_divide(self):
        c = Calculator()
        assert c.divide(18, 6) == 3
