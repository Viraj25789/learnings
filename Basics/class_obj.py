# class Car:
#     def __init__(self, brand, model, year):
#         self.brand =brand
#         self.model=model
#         self.year=year
#     def show_info(self):
#         print(f"brand: {self.brand}\nmodel: {self.model}\nyear: {self.year}")
# car_1 = Car("BMW","M4","2024")
# car_1.show_info()


class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=int(marks)
    
    def grade(self):
        if self.marks>=90:
            print("A")
        elif self.marks>=75:
            print("B")
        elif self.marks>=35:
            print("C")
        else:
            print("Fail")

student_1=Student("viraj","100")
student_2=Student("jolly","35")
student_3=Student("bunny","34")

students=[student_1,student_2,student_3]

for i in students:
    i.grade()