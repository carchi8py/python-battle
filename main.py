from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n\n")
print("NAME                   Hp                                mp")
print("                       _________________________         __________ ")
print(Bcolors.BOLD + "Valos:        " +
                  "460/460 |" + Bcolors.OKGREEN + "██████████               " + Bcolors.ENDC + Bcolors.BOLD + "|  " +
                  "65/65 |" + Bcolors.OKBLUE + "████      " + Bcolors.ENDC + "|")
print("                       _________________________         __________ ")
print("Valos:        460/460 |                         |  65/65 |          |")
print("                       _________________________         __________ ")
print("Valos:        460/460 |                         |  65/65 |          |")

#black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("thunder", 10, 100, "black")
blizzard = Spell("blizzard", 10, 100, "black")
meteor = Spell("meteor", 20, 200, "black")
quake = Spell("quake", 14, 140, "black")

#white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
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
player = Person(460, 65, 60, 34, player_magic, player_item)
enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print("========================")
    player.choose_action()
    choice = int(input("Choose action:")) - 1

    #if this is 0 we are doing a melee attack
    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")

    #if this is 1 we are doing magic attack
    elif choice == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1
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
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKGREEN + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + Bcolors.ENDC)
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
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(Bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + Bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(Bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + Bcolors.ENDC)


    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)
    print("-----------------------------")
    print("Enemy HP:", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your HP:", Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolors.ENDC)
    print("Your MP:", Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Bcolors.ENDC + "\n")

    #check if someone has died
    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You win" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "Your enemy has defeated you!" + Bcolors.ENDC)
        running = False
