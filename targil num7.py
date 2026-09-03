num_stud = int(input("num of student"))
min_grade = 100
i = 0
while i < num_stud:
    grade = int(input("grade"))
    if grade < min_grade:
        min_grade = grade
    i += 1
    print(min_grade)

    total_sum = 0
    number = int(input("enter number: "))
    while number != 999:
        total_sum +=number
        number = int(input("enter number"))
    print(total_sum)