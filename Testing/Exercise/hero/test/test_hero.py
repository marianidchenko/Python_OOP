from unittest import TestCase, main
from Testing.Exercise.hero.project.hero import Hero


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero("name", 3, 50, 25)
        self.strong = Hero("hero1", 100, 100, 100)
        self.equal = Hero("hero2", 3, 50, 25)
        self.weak = Hero("hero3", 1, 10, 0)

    def test_init_returns_correct_values(self):
        self.assertEqual("name", self.hero.username)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(25, self.hero.damage)

    def test_batting_against_yourself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_health_0_or_below(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.strong)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_with_health_0_or_below(self):
        self.strong.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.strong)
        self.assertEqual(f"You cannot fight hero1. He needs to rest", str(ex.exception))

    def test_battle_with_hero_win(self):
        result = self.hero.battle(self.weak)
        self.assertEqual(-65, self.weak.health)
        self.assertEqual(4, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(30, self.hero.damage)
        self.assertEqual(result, "You win")

    def test_battle_draw(self):
        result = self.hero.battle(self.equal)
        self.assertEqual(result, "Draw")

    def test_battle_with_hero_loss(self):
        result = self.hero.battle(self.strong)
        self.assertEqual(-9950, self.hero.health)
        self.assertEqual(101, self.strong.level)
        self.assertEqual(30, self.strong.health)
        self.assertEqual(105, self.strong.damage)
        self.assertEqual(result, "You lose")

    def test_str_returns_correct_values(self):
        expected = "Hero name: 3 lvl\nHealth: 50\nDamage: 25\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()