from .Canvas import Canvas
from swampy.TurtleWorld import Turtle, TurtleWorld, fd, rt


class CanvasSwampy(Canvas):

    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.world = TurtleWorld()
        self.turtle = Turtle()
        self.turtle.set_delay(0.1)

    def save(self):
        pass

    def draw_pixel(self, x, y, color):
        pass

    def draw_square(self, x, y, width, height, color):
        self.turtle.x = x
        self.turtle.y = y
        list(map(lambda s: [fd(self.turtle, s), rt(self.turtle)], [width, height, width, height]))

    def draw_poly(self, x, y, n, face_l, angle=360, color="red"):
        self.turtle.x = x
        self.turtle.y = y
        list(map(lambda i: [fd(self.turtle, face_l), rt(self.turtle, angle / n)], range(n)))
