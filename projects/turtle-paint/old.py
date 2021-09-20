from swampy.TurtleWorld import Turtle, TurtleWorld, fd, lt, rt, wait_for_user
import random
import math
#world = TurtleWorld()
bob = Turtle()
bob.set_delay(0.00001)

circum = lambda r: 2 * math.pi * r

#square = lambda turtle, w, h: list(map(lambda s: [fd(turtle, s), rt(turtle)], [w, h, w, h]))
#poly = lambda turtle, n, face_l, a=360: list(map(lambda i: [fd(turtle, face_l), rt(turtle, a / n)], range(n)))
#circle = lambda turtle, rad: poly(turtle, 30, (circum(rad)/180) * 2)
#arc = lambda turtle, rad, angle: poly(turtle, 30, (circum(rad)/180) * 2, a=angle)

class Pen(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.x = x
        self.y = y

    def square(self, width, height):
        for length in [width, height, width, height]:
            self.fd(length)
            self.rt()

    def poly(self, num_sides, side_length, angle=360, direction='right', color='blue'):
        self.set_pen_color(color)
        turn_func = {'right': self.rt, 'left': self.lt}
        side_deg = 360 / num_sides
        turns = int(angle / side_deg)

        for i in range(turns):
            self.fd(side_length)
            turn_func[direction](side_deg)

    def circle(self, radius, num_sides=360, angle=360, direction='right', color='blue'):
        circumference = circum(radius)
        side_length = circumference / num_sides
        self.poly(num_sides, side_length, angle=angle, direction=direction, color=color)


def get_cathetus(v, length):
    v = math.radians(v)
    x = math.cos(v) * length
    y = math.sin(v) * length
    return x, y


def get_velocity(deg, length):
    deg = deg % 360
    if 0 <= deg <= 90:
        v_x, v_y = get_cathetus(deg, length)
    elif 90 < deg <= 180:
        v_x, v_y = get_cathetus(180 - deg, length)
        v_x = -v_x
    elif 180 < deg <= 270:
        v_x, v_y = get_cathetus(deg - 180, length)
        v_x, v_y = -v_x, -v_y
    elif 270 < deg < 360:
        v_x, v_y = get_cathetus(360 - deg, length)
        v_y = -v_y
    else:
        raise ValueError

    return v_x, v_y


def calc_location(x, y, heading, num_sides, side_length, angle=360, direction='right'):
    side_deg = 360 / num_sides
    turns = int(angle / side_deg)
    side_deg = -side_deg if direction == 'right' else side_deg
    print(direction, side_deg)

    for i in range(turns):
        v_x, v_y = get_velocity(heading, side_length)
        x += v_x
        y += v_y
        heading += side_deg

    return x, y, heading


def circle(turtle, radius, num_sides=360, angle=360, direction='right', color='blue'):
    pass


def plot():
    plot = lambda turtle, func, steps, siz: list(map(lambda x: [fd(turtle, siz), lt(turtle), fd(turtle, func(x)), rt(turtle)],range(steps)))

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


def random_jibberish():
    size = 200

    while True:
        num_sides = random.randint(3, 30)
        num_sides = 5
        side_length = random.randint(1, size // 2)
        direction = random.choice(['right', 'left'])
        # direction = 'left'
        angle = random.randint(1, 360)
        color = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
        color = 'blue'

        x, y, heading = calc_location(bob.x, bob.y, bob.heading, num_sides, side_length, angle=angle, direction=direction)
        print(x, y, heading)
        if -size < x < size and -size < y < size:
            poly(bob, num_sides, side_length, angle=angle, direction=direction, color=color)
            print(bob.x, bob.y, bob.heading)


def remove_this(turtle, colors=None, rotations=1000, radius=100, num_sides=6):
    if colors is None:
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    for i in range(rotations):
        color = colors[num_sides % len(colors)]
        circle(turtle, radius, num_sides=num_sides, angle=90, color=color)
        bob.heading = (bob.heading - 180) % 360
        if i + 1 >= num_sides * 2:
            num_sides += 1


def arcygon(turtle, radius, num_sides=4, angle=90, color='blue'):
    for _ in range(num_sides * 2):
        circle(turtle, radius, num_sides=num_sides, angle=angle, color=color)
        turtle.heading = (turtle.heading - 180) % 360


def dunno_shape(turtle, radius=100, rotations=1000, num_sides=6, colors=None):
    if colors is None:
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    for i in range(rotations):
        color = colors[num_sides % len(colors)]
        circle(turtle, radius, num_sides=num_sides, angle=90, color=color)
        turtle.heading = (turtle.heading - 180) % 360
        if i % 2 != 0:
            num_sides += 1


def corona_ball(turtle, rad=100, colors=None):
    if colors is None:
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    for num_sides in range(100, 1000):
        color = colors[num_sides % len(colors)]
        arcygon(turtle, rad, num_sides, color=color)
        num_sides += 1


#arcygon(bob, 100, 6)
RADIUS = 200
bob.heading = 90
bob.y -= RADIUS
corona_ball(bob, rad=RADIUS)

wait_for_user()
