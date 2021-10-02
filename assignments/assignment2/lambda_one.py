greater_then = lambda arr, num: filter(lambda x: x > num, arr) 


my_list = [60, 91, 38, 13, 18, 34, 15, 74] 


print(list(greater_then(my_list, 37)))
