class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"I'm a student and my grade is {self.grade}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I'm a teacher and I teach {self.subject}.")

person1 = Person("Yebi", 19)
student1 = Student("Yebi", 19, "A")
teacher1 = Teacher("Arie Vatresia", 30, "object oriented programming")

person1.introduce() 
print(" ")
student1.introduce()  
print(" ")
teacher1.introduce()  
