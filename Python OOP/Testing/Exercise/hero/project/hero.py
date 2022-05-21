class Hero:
    username: str
    health: float
    damage: float
    level: int

    def __init__(self, username: str, level: int, health: float, damage: float):
        self.username = username
        self.level = level
        self.health = health
        self.damage = damage

    def battle(self, enemy_hero):
        if enemy_hero.username == self.username:
            raise Exception("You cannot fight yourself")

        if self.health <= 0:
            raise ValueError(
                "Your health is lower than or equal to 0. You need to rest")

        if enemy_hero.health <= 0:
            raise ValueError(
                f"You cannot fight {enemy_hero.username}. He needs to rest")

        player_damage = self.damage * self.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level

        self.health -= enemy_hero_damage
        enemy_hero.health -= player_damage

        if self.health <= 0 and enemy_hero.health <= 0:
            return "Draw"

        if enemy_hero.health <= 0:
            return self._extracted_from_battle_21(self, "You win")
        return self._extracted_from_battle_21(enemy_hero, "You lose")

    # TODO Rename this here and in `battle`
    def _extracted_from_battle_21(self, arg0, arg1):
        arg0.level += 1
        arg0.health += 5
        arg0.damage += 5
        return arg1

    def __str__(self):
        return f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
