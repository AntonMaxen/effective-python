import numpy as np
import datetime
import time

import os
for k, v in os.environ.items():
    if 'env' in v.lower():
        print(f'{k}: {v}')

#Vi kan börja med att försäkra oss om att vi kan behandla funktioner som objekt

def test_function():
    print("Nuke the whales!")
    return "Don't nuke the whales."
# #Fullgod funktion som ger oss instruktioner om hur vi ska leva våra liv. Gör det vi väntar oss.
# string = test_function()
# print(string)

print('hello oscar')

print(np.ones((10, 10)))

for i in range(10):
    print(i**2)

print([i for i in range(256)])

something = input('heh')


# print(test_function)
# print(isinstance(test_function, object))
# #.. är det förstås ett objekt.

# #Detta innebär att vi kan skicka in functionen som vilket inargument som helst!

# def test_function_to_test_test_function(func):
#     #Kallar bara på funktionen här
#     func()

# test_function_to_test_test_function(test_function)


#Vi gör en wrapperfunktion!



def new_function(func):
    #Vi skickar alltså in en funktion som inargument som vi sen kallar på IGEN genom 
    #att returna vår wrapping funktion

    def wrapping_function():
        value_for_demonstration = 1337
        print("Starting wrapping function.")
        func()
        print("Ending wrapping function.")
    #print(value_for_demonstration)
    return wrapping_function #Här fortsätter vi vår resa med


#print(value_for_demonstration)
#Vi testar att definiera och skicka in en funktion till new_function

new_function(test_function)
#Vad händer här?

print([i for i in range(100)])

test_function = new_function(test_function)
test_function()
#Greppar vi allt det här är vi redo för decorators!
#Synonymt:
@new_function
def test_function():
    print("Don't nuke the whales!")

test_function()




#Mycket stulet exempel

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner


# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(10,0)
