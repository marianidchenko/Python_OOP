from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room
from project.appliances.fridge import Fridge


class RoomTests(TestCase):
    def setUp(self):
        self.room = Room("name", 100, 2)
        self.child1 = Child(1, 1, 2)
        self.child2 = Child(1, 1, 2)

    def test_init_returns_correct_values(self):
        self.assertEqual("name", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_negative_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -3
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_expenses_positive_value_returns_correct_results(self):
        self.room.expenses = 3
        self.assertEqual(3, self.room.expenses)

    def test_calculate_expenses_returns_correct_values(self):
        self.room.calculate_expenses([self.child1, self.child2])
        self.assertEqual(240, self.room.expenses)


if __name__ == '__main__':
    main()