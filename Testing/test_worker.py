class Worker:
  def __init__(self, name, salary, energy):
    self.name = name
    self.salary = salary
    self.energy = energy
    self.money = 0

  def work(self):
    if self.energy <= 0:
        raise Exception('Not enough energy.')

    self.money += self.salary
    self.energy -= 1

  def rest(self):
    self.energy += 1

  def get_info(self):
    return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_initialize_name_salary_energy(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_energy_increased_after_resting(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.rest()
        result = self.worker.energy
        expected = 11
        self.assertEqual(expected, result)

    def test_working_with_0_or_less_energy_raises(self):
        worker = Worker("Tired", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual(str(ex.exception), "Not enough energy.")

    def test_salary_increasing_after_work(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_energy_decreasing_after_work(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_get_info_returning_correct_values(self):
        result = self.worker.get_info()
        expected = f'Test has saved 0 money.'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
