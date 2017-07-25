import os
import sys
import unittest
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from magic import Spell

class SetMagic(unittest.TestCase):
    def test_init_spell(self):
        spell = Spell("Fire", 10, 100, "black")
        self.assertTrue(spell.name,"Fire")
        self.assertTrue(spell.cost, 10)
        self.assertTrue(spell.dmg, 100)
        self.assertTrue(spell.type, "black")


class TestGenerateSpellDamage(unittest.TestCase):
    def test_generate_spell_damage(self):
        rand_int = random.randint(1, 100)
        blizzard = Spell("blizzard", 10, 100, "black")
        dmg = blizzard.generate_damage()
        self.assertLess(100 - 16, dmg)
        self.assertGreater(100 + 16, dmg)

if __name__=="__main__":
    unittest.main()