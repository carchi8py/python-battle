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

        person = game.Person(hp, mp, atk, df, magic)
        self.assertTrue(person.hp, hp)
        self.assertTrue(person.mp, mp)
        self.assertTrue(person.atkl, atk-10)
        self.assertTrue(person.df, df)
        self.assertTrue(person.magic, magic)
        self.assertGreater(person.mp, mp-2)

class TestGenerateDamage(unittest.TestCase):
    def test_generate_damage(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(rand_int, rand_int, rand_int, rand_int, magic)
        damage = person.generate_damage()

        self.assertLess(damage, rand_int+11)
        self.assertGreater(damage, rand_int-11)

class TestGenerateSpellDamage(unittest.TestCase):
    def test_generate_spell_damage(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80}]
        person = game.Person(rand_int, rand_int, rand_int, rand_int, magic)
        spell1 = person.generate_spell_damage(0)
        spell2 = person.generate_spell_damage(1)

        self.assertLess(spell1,66)
        self.assertGreater(spell1, 54)
        self.assertLess(spell2,86)
        self.assertGreater(spell2, 74)

class TestTakeDamage(unittest.TestCase):
    def test_take_damage(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(200, rand_int, rand_int, rand_int, magic)
        new_hp = person.take_damage(rand_int)
        self.assertEqual(200-rand_int,new_hp)
    def test_if_zero(self):
        rand_int = random.randint(10, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(5, rand_int, rand_int, rand_int, magic)
        new_hp = person.take_damage(rand_int)
        self.assertEqual(0,new_hp)

class TestGetHp(unittest.TestCase):
    def test_get_hp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(rand_int, rand_int, rand_int, rand_int, magic)
        self.assertEqual(rand_int, person.get_hp())

class TestGetMaxHp(unittest.TestCase):
    def test_get_max_hp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(rand_int, rand_int, rand_int, rand_int, magic)
        self.assertEqual(rand_int, person.get_max_hp())

class TestGetMp(unittest.TestCase):
    def test_get_mp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(200, rand_int, rand_int, rand_int, magic)
        self.assertEqual(rand_int, person.get_mp())

class TestGetMaxMp(unittest.TestCase):
    def test_get_max_mp(self):
        rand_int = random.randint(1, 100)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(200, rand_int, rand_int, rand_int, magic)
        self.assertEqual(rand_int, person.get_max_mp())

class TestReduceMp(unittest.TestCase):
    def test_reduce_mp(self):
        rand_int = random.randint(40, 100)
        spell_cost = random.randint(10,15)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60}]
        person = game.Person(200, rand_int, rand_int, rand_int, magic)
        person.reduce_mp(spell_cost)
        self.assertEqual(person.get_mp(), rand_int - spell_cost)

class GetSpellName(unittest.TestCase):
    def test_get_spell_name(self):
        rand_int = random.randint(1, 100)
        spell = random.randint(0,2)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]
        person = game.Person(200, rand_int, rand_int, rand_int, magic)
        self.assertEqual(magic[spell]["name"], person.get_spell_name(spell))

class GetSpellCost(unittest.TestCase):
    def test_get_spell_cost(self):
        rand_int = random.randint(1, 100)
        spell = random.randint(0,2)
        magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]
        person = game.Person(200, rand_int, rand_int, rand_int, magic)
        self.assertEqual(magic[spell]["cost"], person.get_spell_mp_cost(spell))



if __name__=="__main__":
    unittest.main()