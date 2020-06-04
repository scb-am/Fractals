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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    print(fight(chuck, bruce))# == True
    print(fight(dave, carl))# == False
    print(fight(carl, mark))# == False
