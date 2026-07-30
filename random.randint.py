import random


random.seed(1)
best_score = None
while True:
   secret_number = random.randint(1,100)
   guesses = 0
   print("i picked a number between 1 and 100")
   while True:
       user_guess =int(input("guess? "))
       guesses += 1
       if user_guess > secret_number :
           print ("too high")
       elif user_guess < secret_number :
           print("too low")
       else:
           print("correct!")
           break
   if best_score is None or guesses < best_score:
        best_score = guesses
   play_again =input("doy you want to play again? (yes/no):").strip().lower()
   if  play_again != 'yes':
      break
if best_score is not None:
    print(f"best score:{best_score} guesses")
else:
     print("None")
