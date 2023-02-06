import random
import time
import sys


class Enemy:
    def __init__(self, hp, damage, agi, name):
        self.hp = hp
        self.damage = damage
        self.agi = agi
        self.name = name

    def godly_slash(self):
        print('Yaldabaoth does a godly slash against you!')
        damage = self.damage + random.randint(1, 10)
        if damage >= 35:
            print(f'That is a lot of damage! ({damage})')
        time.sleep(1)
        return damage

    def torment(self, you):
        print('Yaldabaoth torments you!')
        damage = self.damage + random.randint(1, 3)
        you.agi = you.agi - 1
        print(f'Your agility is now {you.agi}')
        if damage >= 35:
            print(f'That is a lot of damage {you.damage}')
        time.sleep(1)
        return damage

    def apocalypse(self):
        print('Yaldabaoth brings the Apocalypse!')
        damage = self.damage + random.randint(5, 35)
        if damage >= 35:
            print(f'That is a lot of damage! {damage}')
        time.sleep(1)
        return damage

    def heavens_ward(self):
        print('Yaldabaoth opens the skies and heals himself!')
        self.hp = self.hp + 100
        print(f'Yaldabaoth now has {self.hp}')
        time.sleep(1)
        damage = 0
        return damage

    def murloc_slash(self):
        print('Grrlgrrl slashes you!')
        damage = self.damage + random.randint(1, 20)
        if damage >= 35:
            print(f'That is a lot of damage! {damage}')
        time.sleep(1)
        return damage

    def slimy_mess(self, player):
        print('Grrlgrrl throws his feces at you!')
        self.damage = self.damage + 1
        player.agi = player.agi - 2
        print(f'Your agility is now {player.agi}')
        time.sleep(1)
        damage = 0
        return damage

    def murloc_horde(self):
        print('Grrlgrrl invokes an army of murlocs to attack you!')
        damage = self.damage + random.randint(10, 30)
        if damage >= 35:
            print(f'That is a lot of damage! {damage}')
        time.sleep(1)
        return damage

    def blobby_attack(self, player):
        print('Eeew! The Blob bounced against you!')
        player.agi = player.agi - 2
        damage = self.damage + random.randint(1, 20)
        if damage >= 100:
            print(f'That is so much damage! {damage}')
        time.sleep(1)
        return damage

    def sabotage(self, player):
        print('Eeew! The Blob left a mess on the entire floor!')
        self.agi = self.agi + 1
        player.agi = player.agi - 1
        print(f'The the Blob can move faster and you cannot! The Blobs agility {self.agi}. Your agility {player.agi}')
        time.sleep(1)
        damage = 0
        return damage

    def anti_noob_slash(self):
        print('Holger slashes you!')
        damage = self.damage + random.randint(1, 10)
        if damage >= 35:
            print(f'That is a lot of damage! {damage}')
        time.sleep(1)
        return damage

    def quick_attack(self):
        print('Holger pushes himself to the limit attacking you very fast!')
        self.agi = self.agi + 1
        damage = self.damage + random.randint(1, 5)
        if damage >= 35:
            print(f'That is a lot of damage! {damage}')
        time.sleep(1)
        return damage

    def noob_killer(self):
        print('Holger attacks you with all his power!')
        damage = self.damage + random.randint(10, 20)
        if damage >= 35:
            print(f'That is a lot of damage! {damage}')
        self.damage = self.damage + random.randint(1, 3)
        time.sleep(1)
        return damage

    def howl(self, player):
        print('Holger howls!')
        self.damage = self.damage + 2
        player.damage = player.damage - 1
        print(f'Holger got stronger and you got weaker! Your damage now is {player.damage}')
        time.sleep(1)
        damage = 0
        return damage


