colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def arcygon(turtle, radius, num_sides=4, angle=90, color='blue'):
    for i in range(num_sides * 2):
        circle(bob, radius, num_sides=num_sides, angle=angle, color=color)
        turtle.heading = (turtle.heading - 180) % 360


rad = 100

for num_sides in range(6, 1000):
    color = colors[num_sides % len(colors)]
    arcygon(bob, rad, num_sides, color=color)
    num_sides += 1


arcygon(bob, 100, 6)
