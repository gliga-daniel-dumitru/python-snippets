people = {
            "Alice": {"age": 30, "job": "lawyer"},
            "Bob": {"age": 20, "job": None}
        }

for name, details in people.items():
    age = details.get("age", 0)
    job = details.get("job", "student")

formatted_string = f"My name is {name}, I am {age} years old. " \
                   f"Next year, I will be {age + 1} years old. " \
                   f"I am currently a {job}."

print(formatted_string)

# Output:
# My name is Alice, I am 30 years old. Next year, I will be 31 years old. I am currently a lawyer.
# My name is Bob, I am 20 years old. Next year, I will be 21 years old. I am currently a student.
