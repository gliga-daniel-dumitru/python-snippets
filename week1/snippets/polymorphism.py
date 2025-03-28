class Person:
    def introduce(self):
        return "Hello, I am a person."

class Student(Person):
    def introduce(self):
        return "Hello, I am a student."

class Teacher(Person):
    def introduce(self):
        return "Hello, I am a teacher."

def introduce_person(person):
    print(person.introduce())

student = Student()
teacher = Teacher()
person = Person()

introduce_person(student)  # Output: Hello, I am a student.
introduce_person(teacher)  # Output: Hello, I am a teacher.
introduce_person(person)   # Output: Hello, I am a person.

