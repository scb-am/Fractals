import math


class Point():
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


class Room():
    def __init__(self, point1_x_coordinate: int, point1_y_coordinate: int,
                 point2_x_coordinate: int, point2_y_coordinate: int):
        self.point1_x_coordinate = point1_x_coordinate
        self.point1_y_coordinate = point1_y_coordinate
        self.point2_x_coordinate = point2_x_coordinate
        self.point2_y_coordinate = point2_y_coordinate


class Sensor():
    def __init__(self, center: Point, radius: int):
        self.x_coordinate = center.x_coordinate
        self.y_coordinate = center.y_coordinate
        self.radius = radius


class Cross_point(Point):
    def __init__(self, x_coordinate: int, y_coordinate: int, sensors: list):
        super().__init__(x_coordinate, y_coordinate)
        self.sensors = sensors


class Cross_circles_points():
    def __init__(self, sensor_1: Sensor, sensor_2: Sensor):
        self.__sensor_1 = sensor_1
        self.__sensor_2 = sensor_2
        self.__sensor_1_x = sensor_1.x_coordinate
        self.__sensor_1_y = sensor_1.y_coordinate
        self.__sensor_1_radius = sensor_1.radius
        self.__sensor_2_x = sensor_2.x_coordinate
        self.__sensor_2_y = sensor_2.y_coordinate
        self.__sensor_2_radius = sensor_2.radius

    @property
    def distance_between_centers(self):
        return math.sqrt((self.__sensor_1_x - self.__sensor_2_x) ** 2 \
                         + (self.__sensor_1_y - self.__sensor_2_y) ** 2)

    @property
    def distance_sensor_1_point_O(self):
        return (self.__sensor_2_radius ** 2 - self.__sensor_1_radius ** 2 \
                + self.distance_between_centers ** 2) / (2 * self.distance_between_centers)

    @property
    def distance_sensor_2_point_O(self):
        return self.distance_between_centers - self.distance_sensor_1_point_O

    @property
    def point_O_x_coordinate(self):
        return self.__sensor_1_x + self.distance_sensor_2_point_O / self.distance_between_centers * \
               (self.__sensor_2_x - self.__sensor_1_x)

    @property
    def point_O_y_coordinate(self):
        return self.__sensor_1_y + self.distance_sensor_2_point_O / self.distance_between_centers * \
               (self.__sensor_2_y - self.__sensor_1_y)

    @property
    def distance_between_cross_points(self):
        return math.sqrt(self.__sensor_1_radius ** 2 - self.distance_sensor_2_point_O ** 2)

    @property
    def calculate(self):
        if self.distance_between_centers < self.__sensor_1_radius + self.__sensor_2_radius and \
                self.distance_between_centers > math.fabs(self.__sensor_1_radius - self.__sensor_2_radius):
            cross_point_1_x = self.point_O_x_coordinate + (self.__sensor_2_y - self.__sensor_1_y) / \
                              self.distance_between_centers * self.distance_between_cross_points
            cross_point_1_y = self.point_O_y_coordinate - (self.__sensor_2_x - self.__sensor_1_x) / \
                              self.distance_between_centers * self.distance_between_cross_points
            cross_point_1 = Cross_point(cross_point_1_x, cross_point_1_y, [self.__sensor_1, self.__sensor_2])
            cross_point_2_x = self.point_O_x_coordinate - (self.__sensor_2_y - self.__sensor_1_y) / \
                              self.distance_between_centers * self.distance_between_cross_points
            cross_point_2_y = self.point_O_y_coordinate + (self.__sensor_2_x - self.__sensor_1_x) / \
                              self.distance_between_centers * self.distance_between_cross_points
            cross_point_2 = Cross_point(cross_point_2_x, cross_point_2_y, [self.__sensor_1, self.__sensor_2])
            return cross_point_1, cross_point_2
        else:
            return None


