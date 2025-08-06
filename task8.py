class Student:
    def __init__(self):
        self.__name = ""
        self.__grade = 0

#getter 
    def get_name(self):
        return self.__name 
    def get_grade(self):
        return self.__grade 

#setter
    def set_name(self, name):
        if isinstance(name, str) and name.strip() != "":
            self .__name = name.strip()
        else:
            print("Xeta: Ad duzgun formada olmalidir")

    def set_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= 100:
            self .__grade = grade
        else:
            print("Xeta: Qiymet 0 ile 100 arasinda olmalidir")
            
student = Student()
student.set_name("Aynur")
student.set_grade(95)
print(f"Telebe adi: {student.get_name()}")
print(f"Telebenin qiymeti: {student.get_grade()}")

student.set_grade(150)
student.set_name("")

               