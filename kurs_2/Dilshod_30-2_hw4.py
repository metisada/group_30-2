import random
from random import randint, choice
from enum import Enum

class Ability(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    INVISIBLITY = 5
    REDUCE_LIFE = 6
    REVIVE = 7
    BOMBING = 8

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} | Health: {self.__health} | Damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f'| Defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass

class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = random.randint(2, 5)  # 2,3,4,5
        if boss.health > 0:
            boss.health -= coefficient * self.damage
            print(f'Warrior hits critically {coefficient * self.damage}')

class Magic(Hero):

    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.damage += randint(1,5)

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        self.__blocked_damage = boss.damage * randint(1,99)//100
        self.health += self.__blocked_damage
        boss.health -= self.__blocked_damage
        print(f'Berserk blocked and reverted {self.__blocked_damage} damage')

class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.INVISIBLITY)
        self.__is_invisible = False
        self.__accumulated_damage = 0
        self.__invisble_count = 0

    def apply_super_power(self, boss, heroes):
        if not self.__is_invisible and self.__invisble_count < 2:
            if randint(0,1) == 1:
                self.__invisble_count += 1
                self.health += boss.damage
                self.__accumulated_damage += boss.damage
                self.__is_invisible = True
                print(f'Avrora is invisible. Health is {self.health}, accumulated damage is {self.__accumulated_damage}')
        elif self.__is_invisible and self.__invisble_count < 2:
            self.__invisble_count += 1
            self.health += boss.damage
            self.__accumulated_damage += boss.damage
            print(f'Avrora is invisible. Health is {self.health}, accumulated damage is {self.__accumulated_damage}')
            if self.__invisble_count == 2:
                self.__is_invisible = False

    def hit(self, boss):
        if not self.__is_invisible:
            boss.health -= self.damage + self.__accumulated_damage
            self.__accumulated_damage = 0


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.REDUCE_LIFE)

    def apply_super_power(self, boss, heroes):
        if round_number != 0 and round_number % 2 == 0:
            number_of_health = randint(1,40)
            boss.health -= number_of_health
            random_hero = random.choice(heroes)
            while random_hero == self:
                random_hero = random.choice(heroes)
            random_hero.health += number_of_health
            print(f'Hacker reduced {number_of_health} and healed {random_hero.name}')

class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.REVIVE)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                hero.health = self.health
                self.health = 0
                print(f'Witcher revived the hero {hero.name}')
                break

    def hit(self, boss):
        pass

class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOMBING)
        self.__is_bomb_used = False

    def apply_super_power(self, boss, heroes):
        if self.health == 0 and not self.__is_bomb_used:
            boss.health -= 100
            print(f'Bomber died and used bomb!')

    def hit(self, boss):
        if self.health > 0 and boss.defence != Ability.BOMBING:
            boss.health -= self.damage

round_number = 0

def start():
    boss = Boss('Boss', 1000, 50)
    berserk = Berserk('Berserk', 270, 10)
    avrora = Avrora('Avrora', 170, 20)
    hacker = Hacker('Hacker', 250, 15)
    witcher = Witcher('Witcher', 200,15)
    bomber = Bomber('Bomber', 200, 10)
    heroes_list = [ berserk, avrora,hacker,witcher, bomber]

    show_stats(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


def show_stats(boss, heroes):
    print(f'ROUND {round_number} --------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if (hero.health > 0 and boss.health > 0 \
                and boss.defence != hero.super_ability) or isinstance(hero,Bomber):
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)


start()
