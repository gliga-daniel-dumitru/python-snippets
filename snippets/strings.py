### Strings

s = "Hello World"

print(s[1]) # access 2nd char - prints "e"
s1 = s + s[0] # update
print(s1) # prints "Hello WorldH"

## Multi-line Strings

s = """I am Learning
Python Strings"""
print(s)

## String Slicing
s = "Hello World"

print(s[1:4]) # Retrieves characters from index 1 to 3: 'ell'
print(s[:3])  # Retrieves characters from beginning to index 2: 'Hel'
print(s[3:])  # Retrieves characters from index 3 to the end: 'lo World'

## Common String Methods
s = "Hello World"

print(len(s))       # output: 11
print(s.upper())    # output: HELLO WORLD
print(s.lower())    # output: hello world

## Formatting Strings
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}") # output: 'Name: Alice, Age: 22'

