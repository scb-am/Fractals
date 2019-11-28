import random
from builtins import property
from tkinter import *

import settings as s


class FractalsApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.__run_app()

    def __run_app(self):
        self.canvas = Canvas(self, width=s.CANVAS_WIDTH, height=s.CANVAS_HEIGHT, bg="white", cursor="cross")
        self.__point_number = 0
        self.__color_selector = {
            1: 'red',
            2: 'green',
            3: 'blue',
        }
        self.__point_list = []
        self.button_clear = Button(self, text="Clear", command=self.__clear_all)
        self.button_clear.pack(side="bottom", fill="both", expand=True)
        self.button_pause = Button(self, text="Pause", command=self.__pause)
        self.button_pause.pack(side="bottom", fill="both", expand=True)
        self.button_play = Button(self, text="Play", command=self.__play)
        self.button_play.pack(side="bottom", fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.__create_point)
        self.canvas.pack()

    def __clear_all(self):
        self.canvas.delete("all")

    def __pause(self):
        self.timer.pause()

    def __play(self):
        self.timer.play()

    def __create_point(self, event):
        self.__point_number += 1
        if self.__point_number <= 3:
            self.__point_list.append(Point(event.x, event.y, 5, self.canvas, self.__color_selector[self.__point_number]))
        else:
            self.__start_point_x, self.__start_point_y = event.x, event.y
            Point(self.__start_point_x, self.__start_point_y, 0, self.canvas, None)
            self.__run_timer()

    def __run_timer(self):
        self.point1, self.point2, self.point3 = self.__point_list
        self.timer = Timer(self.__start_point_x, self.__start_point_y, self.canvas, point_1=self.point1,
                           point_2=self.point2, point_3=self.point3)
        self.timer.run()


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
    def __init__(self, x, y, canvas, **kwargs):
        self.__dict__.update(kwargs)
        self.delay = 10
        self.x = x
        self.y = y
        self.canvas = canvas

    def run(self):
        self.point = Point(self.x, self.y)
        self.canvas.pack()
        self.canvas.after(self.delay, self.refresh_canvas)

    def pause(self):
        self.delay = 10000000000

    def play(self):
        self.delay = 10
        self.refresh_canvas()

    def create_next_point(self, target_point):
        return NextPoint(self.point, target_point, 0, self.canvas, None).next_point_coordinates

    def refresh_canvas(self):
        """ refresh the content of the canvas """
        selector = {
            1: self.create_next_point(self.point_1),
            2: self.create_next_point(self.point_2),
            3: self.create_next_point(self.point_3),
        }
        random_num = random.randint(1, 3)
        self.point = selector[random_num]
        print(f'x: {self.point.x_coordinate}, y: {self.point.y_coordinate}')
        self.canvas.after(self.delay, self.refresh_canvas)


if __name__ == '__main__':
    app = FractalsApp()
    app.mainloop()
