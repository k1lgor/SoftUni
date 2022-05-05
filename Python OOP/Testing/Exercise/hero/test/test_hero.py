from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('manqk', 100, 100, 50)
        self.enemy = Hero('lek', 100, 100, 50)

    def test_init(self):
        username = 'manqk'
        level = 100
        health = 100
        damage = 50
        hero = Hero(username, level, health, damage)
        self.assertEqual('manqk', hero.username)
        self.assertEqual(100, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(50, hero.damage)

    def test_str(self):
        result = f"Hero manqk: 100 lvl\n" \
                 f"Health: 100\n" \
                 f"Damage: 50\n"
        expected = self.hero.__str__()
        self.assertEqual(result, expected)

    def test_battle_same_name(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_health(self):
        for health in [0, -50]:
            self.hero.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_enemy_health(self):
        for health in [0, -50]:
            self.enemy.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f'You cannot fight {self.enemy.username}. He needs to rest', str(ex.exception))

    def test_battle_draw(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual('Draw', result)
        self.assertEqual(-4900.0, self.hero.health)
        self.assertEqual(-4900.0, self.enemy.health)

    def test_battle_win(self):
        enemy = Hero('lek', 1, 100.0, 50)
        result = self.hero.battle(enemy)
        self.assertEqual('You win', result)
        self.assertEqual(101, self.hero.level)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(-4900.0, enemy.health)

    def test_battle_lose(self):
        hero = Hero('manqk', 1, 100, 50)
        enemy = Hero('lek', 1, 100, 50)
        result = hero.battle(enemy)
        self.assertEqual('You lose', result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(55, enemy.damage)
        self.assertEqual(50, hero.health)


if __name__ == '__main__':
    main()
