import random
from builtins import property
from tkinter import *

import settings as s


class PointAttributes:
    def __init__(self, r=None, canvas=None, color=None):
        self.r = r
        self.canvas = canvas
        self.color = color


class Point(PointAttributes):
    def __init__(self, x_coordinate, y_coordinate, r=None, canvas=None, color=None):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        super().__init__(r, canvas, color)
        if self.r is not None:
            self.create_circle()

    @property
    def x_coordinate(self):
        return self.__x_coordinate

    @property
    def y_coordinate(self):
        return self.__y_coordinate

    def create_circle(self):
        x0 = self.x_coordinate - self.r
        y0 = self.y_coordinate - self.r
        x1 = self.x_coordinate + self.r
        y1 = self.y_coordinate + self.r
        return self.canvas.create_oval(x0, y0, x1, y1, fill=self.color)


class NextPoint(PointAttributes):
    def __init__(self, old_point: Point, target_point: Point, r=None, canvas=None, color=None):
        self.__old_x_coordinate = old_point.x_coordinate
        self.__old_y_coordinate = old_point.y_coordinate
        self.__target_x_coordinate = target_point.x_coordinate
        self.__target_y_coordinate = target_point.y_coordinate
        super().__init__(r, canvas, color)

    @property
    def next_x_coordinate(self):
        return round((self.__old_x_coordinate + self.__target_x_coordinate) / 2)

    @property
    def next_y_coordinate(self):
        return round((self.__old_y_coordinate + self.__target_y_coordinate) / 2)

    @property
    def next_point_coordinates(self):
        return Point(self.next_x_coordinate, self.next_y_coordinate, self.r, self.canvas, self.color)


class Timer:
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.point = Point(x, y)
        self.canvas.pack()
        self.canvas.after(10, self.refresh_canvas)

    def create_next_point(self, target_point):
        return NextPoint(self.point, target_point, 0, self.canvas, None).next_point_coordinates

    def refresh_canvas(self):
        """ refresh the content of the canvas """
        selector = {
            1: self.create_next_point(point_1),
            2: self.create_next_point(point_2),
            3: self.create_next_point(point_3),
        }
        random_num = random.randint(1, 3)
        self.point = selector[random_num]
        print(f'x: {self.point.x_coordinate}, y: {self.point.y_coordinate}')
        self.canvas.after(10, self.refresh_canvas)


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=s.CANVAS_WIDTH, height=s.CANVAS_HEIGHT)

    point_1 = Point(s.POINT_1_X, s.POINT_1_Y, 5, canvas, 'red')
    point_2 = Point(s.POINT_2_X, s.POINT_2_Y, 5, canvas, 'green')
    point_3 = Point(s.POINT_3_X, s.POINT_3_Y, 5, canvas, 'blue')

    timer = Timer(s.START_POINT_X, s.START_POINT_Y, canvas)

    root.mainloop()
