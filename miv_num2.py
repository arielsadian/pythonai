
def special_percentile(percent:int,numbers: list):
    numbers.sort()
    index = int((percent / 100) * len(numbers))
    return float(numbers[index])
print(special_percentile(25,[40,10,30,20]))