class Archer:
    def __init__(self, hp, damage, agi, name):
        self.hp = hp
        self.damage = damage
        self.agi = agi
        self.name = name

    def golden_arrow(self):  # concept of an attack
        print('You attacked with a golden arrow!')
        damage = self.damage + random.randint(10, 50)
        if damage >= 20:
            print(f'That is a lot of damage ({damage})')
        time.sleep(1)
        return damage

    def slowing_arrow(self, enemy):
        print('You threw an slowing arrow against your enemy!')
        enemy.agi = enemy.agi - 1
        damage = self.damage + random.randint(1, 3)
        time.sleep(1)
        return damage

    def super_arrow(self):
        print('You threw a super arrow against your enemy!')
        damage = self.damage + random.randint(10, 80)
        if damage >= 100:
            print(f'That is a lot of damage! ({damage})')
        time.sleep(1)
        return damage

    def vigor(self):
        self.hp = self.hp + 10
        self.agi = self.agi + 3
        print(f'Your health is now {self.hp}')
        time.sleep(1)
        return 0


class Warrior:
    def __init__(self, hp, damage, agi, name=''):
        self.hp = hp
        self.damage = damage
        self.agi = agi
        self.name = name

    def hard_slash(self):
        print('You did a hard slash against your enemy!')
        damage = self.damage + random.randint(1, 100)
        if damage >= 100:
            print(f'That is a lot of damage ({damage})')
        time.sleep(1)
        return damage

    def precision_slash(self):
        print('You did a precision slash against your enemy!')
        damage = self.damage + random.randint(25, 70)
        if damage >= 80:
            print(f'That is a lot of damage ({damage})')
        time.sleep(1)
        return damage

    def berserk(self):
        self.hp = self.hp - 15
        self.agi = self.agi + 4
        print(f'You feel faster and deadlier. Your health is now {self.hp}')
        time.sleep(1)
        return 0

    def onslaught(self):
        self.hp = self.hp - 15
        damage = self.damage + random.randint(100, 300)
        print(f'You gave 15 of your life (actual hp: {self.hp}), but you did {damage} points of damage!')
        if damage >= 250:
            print("OH SHIT! That's a lot of damage!")
        time.sleep(1)
        return damage


def instance():
    print('Select your option: ')
    print('\t1 Create Character \n\t2 Battle (Only if Character is done)\n\t3 Exit\n')
    option = int(input())
    try:
        if option == 1:
            char_creator()
            instance()
        elif option == 2:
            battle(char_selector(), enemy_creator())
            instance()
        elif option == 3:
            print('Closing Program.')
            time.sleep(2)
            sys.exit()
        elif option == 5:
            print(playerCharacters)
    except ValueError:
        print('Only numbers, mate')
        instance()


def name_maker():
    name = input("Insert your character's name\n")
    return name


def char_creator():
    try:
        option = int(input('Select your character class: \n\t1 Warrior\n\t2 Archer\n'))
        print('*Warriors are stronger than Archers, but Archers are usually faster*')
        if option == 1:
            char = Warrior(random.randint(300, 600), random.randint(25, 50), random.randint(7, 18), name_maker())
            print(f'Your stats are: \n\tHit points: {char.hp}\n\tDamage: {char.damage}\n')
            time.sleep(1)
            playerCharacters.append(char)
            print(f'You successfully created {char.name}')
            time.sleep(1)
            return playerCharacters
        elif option == 2:
            char = Archer(random.randint(200, 500), random.randint(15, 40), random.randint(9, 20), name_maker())
            print(f'Your stats are: \n\tHit points: {char.hp}\n\tDamage: {char.damage}\n')
            time.sleep(1)
            playerCharacters.append(char)
            print(f'You successfully created {char.name}')
            time.sleep(1)
            return playerCharacters
        else:
            print('Wrong number, mate.')
            char_creator()
    except ValueError:
        print('Only numbers, please.')
        char_creator()


def char_selector():
    des_name = input('Select your character by typing its name\n')
    for _, v in enumerate(playerCharacters):
        if des_name == v.name:
            return v
    else:
        print('Character not found.')
        instance()


