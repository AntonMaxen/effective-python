from paint import get_canvas
import time

WIDTH = 640
HEIGHT = 480

canvas = get_canvas("swampy", width=WIDTH, height=HEIGHT)


canvas.draw_square(120, 120, 100, 100, (255, 0, 0))
canvas.save()

time.sleep(3)

# canvas.draw_circle(0, 0, 50, "red")
# canvas.draw_arc(0, 0, 100, 180, "red")
