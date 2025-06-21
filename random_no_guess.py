import random
from random import randint

a=randint(1,100)

guess_count=0

for i in range (1,100):
    user_input=int(input("Guess the number:"))
    guess_count=guess_count+1
    if user_input<a:
        print("Higher number please")
    elif user_input>a:
        print("Lower number please")
    elif user_input==a:
        print(f"You guessed the number in {guess_count} guesses\n")
        break

with open ("no_guesser.txt") as f:
    lowest_score=int(f.read())


    if guess_count<lowest_score:
        print("New high score!!!!")
        with open ("no_guesser.txt",'w') as f:
            f.write(str(guess_count))
    elif guess_count==1:
        print("Lowest score is 1")
        print("Resetting......")
        f.write("0")
    else:
        print(f"Lowest score is {lowest_score}")
