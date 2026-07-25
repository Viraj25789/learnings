class Person:

    def __init__(self, name, age):
        self.name= name
        self.age= age
    
class Student(Person):

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def show_info(self):
        return f"name: {self.name}\nage:{self.age}\nmarks:{self.marks}"

Student_1 = Student("Viraj","22","100")
Student_2 = Student("Joy",marks="90",age="30")

print(Student_1.show_info())
print(Student_2.show_info())