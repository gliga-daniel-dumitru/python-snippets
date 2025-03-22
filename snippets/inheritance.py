
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

class Employee(Person):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

    def introduce(self):
        return f"Hi, my name is {self.name}, I am {self.age} years old, and I work as a {self.occupation}."

person = Person("Alice", 30)
print(person.say_hi())  # Output: Hi, my name is Alice and I am 30 years old.

employee = Employee("Bob", 25, "designer")
print(employee.say_hi())  # Output: Hi, my name is Bob, I am 25 years old,
                          # and I work as a designer.

       