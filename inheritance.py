
class Education_info():
    marks_12th=87
    cet_marks=97
    @staticmethod
    def disp1():
        print(f"12th marks={Education_info.marks_12th}\nCET marks={Education_info.cet_marks}")

class personal_info(Education_info):
    name="Sarthak"
    age=18
    @staticmethod
    def disp2():
        Education_info.disp1()
        print(f"Name={personal_info.name}\nAge={personal_info.age}")

b=personal_info()
b.disp2()
