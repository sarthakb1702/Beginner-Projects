import random

def game():
    score=random.randint(1,100)
    with open ("highscore.txt") as f:
        highscore=f.read()
        if highscore=="100":
            with open ("highscore.txt","w") as f:
                f.write("0")
                print("Previous highscore was 99... resetting to 0...")
        if highscore=="":
            highscore=0
        elif(score>int(highscore)):
            print("Congrajulations... you have beat the high score!!")
            print(f"Your score is {score}")
            with open ("highscore.txt","w") as f:
                f.write(str(score))
        elif(score<int(highscore)):
            print("You haven't beat the high score... better luck next time")
            print(f"Your score is {score}")

        
            
game()