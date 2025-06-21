class Brand:
    def __init__(self,brand_name):
        self.brand_name= brand_name

    def showBrand(self):
        print(f"Name of brand:{self.brand_name}")

class Colour:
    def __init__(self,colour):
        self.colour= colour

    def dispcolour(self):
        print(f"Colour={self.colour}")

class Model(Brand,Colour):

    def __init__(self,brand_name,colour,model_name):
        Brand.__init__(self,brand_name)
        Colour.__init__(self,colour)
        self.model_name= model_name

    def showModel(self):
        print(f"Model Name: {self.model_name}")

brand=input("Enter Brand Name:")
colour=input("ENter Colour:")
model_name=input("ENter Model Name:")

a=Model(brand,colour,model_name)
a.showBrand()
a.dispcolour()
a.showModel()
