class Calulator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square of {n} is {self.n*self.n}")
    
    def cube(self):
        print(f"The square of {n} is {self.n**3}")

    def sqrt(self):
        print(f"The square root of {n} is {self.n**(1/2)}")



n=int(input("ENter a number:"))

c=Calulator(n)
c.square()
c.cube()
c.sqrt()
