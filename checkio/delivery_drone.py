import time


class Package:
    def __init__(self, position):
        self.position = position
        self.map_position = None


class Map:
    def __init__(self, map_len):
        self.map: list = [[]] * map_len

    def add_package(self, package: Package, position: int):
        if not self.map[position]:
            self.map[position] = []
        self.map[position].append(package)
        package.map_position = position

    def del_packege(self, package: Package, position: int):
        self.map[position].remove(package)

    def is_valid(self):
        return all([all([pack.position == i for pack in packs]) for i, packs in enumerate(self.map)])

    def get_far_package(self):
        for i, packs in enumerate(self.map[::-1]):
            if packs and any([pack.position != len(self.map) - i - 1 for pack in packs]):
                return len(self.map) - i - 1
        return 0

    def has_package(self, position):
        if any([pack.position != position for pack in self.map[position]]):
            return True
        return False

    def give_package(self, position):
        return max([(x, x.position - position) for x in self.map[position] if x.position != position], key=lambda x: x[1])[0]

    def check_distance(self, position):
        return max([(x, x.position - position) for x in self.map[position]], key=lambda x: x[1])[1]

    def __str__(self):
        result = ""
        max_packages = max([len(x) for x in self.map])
        for packages_level in range(max_packages - 1, -1, -1):
            result += "|"
            if packages_level:
                for i in range(len(self.map)):
                    if self.map[i] and packages_level < len(self.map[i]):
                        result += f"\033[4m|{self.map[i][packages_level].position:^3}|\033[0m|"
                    else:
                        result += "     |"
            else:
                for i in range(len(self.map)):
                    if self.map[i]:
                        result += f"\033[4m|{self.map[i][0].position:^3}|\033[0m|"
                    else:
                        result += "_____|"
            result += "\n"
        result += "\033[4m|" + "".join([f"{str(x):^5}|" for x in range(len(self.map))]) + "\033[0m\n"
        return result


class Drone:
    def __init__(self, map: Map):
        self.map = map
        self.position = 0
        self.package = None
        self.moves = 0

    def move_left(self):
        self.position -= 1
        self.moves += 1

    def move_right(self):
        self.position += 1
        self.moves += 1

    def get_package(self, package: Package):
        if not self.package:
            self.package = package
            self.map.del_packege(package, self.position)

    def drop_package(self):
        # self.package.position = self.position
        self.map.add_package(self.package, self.position)
        self.package = None

    def run_drone(self):
        while not self.map.is_valid():
            if self.package:
                if self.map.has_package(self.position):
                    if self.package.position > self.position:
                        if self.map.check_distance(self.position) > self.position - self.package.position:
                            self.drop_package()
                            self.get_package(self.map.give_package(self.position))
                    elif self.package.position < self.position:
                        if self.map.check_distance(self.position) < self.position - self.package.position:
                            self.drop_package()
                            self.get_package(self.map.give_package(self.position))
                if self.package.position < self.position:
                    self.move_left()
                elif self.package.position > self.position:
                    self.move_right()
                else:
                    self.drop_package()
                time.sleep(0.3)
                print(self)
            else:
                if self.map.has_package(self.position) and self.map.check_distance(self.position) > 0:
                    self.get_package(self.map.give_package(self.position))
                else:
                    target = self.map.get_far_package()
                    if target > self.position:
                        self.move_right()
                    elif target < self.position:
                        self.move_left()
                    else:
                        self.get_package(self.map.give_package(self.position))
                time.sleep(0.3)
                print(self)
        while self.package:
            if self.package:
                if self.package.position < self.position:
                    self.move_left()
                elif self.package.position > self.position:
                    self.move_right()
                else:
                    self.drop_package()
            time.sleep(0.3)
            print(self)
        while self.position != 0:
            self.move_left()
            time.sleep(0.3)
            print(self)

    def __str__(self):
        result = "\n\n"
        result += " " + "      " * self.position + "T___T \n"
        if self.package:
            result += " " + "      " * self.position + f"|\033[4m{self.package.position:^3}\033[0m|\n"
        result += "\n" + str(self.map)
        return result


# map = Map(11)
# drone = Drone(map)
# print(drone)
#
# drone.run_drone()
# package_8 = Package(9)
# map.add_package(package_8, 4)
# package_10 = Package(2)
# map.add_package(package_10, 6)
# package_11 = Package(10)
# map.add_package(package_11, 4)
# print(drone)
# drone.run_drone()
# print(drone.moves)


def delivery_drone(orders) -> int:
    map = Map(len(orders))

    for i, order in enumerate(orders):
        if order:
            package = Package(order)
            map.add_package(package, i)

    drone = Drone(map)
    print(drone)
    drone.run_drone()
    print(drone.moves)
    return drone.moves


# # assert delivery_drone([0, 1, 0]) == 0
# assert delivery_drone([0, 2, 0, 3]) == 4
# delivery_drone([0, 2, 0, 3])
delivery_drone([0,2,17,0,2,0,2,3,0,0,0,6,23,0,0,0,19,0,0,0,15,20,0,0,16,0,0])