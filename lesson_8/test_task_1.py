import unittest

from lesson_8.task_1 import *

NAME = 'Bill'
AGE = 44

alex_1 = Alex('Alex1', 22)
alex_2 = Alex('Alex2', 33)
bill_1 = Bill(NAME, AGE)
bill_2 = Bill('Bill2', 55)


class TestSingletonEngineer(unittest.TestCase):
    """Test Singleton Pattern works as expected."""

    def test_id(self):
        self.assertEqual(id(alex_1), id(alex_2))

    def test_name(self):
        self.assertEqual(alex_1.name, alex_2.name)

    def test_age(self):
        self.assertEqual(alex_1.age, alex_2.age)

    def test_id_approach_2(self):
        self.assertEqual(id(bill_1), id(bill_2))

    def test_name_approach_2(self):
        self.assertEqual(bill_1.name, NAME)
        self.assertEqual(bill_2.name, NAME)

    def test_age_approach_2(self):
        self.assertEqual(bill_1.age, AGE)
        self.assertEqual(bill_2.age, AGE)
