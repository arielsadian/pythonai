#start
number =int(input("please enter a number"))
if number < 10 or number > 99:
    print("number should be between 10-99")
else:
     tens = number//10
     ones = number %10
     if tens==ones:
         print("tens equal ones")
     else:
         print ("tens not eqal ones")
