import os
import sys
import unittest
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import game

class TestPerson(unittest.TestCase):
    def test_set_person(self):
        hp = random.randint(1, 100)
        mp = random.randint(1, 100)
        atk = random.randint(1, 100)
        df = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

        person = game.Person("bob", hp, mp, atk, df, magic, [])
        self.assertTrue(person.hp, hp)
        self.assertTrue(person.mp, mp)
        self.assertTrue(person.atkl, atk-10)
        self.assertTrue(person.df, df)
        self.assertTrue(person.magic, magic)
        self.assertGreater(person.mp, mp-2)
        self.assertEqual("bob", person.name)

class TestGenerateDamage(unittest.TestCase):
    def test_generate_damage(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", rand_int, rand_int, rand_int, rand_int, magic, [])
        damage = person.generate_damage()

        self.assertLess(damage, rand_int+11)
        self.assertGreater(damage, rand_int-11)

class TestTakeDamage(unittest.TestCase):
    def test_take_damage(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", 200, rand_int, rand_int, rand_int, magic, [])
        new_hp = person.take_damage(rand_int)
        self.assertEqual(200-rand_int,new_hp)
    def test_if_zero(self):
        rand_int = random.randint(10, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", 5, rand_int, rand_int, rand_int, magic, [])
        new_hp = person.take_damage(rand_int)
        self.assertEqual(0,new_hp)

class TestHeal(unittest.TestCase):
    def test_heal(self):
        random_int = random.randint(10, 100)
        person = game.Person("bob", 300, 0, 0, 0, [], [])
        person.take_damage(200)
        new_hp = person.heal(random_int)
        self.assertEqual(new_hp, 100 + random_int)

class TestGetHp(unittest.TestCase):
    def test_get_hp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", rand_int, rand_int, rand_int, rand_int, magic, [])
        self.assertEqual(rand_int, person.get_hp())

class TestGetMaxHp(unittest.TestCase):
    def test_get_max_hp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", rand_int, rand_int, rand_int, rand_int, magic, [])
        self.assertEqual(rand_int, person.get_max_hp())

class TestGetMp(unittest.TestCase):
    def test_get_mp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", 200, rand_int, rand_int, rand_int, magic, [])
        self.assertEqual(rand_int, person.get_mp())

class TestGetMaxMp(unittest.TestCase):
    def test_get_max_mp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", 200, rand_int, rand_int, rand_int, magic, [])
        self.assertEqual(rand_int, person.get_max_mp())

class TestReduceMp(unittest.TestCase):
    def test_reduce_mp(self):
        rand_int = random.randint(40, 100)
        spell_cost = random.randint(10,15)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person("bob", 200, rand_int, rand_int, rand_int, magic, [])
        person.reduce_mp(spell_cost)
        self.assertEqual(person.get_mp(), rand_int - spell_cost)



if __name__=="__main__":
    unittest.main()