class Cross_circle_vs_lines_points():
    def __init__(self, sensor: Sensor, room: Room):
        self.__sensor = sensor
        self.__sensor_x = sensor.x_coordinate
        self.__sensor_y = sensor.y_coordinate
        self.__sensor_radius = sensor.radius
        self.__point1_x_coordinate = room.point1_x_coordinate
        self.__point1_y_coordinate = room.point1_y_coordinate
        self.__point2_x_coordinate = room.point2_x_coordinate
        self.__point2_y_coordinate = room.point2_y_coordinate
        self.__points = []

    def calculate_cross_point_coordinates(self, sensor_axis_1_arg, sensor_axis_2_arg, room_axis_arg):
        cross_point_1_axis_coordinate = (2 * sensor_axis_1_arg + math.sqrt(4 * (self.__sensor_radius ** 2) - 4 * \
                                                                           ((room_axis_arg - \
                                                                             sensor_axis_2_arg) ** 2))) / 2
        cross_point_2_axis_coordinate = (2 * sensor_axis_1_arg - math.sqrt(4 * (self.__sensor_radius ** 2) - 4 * \
                                                                           ((room_axis_arg - \
                                                                             sensor_axis_2_arg) ** 2))) / 2
        return cross_point_1_axis_coordinate, cross_point_2_axis_coordinate

    def create_cross_points(self, point: Point):
        return Cross_point(point.x_coordinate, point.y_coordinate, self.__sensor)

    def calculate(self):
        if self.__sensor_x + self.__sensor_radius > self.__point1_x_coordinate and \
                self.__sensor_x - self.__sensor_radius < self.__point1_x_coordinate:
            cross_point_1_x = cross_point_2_x = self.__point1_x_coordinate
            cross_point_1_y, cross_point_2_y = self.calculate_cross_point_coordinates(self.__sensor_y,
                                                                                      self.__sensor_x,
                                                                                      self.__point1_x_coordinate)
            self.__points.extend([Point(cross_point_1_x, cross_point_1_y), Point(cross_point_2_x, cross_point_2_y)])

        if self.__sensor_x + self.__sensor_radius > self.__point2_x_coordinate and \
                self.__sensor_x - self.__sensor_radius < self.__point2_x_coordinate:
            cross_point_1_x = cross_point_2_x = self.__point2_x_coordinate
            cross_point_1_y, cross_point_2_y = self.calculate_cross_point_coordinates(self.__sensor_y,
                                                                                      self.__sensor_x,
                                                                                      self.__point2_x_coordinate)
            self.__points.extend([Point(cross_point_1_x, cross_point_1_y), Point(cross_point_2_x, cross_point_2_y)])

        if self.__sensor_y + self.__sensor_radius > self.__point1_y_coordinate and \
                self.__sensor_y - self.__sensor_radius < self.__point1_y_coordinate:
            cross_point_1_y = cross_point_2_y = self.__point1_y_coordinate
            cross_point_1_x, cross_point_2_x = self.calculate_cross_point_coordinates(self.__sensor_x,
                                                                                      self.__sensor_y,
                                                                                      self.__point1_y_coordinate)
            self.__points.extend([Point(cross_point_1_x, cross_point_1_y), Point(cross_point_2_x, cross_point_2_y)])

        if self.__sensor_y + self.__sensor_radius > self.__point2_y_coordinate and \
                self.__sensor_y - self.__sensor_radius < self.__point2_y_coordinate:
            cross_point_1_y = cross_point_2_y = self.__point2_y_coordinate
            cross_point_1_x, cross_point_2_x = self.calculate_cross_point_coordinates(self.__sensor_x,
                                                                                      self.__sensor_y,
                                                                                      self.__point2_y_coordinate)
            self.__points.extend([Point(cross_point_1_x, cross_point_1_y), Point(cross_point_2_x, cross_point_2_y)])

        if len(self.__points) > 0:
            return [self.create_cross_points(point) for point in self.__points]
        else:
            return None


def check_cross_point(room, cross_point):
    if room.point1_x_coordinate <= cross_point.x_coordinate <= room.point2_x_coordinate and \
        room.point1_y_coordinate <= cross_point.y_coordinate <= room.point2_y_coordinate:
        return cross_point

def check_is_cross_point_in_sensor(cross_point, sensor):
    distance = math.sqrt((cross_point.x_coordinate - sensor.x_coordinate) ** 2 + \
                        (cross_point.y_coordinate - sensor.y_coordinate) ** 2)
    if distance <= sensor.radius:
        return True
    else:
        return False

def check_is_point_in_sensor(x_coordinate, y_coordinate, sensor):
    distance = math.sqrt((x_coordinate - sensor.x_coordinate) ** 2 + (y_coordinate - sensor.y_coordinate) ** 2)
    if distance <= sensor.radius:
        return True
    else:
        return False

def is_covered(room, sensors):
    room = Room(0, 0, room[0], room[1])
    sensors = {Sensor(Point(sensor[0], sensor[1]), sensor[2]) for sensor in sensors}
    cross_points_set = set()
    for sensor_1 in sensors:
        if Cross_circle_vs_lines_points(sensor_1, room).calculate():
            cross_points_set.update(Cross_circle_vs_lines_points(sensor_1, room).calculate())
        for sensor_2 in sensors:
            if Cross_circles_points(sensor_1, sensor_2).calculate:
                cross_points_set.update(Cross_circles_points(sensor_1, sensor_2).calculate)
    valid_cross_points_set = {check_cross_point(room, cross_point) for cross_point in cross_points_set}
    valid_cross_points_set.discard(None)

    cross_points_validation_list = []
    for cross_point in valid_cross_points_set:
        sensors_to_check = sensors.copy()
        if type(cross_point.sensors) == Sensor:
            sensors_to_check.discard(cross_point.sensors)
        else:
            for sensor in cross_point.sensors:
                sensors_to_check.discard(sensor)
        cross_point_valid = False
        for sensor_to_check in sensors_to_check:
            if check_is_cross_point_in_sensor(cross_point, sensor_to_check):
                cross_point_valid = True
        cross_points_validation_list.append(cross_point_valid)
    if all(cross_points_validation_list) and len(cross_points_validation_list) > 0:
        return True
    else:
        room_covered = False
        for sensor in sensors:
            if check_is_point_in_sensor(room.point1_x_coordinate, room.point1_y_coordinate, sensor) and \
                check_is_point_in_sensor(room.point1_x_coordinate, room.point2_y_coordinate, sensor) and \
                check_is_point_in_sensor(room.point2_x_coordinate, room.point1_y_coordinate, sensor) and \
                check_is_point_in_sensor(room.point2_x_coordinate, room.point2_y_coordinate, sensor):
                room_covered = True
        if room_covered:
            return True
        else:
            return False


print(is_covered([200, 150], [[100, 75, 10]]))   #False
print(is_covered([200, 150], [[100, 75, 10], [100, 75, 130]]))   #True
print(is_covered([200, 150], [[100, 75, 130]]))   #True
print(is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]))   #True
print(is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]))   #False

