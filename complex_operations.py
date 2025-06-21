class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __add__(self,c2):
        return Complex(self.real+c2.real,self.img+c2.img)
    
    def display_add(self):
        print(f"{self.real}+{self.img}i")

    def __mul__(self,c2):
        real_part=(self.real*c2.real-self.img*c2.img)
        img_part=self.real*c2.img+self.img*c2.real
        return Complex(real_part,img_part)
    
    def display_mul(self):
        print(f"{self.real}+{self.img}i")
        
r1=int(input("Enter real part of 1st complex number:"))
i1=int(input("Enter imaginary part of 1st complex number:"))
r2=int(input("Enter real part of 2nd complex number:"))
i2=int(input("Enter imaginary part of 2nd complex number:"))

c1=Complex(r1,i1)
c2=Complex(r2,i2)
c3=c1+c2
c4=c1*c2

c3.display_add()
c4.display_mul()