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



if __name__=="__main__":
    unittest.main()