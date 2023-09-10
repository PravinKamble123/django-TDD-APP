"""
Sample test
"""

from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""
    def test_add_numbers(self):
        """Adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Subtracting numbers."""
        res = calc.sub(20, 10)
        self.assertEqual(res, 10)
