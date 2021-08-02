from unittest import TestCase, main
from Testing.Exercise.vehicle.project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10, 3)   # capacity = fuel, fuel_consumption = 1.25

    def test_vehicle_default_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init_returns_correct_value(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(10, self.vehicle.capacity)
        self.assertEqual(3, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(4)
        self.assertEqual(5, self.vehicle.fuel)

    def test_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_under_capacity(self):
        self.vehicle.drive(4)
        self.vehicle.refuel(3)
        self.assertEqual(8, self.vehicle.fuel)

    def test_refuel_over_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_returns_correct_value(self):
        expected = "The vehicle has 3 " \
                   "horse power with 10 fuel left and 1.25 fuel consumption"
        result = str(self.vehicle)
        self.assertEqual(expected, result)