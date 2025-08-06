class SchoolMember:
    def __init__(self, name, role, age):
        self.__name = name
        self.__role = role  
        self.__age = age 
        
#getter
    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def get_age(self):
        return self.__age

#setter
    def set_name(self, name):
        self.__name = name 

    def set_role(self, role):
        self.__role = role   

    def set_age(self, age): 
     if age < 5:
        self.__age = age 
     else:
        print("Invalid age")

    def introdunce(self):
        print("Men mekteb uzvuyem")

class Teacher(SchoolMember):
    def __init__(self, name, age, subject):
        super().__init__(name, "Teacher", age)
        self.subject = subject 

    def introduce(self):
        print(f"Men muellimem. Adim {self.get_name()}, yasim {self.get_age()}, fennim {self.subject}.")

class Student(SchoolMember):
    def __init__(self, name, age, grade):
        super().__init__(name, "Student", age)
        self.grade = grade 
    
    def introduce(self):
        print(f"Men telebeyem, adim {self.get_name()}, {self.get_age()} yasim var, sinfim {self.grade}")

#Yoxlayaq:
teacher = Teacher("Jack", 32, "Mathematic")
student = Student("Robert", 15, "10B")

teacher.introduce()
student.introduce()

student.set_age(4)
teacher.set_role("lider")
print(teacher.get_role())