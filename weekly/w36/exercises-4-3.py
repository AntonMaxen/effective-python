from swampy.TurtleWorld import *
import math


def orient(t):
    deg = t.get_heading()
    deg = deg % 360
    t.rt(((360 - deg) % 360))


def square(t, side_length):
    orient(t)
    for _ in range(4):
        t.fd(side_length)
        t.rt(90)


def polygon(t, side_length, deg, angle=360):
    orient(t)
    turns = int(360 / deg)
    for i in range(turns):
        if i * deg > angle:
            t.pu()

        t.fd(side_length)
        t.rt(deg)


def circle(t, r, angle=360):
    orient(t)
    circumference = 2 * math.pi * r
    side_len = circumference / 360
    polygon(t, side_len, 1, angle=angle)


def main():
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.01
    circle(bob, 10, 280)

    wait_for_user()


if __name__ == '__main__':
    main()
