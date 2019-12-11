class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2):
    attack, defence = unit_1, unit_2
    while unit_1.is_alive and unit_2.is_alive:
        defence.health -= attack.attack
        attack, defence = defence, attack
    return unit_1.is_alive

class Army():
    def __init__(self):
        self.army = []

    def add_units(self, type_of_unit, count):
        self.army.extend([type_of_unit() for i in range(count)])
    # def add_units(self, *args):
    #     self.army.extend([*args])

class Battle():
    def fight(self, army1, army2):
        while army1.army and army2.army:
            if fight(army1.army[-1], army2.army[-1]):
                army2.army.pop()
            else:
                army1.army.pop()
        return len(army2.army) == 0
        # if army1.army:
        #     return True
        # return False




if __name__ == '__main__':

    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    battle = Battle()

    print(battle.fight(my_army, enemy_army)) # == True

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    print(battle.fight(army_3, army_4))# == False


"""Very good solution! But Python take O(n) time to remove the first element from the list, so it’s better to remove element from the end"""

# class Warrior:
#     """Define a warrior."""
#
#     def __init__(self):
#         self.health = 50
#         self.attack = 5
#
#     @property
#     def is_alive(self) -> bool:
#         return self.health > 0
#
#
# class Knight(Warrior):
#     """Define a knight, it's a warrior with an increased attack of 7."""
#
#     def __init__(self):
#         super().__init__()
#         self.attack = 7
#
#
# def fight(unit_1, unit_2) -> bool:
#     """Duel fight...
#     Is unit_1 stronger than unit_2?"""
#     while unit_1.is_alive and unit_2.is_alive:
#         unit_2.health -= unit_1.attack
#         unit_1.health -= unit_2.attack if unit_2.is_alive else 0
#     return unit_1.is_alive
#
#
# class Army:
#     """Define an army."""
#
#     def __init__(self):
#         """An empty army for start."""
#         self.list = []
#
#     def add_units(self, unit, amount_of_units):
#         """Add an amount of specific units to the army."""
#         self.list += [unit() for k in range(amount_of_units)]
#
#     @property
#     def is_alive(self) -> bool:
#         """Does the army have a living warrior?"""
#         return self.list != []
#
#     @property
#     def warrior(self):
#         """First warrior alive of the army."""
#         return self.list[0]
#
#     @property
#     def pop(self):
#         """Pop a dead warrior out of the list."""
#         self.list.pop(0)
#
#
# class Battle:
#     def fight(self, army_1, army_2) -> bool:
#         while army_1.is_alive and army_2.is_alive:
#             if fight(army_1.warrior, army_2.warrior):
#                 army_2.pop
#             else:
#                 army_1.pop
#         return army_1.is_alive