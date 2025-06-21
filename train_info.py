import random
class Train:
    def __init__(self):
        self.book=False
        self.seats=random.randint(0,40)
        self.fare=700


    def bookTicket(self):
        user_input=input("Do you want to book your ticket ?:\n")

        if user_input=="yes":
            self.bookTicket=True
            self.show_status()
            self.show_fare()
        else:
            print("Booking cancelled")

    def show_status(self):
        if self.seats==0:
            print("No seats available!")
        else:
            print(f"No. of seats available are {self.seats}")

    def show_fare(self):
        print(f"The fare of ticket is {self.fare}")

t=Train()
t.bookTicket()