from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

import random

#black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("thunder", 25, 600, "black")
blizzard = Spell("blizzard", 25, 600, "black")
meteor = Spell("meteor", 40, 1200, "black")
quake = Spell("quake", 14, 140, "black")

#white magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 35, 1500, "white")

#Create some items
potion = Item("Potion", "potion", "Heals 300 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 500 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 100 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
megaelixer = Item("MegaElixer", "elixer", "Fully restores all party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_item = [{"item": potion, "quantity": 15},
               {"item": hipotion, "quantity": 5},
               {"item": superpotion, "quantity": 5},
               {"item": elixer, "quantity": 5},
               {"item": megaelixer, "quantity": 2},
               {"item": grenade, "quantity": 5}]

#Instantiate People
player1 = Person("Valos:", 3260, 132, 300, 34, player_magic, player_item)
player2 = Person("Nick :", 4160, 188, 311, 34, player_magic, player_item)
player3 = Person("Robot:", 4089, 174, 288, 34, player_magic, player_item)
enemy1 = Person("Imp  :", 1250, 130, 560, 325, [], [])
enemy2 = Person("Magus:", 18200, 701, 550, 25, [], [])
enemy3 = Person("Imp  :", 1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print("========================")
    print("\n\n")
    print("NAME                     HP                                   MP")
    for player in players:
        player.get_stats()
    print('\n')
    for enemy in enemies:
        enemy.get_enemy_stats()
    for player in players:
        player.choose_action()
        choice = int(input("    Choose action:")) - 1

        #if this is 0 we are doing a melee attack
        if choice == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name + " for", dmg, "points of damage.")
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]

        #if this is 1 we are doing magic attack
        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic:")) - 1
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + Bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(Bcolors.OKGREEN + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name + Bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]
        elif choice == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + "None left..." + Bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1


            if item.type == "potion":
                player.heal(item.prop)
                print(Bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + Bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(Bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + Bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(Bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name + Bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

    enemy_choice = 1
    target = random.randrange(0,len(players))
    enemy_dmg = enemies[0].generate_damage()
    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    defeated_enemies = 0
    defeated_players = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    if defeated_enemies == len(enemies):
        print(Bcolors.OKGREEN + "You win" + Bcolors.ENDC)
        running = False
    if defeated_players == len(players):
        print(Bcolors.FAIL + "Your enemies have defeated you!" + Bcolors.ENDC)
        running = False
