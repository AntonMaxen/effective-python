import numpy as np
from typing import List
import matplotlib.pyplot as plt
from math import pi
import time

# Generellt sett: [operation(val) för val i iterable] -> [operation(val_0), operation(val_1).. operation(val_n)]
#Typ hello world för list comprehensions:
vals = [val for val in range(10)]
print(vals)

#Det går givetvis att baka in enumerate här - inte det vanligaste man ser, men det fungerar
log_values = [(i,np.log(x)) for i,x in enumerate(range(1,100))]
#print(log_values)



#Unpack tillsammans med list comprehension för att skapa objekt:
class MyCoolClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

#Generera lite tuples
list_of_tuples = [(val, val) for val in range(100)]
#Använd dessa tuples för att med unpack öppna upp varje tuple och använd dessa värden i init
list_of_objects = [MyCoolClass(*args) for args in list_of_tuples]

#Fungerar också med:
list_of_objects = [MyCoolClass(arg1, arg2) for arg1, arg2 in list_of_tuples]




#Genererar samma output, men vilken borde vara bäst?
n = 100000
trials = 15
time_elapsed = 0
# for i in range(trials):
#     start_time = time.time()
#     [val for val in range(n) if np.sin(pi*val/2) > 0]
#     end_time = time.time()
#     time_elapsed += end_time - start_time
# print(time_elapsed)

for i in range(trials):
    start_time = time.time()
    [val for val in filter(lambda x: np.sin(pi*x/2) > 0, range(n))]
    end_time = time.time()
    time_elapsed += end_time - start_time
print(time_elapsed)




