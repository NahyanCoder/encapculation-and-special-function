class Student:
    _schoolName1='Chittagong Grammar School'#private variable
    def __init__(self, name, age):
        self.__name=name#private instances
    def __display(self):#private method
        print("This is the private method.")
std = Student("Bill",25)
print(std._schoolName1)