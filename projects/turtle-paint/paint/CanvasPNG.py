from .Canvas import Canvas
from PIL import Image


class CanvasPNG(Canvas):

    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.image = Image.new('RGB', (self.width, self.height))

    def save(self):
        self.image.save('image.png')

    def draw_pixel(self, x, y, color):
        self.image.putpixel((x, y), color)

    def draw_square(self, x, y, width, height, color):
        pen_x = x
        pen_y = y

        for i in range(width):
            self.draw_pixel(x + i, pen_y, color)
            pen_x = i

        for i in range(height):
            self.draw_pixel(x + pen_x, y + i, color)
            pen_y = i

        for i in range(width):
            self.draw_pixel(x + (width - i), y + pen_y, color)
            pen_x = i

        for i in range(height):
            self.draw_pixel(x, y + (height-i), color)
            pen_y = i


    def draw_poly(self, x, y, n, face_l, angle=360, color="red"):
        pass
