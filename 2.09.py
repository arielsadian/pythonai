import random
def reverse_tuple(tup: tuple):
    """receives a tuple and returns a new tuple with the elements in reverse order."""
    temp_list = []
    for i in range (len(tup) - 1, -1, -1):
        temp_list.append(tup[i])
    return tuple(temp_list)
print(reverse_tuple((1,2,3,4)))
print(reverse_tuple(('a','b','c')))


def random_tuple(length: int):
    """generates a tuple of specified length containing random integers 1 and 100."""
    numbers_list = []
    for _ in range(length):
        num = random.randint(1,100)
        numbers_list.append(num)
    return tuple(numbers_list)
print(random_tuple(5))
print(random_tuple(3))
print(len(random_tuple(10)))


def flat_dict(d: dict):
   """receives a dictionary and returns a flat tuple containing each key followed by its value."""
   result = []
   for key,value in d.items():
       result.append(key)
       result.append(value)
   return tuple(result)
print(flat_dict({'a':1, 'b': 2,'c': 3}))