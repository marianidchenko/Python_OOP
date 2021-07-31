from Testing.CarManager.car_manager import Car
from unittest import TestCase, main


class CarTest(TestCase):
    def setUp(self):
        self.car = Car("make", "model", 1, 10)

# init

    def test_init_values(self):
        self.assertEqual("make", self.car.make)
        self.assertEqual("model", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(10, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

# make

    def test_set_make_valid_value(self):
        self.car.make = "New make"
        self.assertEqual("New make", self.car.make)
        
    def test_set_make_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

# model

    def test_set_model_valid_value(self):
        self.car.model = "New model"
        self.assertEqual("New model", self.car.model)

    def test_set_model_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

# fuel

    def test_set_fuel_valid_value(self):
        self.car.fuel_amount = 5
        self.assertEqual(5, self.car.fuel_amount)

    def test_set_fuel_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -2
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

# fuel consumption
    
    def test_set_fuel_consumption_valid_value(self):
        self.car.fuel_consumption = 5
        self.assertEqual(5, self.car.fuel_consumption)

    def test_set_fuel_consumption_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -2
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

# fuel capacity

    def test_set_fuel_capacity_valid_value(self):
        self.car.fuel_capacity = 5
        self.assertEqual(5, self.car.fuel_capacity)

    def test_set_fuel_capacity_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

# drive

    def test_drive_with_enough_fuel(self):
        self.car.fuel_amount = 1
        self.car.drive(10)
        self.assertEqual(0.9, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    # refuel

    def test_refuel_with_valid_value(self):
        self.car.refuel(3)
        self.assertEqual(3, self.car.fuel_amount)

    def test_refuel_with_invalid_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-3)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")


if __name__ == '__main__':
    main()