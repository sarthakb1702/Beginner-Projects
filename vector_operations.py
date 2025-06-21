class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        a=Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return a
    
    def __mul__(self,other):
        b=Vector(self.x*other.x,self.y*other.y,self.z*other.z)
        return b
    
    def display(self):
        print(f"{self.x}i+{self.y}j+{self.z}k")
    
x1=5
y1=2
z1=3
x2=3
y2=8
z2=5
x3=2
y3=4
z3=8

a1=Vector(x1,y1,z1)
a2=Vector(x2,y2,z2)
a3=Vector(x3,y3,z3)

s1=a1+a2
s1=s1+a3
s2=a1*a2
s2=s2*a3
print("Sum of vector:")
s1.display()
print("Multiplication of vector:")
s2.display()