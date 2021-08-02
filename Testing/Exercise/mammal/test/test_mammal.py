from Testing.Exercise.mammal.project.mammal import Mammal
from unittest import TestCase


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("name", "type", "sound")

    def test_init_returns_correct_value(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_string(self):
        result = self.mammal.make_sound()
        expected = "name makes sound"
        self.assertEqual(expected, result)

    def test_get_kingdom_returns_correct_string(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_returning_correct_values(self):
        result = self.mammal.info()
        self.assertEqual("name is of type type", result)


