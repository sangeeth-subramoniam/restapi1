from django.test import TestCase
from app.calc import add, subt


class CalcTests(TestCase):
    def test_add(self):
        """checks the add fucnction"""
        self.assertEqual(add(5, 10), 15)

    def test_subt(self):
        """tests the subt function """
        self.assertEqual(subt(20, 5), 15)
