price = {'apple':12,'banana':7,'cherry':15}
print(price)
key = input("which fruit?")
try:
    print(price[key])
except KeyError:
    print(f"{key} not exist")
print("goodbye")
  #targil 2

t = (1,2,3)
try:
    t[0] = 99
except TypeError:
    print("cannot change a tuple")
    print(t)
    print("goodbye")
# targil 3

fruits = ["apple","banana"]
try:
    fruits.remove("orange")
except ValueError:
    print("orange is not in the list")
    print(fruits)
    print("goodbye")