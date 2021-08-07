from unittest import TestCase, main

from Retake_19_12_2020.testing.project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self):
        self.factory = PaintFactory("name", 10)

    def test_init_returns_correct_values(self):
        self.assertEqual("name", self.factory.name)
        self.assertEqual(10, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_adding_invalid_ingredient_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("pink", 3)
        self.assertEqual(f"Ingredient of type pink not allowed in PaintFactory", str(ex.exception))

    def test_adding_too_much_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("red", 12)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_adding_ingredient_returns_correct_listing(self):
        self.assertEqual({}, self.factory.ingredients)
        self.factory.add_ingredient("red", 3)
        self.assertEqual({"red": 3}, self.factory.ingredients)

    def test_remove_ingredient_not_in_ingredients_raised(self):
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("red", 3)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_bigger_quantity_of_ingredient_than_available_raises(self):
        self.factory.add_ingredient("red", 3)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("red", 4)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_correct_ingredient_returns_ingredients_as_expected(self):
        self.factory.add_ingredient("red", 3)
        self.factory.remove_ingredient("red", 2)
        self.assertEqual({"red": 1}, self.factory.ingredients)

    def test_products_property_returns_correct_values(self):
        self.assertEqual({}, self.factory.ingredients)


if __name__ == '__main__':
    main()