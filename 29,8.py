# 1. circle_area
def circle_area(radius):
    """
    Calculates the area of a circle based on given radius.

    :param radius: The radius of the circle (int or float)
    :return: Calculated area of the circle (float)
    """
    return 3.14 * (radius ** 2)


# 2. is_adult
def is_adult(age=0):
    """
    Checks if a person is an adult based on their age.

    :param age: Age of the person, defaults to 0 (int or float)
    :return: True if age is 18 or above, False otherwise (bool)
    """
    return age >= 18


# --- Tests ---
print(circle_area(1))
print(circle_area(2.5))
print(circle_area(radius=10))

print(is_adult())
print(is_adult(17))
print(is_adult(18))
print(is_adult(age=40))
#3 apply_discount
def apply_discount(price,percent=10):
    """calculates the final price after applying a percentage discount.
    :param price: original price of the item (int or float)
     :param percent: discount percentage,defaults to 10 (int or float)
     :return: price after discount (float)
     """
    return price * (1 - percent /100)
#4 count_vowels
def count_vowels(text):
    """counts the number of english vowels in a string.
    :param text: input string to search for vowels (str)
    :return: total number of vowels found (int)
    """
    vowels = 'aeiou'
    count = 0
    for char in text:
        if char.lower() in vowels:
                count +=1
    return count
#---calls and test___
print(apply_discount(200))
print(apply_discount(200, 25))
print(apply_discount(200,percent=50))
print(apply_discount(price=80,percent=5))
print(count_vowels('incognito))'))
print(count_vowels('missiiiissippi'))
print(count_vowels('xyz'))