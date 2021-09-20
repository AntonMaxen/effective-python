from .utils import circum
from abc import ABC, abstractmethod


class Canvas(ABC):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def draw_pixel(self, x, y, color):
        pass

    @abstractmethod
    def draw_square(self, x, y, width, height, color):
        pass

    @abstractmethod
    def draw_poly(self, x, y, face_l, angle=360):
        pass

    @abstractmethod
    def save(self):
        pass

    def draw_circle(self, x, y, radius):
        self.draw_poly(x, y, 30, (circum(radius)/180) * 2, 360)

    def draw_arc(self, x, y, radius, angle):
        self.draw_poly(x, y, 30, (circum(radius)/180) * 2, angle)
