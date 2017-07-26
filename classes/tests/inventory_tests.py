import os
import sys
import unittest
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from inventory import Item

class SetItem(unittest.TestCase):
    def test_init_item(self):
        potion = Item("Potion", "potion", "Heals 50 HP", 50)
        self.assertEqual("Potion", potion.name)
        self.assertEqual("potion", potion.type)
        self.assertEqual("Heals 50 HP", potion.description)
        self.assertEqual(50, potion.prop)
