from abc import ABC, abstractmethod


class Army(ABC):
    @property
    @abstractmethod
    def army_name(self):
        pass

    @property
    @abstractmethod
    def swordsman_name(self):
        pass

    @property
    @abstractmethod
    def lancer_name(self):
        pass

    @property
    @abstractmethod
    def archer_name(self):
        pass

    @abstractmethod
    def train_swordsman(self):
        pass

    @abstractmethod
    def train_lancer(self):
        pass

    @abstractmethod
    def train_archer(self):
        pass


class Swordsman:
    def __init__(self, unit_name, unit_type, army_type):
        self.unit_name = unit_name
        self.unit_type = unit_type
        self.army_type = army_type

    def introduce(self):
        return f"{self.unit_type} {self.unit_name}, {self.army_type} swordsman"


class Lancer:
    def __init__(self, unit_name, unit_type, army_type):
        self.unit_name = unit_name
        self.unit_type = unit_type
        self.army_type = army_type

    def introduce(self):
        return f"{self.unit_type} {self.unit_name}, {self.army_type} lancer"


class Archer:
    def __init__(self, unit_name, unit_type, army_type):
        self.unit_name = unit_name
        self.unit_type = unit_type
        self.army_type = army_type

    def introduce(self):
        return f"{self.unit_type} {self.unit_name}, {self.army_type} archer"


class AsianArmy(Army):
    army_name = "Asian"
    swordsman_name = "Samurai"
    lancer_name = "Ronin"
    archer_name = "Shinobi"

    def train_swordsman(self, unit_name: str):
        return Swordsman(unit_name, self.swordsman_name, self.army_name)

    def train_lancer(self, unit_name: str):
        return Lancer(unit_name, self.lancer_name, self.army_name)

    def train_archer(self, unit_name: str):
        return Archer(unit_name, self.archer_name, self.army_name)


class EuropeanArmy(Army):
    army_name = "European"
    swordsman_name = "Knight"
    lancer_name = "Raubritter"
    archer_name = "Ranger"

    def train_swordsman(self, unit_name: str):
        return Swordsman(unit_name, self.swordsman_name, self.army_name)

    def train_lancer(self, unit_name: str):
        return Lancer(unit_name, self.lancer_name, self.army_name)

    def train_archer(self, unit_name: str):
        return Archer(unit_name, self.archer_name, self.army_name)


"""
Swordsman = Lancer = Archer = None

class Soldier:
    def __init__(self, a, t, n):
        self.introduce = lambda: f'{getattr(a, t)} {n}, {a.__name__[:-4]} {t}'
        
class Army:
    def __getattr__(self, item):
        return lambda name: Soldier(self.__class__, item[6:], name)

class EuropeanArmy(Army):
    swordsman, lancer, archer = 'Knight Raubritter Ranger'.split()

class AsianArmy(Army):
    swordsman, lancer, archer = 'Samurai Ronin Shinobi'.split()
"""


"""
class Army:
    def train_swordsman(army, name): return Swordsman(army, name)
    def train_lancer(army, name): return Lancer(army, name)
    def train_archer(army, name): return Archer(army, name)
    
class Soldier:
    def __init__(soldier, army, name):
        soldier.descent, soldier.name = army.descent, name
        soldier.title = getattr(army, soldier.category)

    def introduce(self):
        return f'{self.title} {self.name}, {self.descent} {self.category}'

class Swordsman(Soldier): category = 'swordsman'
class Lancer(Soldier): category = 'lancer'
class Archer(Soldier): category = 'archer'

class AsianArmy(Army):
    descent = 'Asian'
    swordsman, lancer, archer = 'Samurai', 'Ronin', 'Shinobi'

class EuropeanArmy(Army):
    descent = 'European'
    swordsman, lancer, archer = 'Knight', 'Raubritter', 'Ranger'
"""


"""
class Soldier:
    def __init__(self, units, name, army):
        self.units = units
        self.name = name
        self.army = army

    def introduce(self):
        info = self.units[self._type], self.name, self.army, self._type
        return "%s %s, %s %s" % info


class Swordsman(Soldier):
    _type = 'swordsman'


class Lancer(Soldier):
    _type = 'lancer'


class Archer(Soldier):
    _type = 'archer'


class Army:
    def train_swordsman(self, name):
        return Swordsman(self.units, name, self.army)

    def train_lancer(self, name):
        return Lancer(self.units, name, self.army)

    def train_archer(self, name):
        return Archer(self.units, name, self.army)


class EuropeanArmy(Army):
    army = 'European'
    units = {'swordsman': 'Knight', 'lancer': 'Raubritter', 'archer': 'Ranger'}


class AsianArmy(Army):
    army = 'Asian'
    units = {'swordsman': 'Samurai', 'lancer': 'Ronin', 'archer': 'Shinobi'}
"""


"""
from dataclasses import dataclass

@dataclass
class Soldier:
    soldier_type: str
    name: str
    army_type: str
    specialization: str

    def introduce(self):
        return f"{self.soldier_type} {self.name}, {self.army_type} {self.specialization}"

Swordsman = Lancer = Archer = None

class Army:
    def __getattr__(self, method_name):
        train, unit_type = method_name.split("_")
        return lambda name: Soldier(type(self).soldier_type[unit_type], name, type(self).army_type, unit_type)


class AsianArmy(Army):
    army_type = "Asian"
    soldier_type = {"swordsman": "Samurai", "lancer": "Ronin", "archer": "Shinobi"}


class EuropeanArmy(Army):
    army_type = "European"
    soldier_type = {"swordsman": "Knight", "lancer": "Raubritter", "archer": "Ranger"}
"""


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"


"""
def class_factory(food_name, drink_name):
    class T:
        def __init__(self):
            self.food = self.drink = 0

        def add_food(self, food_amount, food_price):
            self.food += food_amount * food_price

        def add_drink(self, drink_amount, drink_price):
            self.drink += drink_amount * drink_price

        def total(self):
            return f'{food_name}: {self.food}, {drink_name}: {self.drink}, Total: {self.food + self.drink}'

    return T


JapaneseCook = class_factory('Sushi', 'Tea')
RussianCook = class_factory('Dumplings', 'Compote')
ItalianCook = class_factory('Pizza', 'Juice')

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())


    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_drink(5, 20)

    assert client_1.total() == "Sushi: 60, Tea: 20, Total: 80"
    assert client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"
    print("Coding complete? Let's try tests!")
"""


# TEMPLATE_CLASS = """class %sCook:
#   def __init__(s): s.f = s.d = 0
#   def add_food(s, a, p): s.f += a*p
#   def add_drink(s, a, p): s.d += a*p
#   def total(s): return '%s: '+str(s.f)+', %s: '+str(s.d)+', Total: '+str(s.f+s.d)"""
# for c in 'Japanese,Sushi,Tea Russian,Dumplings,Compote Italian,Pizza,Juice'.split():
#     exec(TEMPLATE_CLASS % tuple(c.split(',')))