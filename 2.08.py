volume = int(input("enter volume{1-10}"))
match volume:
    case 1:
        print ("very quiet")
    case 2:
        print("quiet")
    case 3 | 4:
        print("low")
    case 5:
        print("medium")
    case 6:
        print("medium high")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9|10:
        print("max voulume")
    case _:
        print ("invalid volume")
