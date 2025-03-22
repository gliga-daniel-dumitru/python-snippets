
class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hi(self):
        return f"Hi, I am {self.name}!"


person1 = Human("Alice", 30, "engineer")
person2 = Human("Bob", 25, "designer")
person3 = Human("Charlie", 40, "writer")

print(person1.say_hi())  # Output: Hi, I am Alice!
print(person2.say_hi())  # Output: Hi, I am Bob!
print(person3.say_hi())  # Output: Hi, I am Charlie!
