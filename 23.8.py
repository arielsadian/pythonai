grades = {}

grades['math'] = int(input('math grade:'))
grades['english'] =int(input('english grade:'))
grades['literature'] = int(input('literature grade:'))
grades['python'] = int(input('python grade:'))
score = list(grades.values())
grades['avg'] = sum(score)/len(score)
grades['max'] = max(score)
grades['min'] = min(score)
del grades['literature']

print(grades)