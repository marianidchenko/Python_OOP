import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        self.assertEqual(vet.name, "Bob")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])
        self.assertEqual(Vet.space, 5)

    def test_register_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet2 = Vet("Peter")
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Doggy registered in the clinic")
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet2.animals, [])

    def test_register_unsuccessfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        for i in range(6):
            vet.register_animal(str(i))
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Not enough space")
        self.assertEqual(len(Vet.animals), 5)
        self.assertEqual(len(vet.animals), 5)

    def test_unregister_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet.register_animal("Kitty")
        res = vet.unregister_animal("Kitty")
        self.assertEqual(res, "Kitty unregistered successfully")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])


if __name__ == "__main__":
    unittest.main()