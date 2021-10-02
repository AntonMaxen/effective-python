# Write a function that takes in a list of strings and returns every character in those strings

listring = lambda strings: [list(string) for string in strings]

listr = ['apple', 'pear', 'banana', 'cherry']

print(listring(listr))
