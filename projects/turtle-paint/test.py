from swampy.TurtleWorld import *
print(type(World.current_world))
world = TurtleWorld()
print(type(World.current_world))
world2 = TurtleWorld()
print(World.current_world)
bob = Turtle()
bob2 = Turtle()

world.wait_for_user()
world2.wait_for_user()