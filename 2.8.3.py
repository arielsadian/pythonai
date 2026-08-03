minutes = int(input("how many minutes did the meal take"))
cost = int(input("how mach did it cost?"))
is_quick_service = minutes < 15
is_expensive = cost > 100
if is_quick_service and not is_expensive:
    print("recommended")
else:
    print("not recommended")