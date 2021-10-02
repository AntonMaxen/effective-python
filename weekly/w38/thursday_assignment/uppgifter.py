import numpy as np

string = "Has anyone really been far even as decided to use even go want to do look more like?"
numbers = range(1000)

#Få ut alla tal mellan 1-1000 som är jämnt delbara med 8 till en lista
output_one = [n for n in range(1000) if n % 8 == 0]
print(output_one)

#Få ut alla tal 1-1000 som har en 3a i sig till en lista
output_two = [n for n in range(1000) if '3' in str(n)]

#Hitta alla tal från 1-1000 vars logaritm med bas 2 är jämnt delbar med 2 (OBS! Standard log för numpy är _givetvis_ det naturliga talet e)
# output_three = [n for n in range(1000) if np.log2(n) % 2 == 0]

#Ta bort alla vokaler i en string och 
output_four = "".join([c for c in string if c not in 'aoueiy'])


#Ge tillbaks alla ord i stringen som har färre än 5 bokstäver i en lista
string = "Has anyone really been far even as decided to use even go want to do look more like?"
output_five = [w for w in string.split() if len(w) < 5]

#Var beredd att beskriva vilken output vi får i mystery_list - någons huvud ska rulla!
iterable = ["1234","12345","Aabcdef","abc","abcdeA", "30000"]
[print(i) for i in filter(lambda x: len(x) % 5 == 0, iterable)]

mystery_list = [x[0] for x in sorted(filter(lambda x: len(x) % 5 == 0, iterable), key = lambda x: x[-1])]
print(mystery_list)



