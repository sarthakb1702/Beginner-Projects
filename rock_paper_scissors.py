from random_picker import pick_random_number

dict={1:"Rock",
      2:"Paper",
      3:"Scissors"}


random_number = pick_random_number(list(dict.keys()))

user=int(input("Enter 1 for rock , 2 for paper , 3 for scissors:"))

if random_number in dict:
    print(f"Computer chosed {dict[random_number]}")
if user in dict:
    print(f"You chosed {dict[user]}")

if(random_number==user):
    print("Its a draw!")
else:
    if(random_number==1 and user==2):
        print("You win!")
    elif(random_number==1 and user==3):
        print("You lose!")
    if(random_number==2 and user==1):
        print("You lose!")
    elif(random_number==2 and user==3):
        print("You win!")
    if(random_number==3 and user==1):
        print("You win!")
    elif(random_number==3 and user==2):
        print("You lose!")
