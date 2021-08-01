class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self):
        self.cat = Cat("Toast")

    def test_cat_size_increasing_after_eating(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_if_fed_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_cat_can_eat_when_fed_raises(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_if_cat_can_sleep_when_not_fed_raises(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_if_sleepy_after_sleeping(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()