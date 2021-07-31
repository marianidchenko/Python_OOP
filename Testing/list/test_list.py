from Testing.list.extended_list import IntegerList

import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.int_list = IntegerList(3, 6, 8)

    def test_init_creates_all_attributes(self):
        self.assertEqual([3, 6, 8], self.int_list._IntegerList__data)

    def test_non_int_passed_to_init(self):
        int_list = IntegerList('a')
        self.assertEqual([], int_list._IntegerList__data)

    def test_adding_regular_int(self):
        self.int_list.add(9)
        result = self.int_list.get_data()
        self.assertEqual([3, 6, 8, 9], result)

    def test_adding_non_int_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add('a')
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_removing_existing_index(self):
        self.int_list.remove_index(0)
        self.assertEqual([6, 8], self.int_list._IntegerList__data)

    def test_removing_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(3)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_getting_valid_element(self):
        result = self.int_list.get(0)
        self.assertEqual(3, result)

    def test_getting_invalid_element_raises(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(3)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_inserting_index_raises(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(3, 1)
        self.assertEqual(str(ie.exception), "Index is out of range")

        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, "a")
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_inserting_valid_int(self):
        self.int_list.insert(0, 1)
        self.assertEqual([1, 3, 6, 8], self.int_list._IntegerList__data)

    def test_get_biggest_returns_correct_value(self):
        result = self.int_list.get_biggest()
        self.assertEqual(8, result)

    def test_getting_index_of_element(self):
        result = self.int_list.get_index(3)
        self.assertEqual(0, result)

    def test_getting_invalid_index_of_element_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.get_index(1)
        self.assertEqual(str(ve.exception), f"1 is not in list")


if __name__ == '__main__':
    unittest.main()