def enemy_creator():
    enemy = Enemy(random.randint(300, 1200), random.randint(30, 35), random.randint(9, 13), 'Boogieman')
    enemy_selector = random.randint(1, 1000)
    if enemy_selector in range(900, 1000):
        print('HOLY SHIT! YOUR ENEMY IS GOD')
        enemy = Enemy(random.randint(2000, 3001), random.randint(25, 40), random.randint(10, 18), 'Yaldabaoth')
        time.sleep(3)
    elif enemy_selector in range(500, 899):
        print('A mutant murloc appears!')
        enemy = Enemy(random.randint(300, 1200), random.randint(30, 35), random.randint(9, 18), 'Grrlgrrl')
        time.sleep(1)
    elif enemy_selector in range(250, 499):
        print('A massive blob appears!')
        enemy = Enemy(random.randint(2500, 3001), random.randint(3, 125), random.randint(1, 15), 'Blob')
        time.sleep(1)
    elif enemy_selector in range(1, 249):
        print('Holger, the noob killer, appears!')
        enemy = Enemy(random.randint(1500, 2200), random.randint(10, 35), random.randint(4, 18), 'Holger')
        time.sleep(1)
    print(f'Your enemy has {enemy.hp} of health and {enemy.damage} of damage')
    time.sleep(1)
    return enemy


def turn_resolver(agi_player, agi_enemy):
    initiative_player = agi_player + random.randint(1, 10)
    initiative_enemy = agi_enemy + random.randint(1, 16)
    if initiative_player > initiative_enemy:
        return True
    elif initiative_enemy > initiative_player:
        return False
    elif initiative_enemy == initiative_player:
        return None


def attack_module_player(player_damage, enemy_hp):
    return enemy_hp - player_damage


def attack_selector_player(battler, enemy):
    try:
        if type(battler) == Archer:
            print('1 Golden Arrow\t2 Slowing Arrow\n3 Super Arrow\t4 Vigor')
            option = int(input('Insert a number to select an attack: '))
            if option == 1:
                return battler.golden_arrow()
            elif option == 2:
                return battler.slowing_arrow(enemy)
            elif option == 3:
                return battler.super_arrow()
            elif option == 4:
                return battler.vigor()
            else:
                print('Doing default attack.')
                return battler.damage
        elif type(battler) == Warrior:
            print('1 Hard Slash\t2 Precision Slash\n3 Berserk\t4 Onslaught')
            option = int(input('Insert a number to select an attack: '))
            if option == 1:
                return battler.hard_slash()
            elif option == 2:
                return battler.precision_slash()
            elif option == 3:
                return battler.berserk()
            elif option == 4:
                return battler.onslaught()
            else:
                print('Wrong number, please select one of the four numbers you were given. Doing default attack.')
                return battler.damage
    except ValueError:
        print('Please, use only the numbers you were given. Doing default attack.')
        return battler.damage


def attack_module_enemy(enemy_damage, player_hp):
    return player_hp - enemy_damage


def attack_module_enemy2(enemy, player):
    if enemy.name == 'Yaldabaoth':
        if enemy.hp in range(1500, 3000):
            healthy_attack = random.randint(1, 200)
            if healthy_attack in range(1, 150):
                return player.hp - enemy.godly_slash()
            elif healthy_attack in range(151, 200):
                return player.hp - enemy.torment(player)
        elif enemy.hp in range(1000, 1499):
            damaged_attack = random.randint(1, 100)
            if damaged_attack in range(1, 60):
                return player.hp - enemy.godly_slash()
            elif damaged_attack in range(61, 94):
                return player.hp - enemy.torment(player)
            elif damaged_attack in range(95, 100):
                return player.hp - enemy.apocalypse()
        elif enemy.hp in range(1, 1000):
            scared_attack = random.randint(1, 150)
            if scared_attack in range(1, 50):
                return player.hp - enemy.heavens_ward()
            elif scared_attack in range(51, 100):
                return player.hp - enemy.apocalypse()
            elif scared_attack in range(101, 150):
                return player.hp - enemy.torment(player)
    elif enemy.name == 'Grrlgrrl':
        if enemy.hp in range(600, 1200):
            healthy_attack = random.randint(1, 100)
            if healthy_attack in range(10, 100):
                return player.hp - enemy.murloc_slash()
            elif healthy_attack in range(1, 9):
                return player.hp - enemy.slimy_mess(player)
            else:
                return player.hp - enemy.damage
        elif enemy.hp in range(1, 599):
            scared_attack = random.randint(1, 100)
            if scared_attack in range(1, 40):
                return player.hp - enemy.murloc_horde()
            elif scared_attack in range(41, 70):
                return player.hp - enemy.slimy_mess(player)
            elif scared_attack in range(71, 100):
                return player.hp - enemy.murloc_slash()
            else:
                return player.hp - enemy.damage
    elif enemy.name == 'Blob':
        if enemy.hp in range(1000, 3000):
            return player.hp - enemy.blobby_attack(player)
        elif enemy.hp in range(1, 999):
            scared_attack = random.randint(1, 10)
            if scared_attack in range(1, 5):
                return player.hp - enemy.blobby_attack(player)
            elif scared_attack in range(6, 10):
                return player.hp - enemy.sabotage(player)
    elif enemy.name == 'Holger':
        if enemy.hp in range(1000, 2200):
            healthy_attack = random.randint(1, 100)
            if healthy_attack in range(1, 89):
                return player.hp - enemy.anti_noob_slash()
            elif healthy_attack in range(90, 100):
                return player.hp - enemy.quick_attack()
        elif enemy.hp in range(1, 999):
            scared_attack = random.randint(1, 100)
            if scared_attack in range(1, 10):
                return player.hp - enemy.noob_killer()
            elif scared_attack in range(11, 50):
                return player.hp - enemy.quick_attack()
            elif scared_attack in range(51, 60):
                return player.hp - enemy.howl(player)
            elif scared_attack in range(61, 100):
                return player.hp - enemy.anti_noob_slash()


def dead_deleter(alive):
    print('\nGiving your hero the proper burial they deserves...\n')
    time.sleep(2)
    for _, dead in enumerate(alive):
        if dead.hp <= 0:
            alive = alive.remove(dead)


def battle(battler, enemy):
    try:
        print('Good luck !')
        time.sleep(1)
        counter = 0
        while battler.hp >= 0 and enemy.hp >= 0:
            counter = counter + 1
            print(f'\n*---------------Turn number {counter}---------------*\n')
            if counter > 50:
                print('What a battle!')
            result = turn_resolver(battler.agi, enemy.agi)
            if result is True:
                enemy.hp = attack_module_player(attack_selector_player(battler, enemy), enemy.hp)
                print(f'Your enemy now has {enemy.hp} of health')
                time.sleep(1)
            elif result is False:
                battler.hp = attack_module_enemy2(enemy, battler)
                print(f'{enemy.name} did {enemy.damage} to you. You now have {battler.hp} of health')
                time.sleep(1)
            elif result is None:
                print('You and your enemy clash insulting each other!')
                time.sleep(1)
        if battler.hp <= 0:
            print('You are dead. Try again')
            dead_deleter(playerCharacters)
            option = int(input('Continue?\n1 Yes\t0 No\n'))
            if len(playerCharacters) == 0:
                print("You don't have enough heroes to continue.")
                time.sleep(1)
                instance()
            elif option == 1:
                print('Opening character selector.')
                time.sleep(1)
                battle(char_selector(), enemy)
            else:
                print("You decided to not continue.")
                instance()
        elif enemy.hp <= 0:
            print('You won !')
            option = int(input('Do you want to kill another boss?\n1 Yes\t0 No\n'))
            if option == 1:
                print('RESUMING BATTLE!')
                time.sleep(1)
                battle(battler, enemy_creator())
            elif option == 0:
                print('Returning to menu.')
                instance()
            else:
                print('Returning to menu.')
                instance()
    except ValueError:
        print('Error. You selected none of your available characters. Try Again.')
        instance()


playerCharacters = []

instance()
