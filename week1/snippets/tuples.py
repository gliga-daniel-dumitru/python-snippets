# Python Tuples
thisTuple = ("apple", "banana", "cherry") # Create a list by using ()
print(thisTuple) # output: ('apple', 'banana', 'cherry')

# Tuple Items
## Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
print(thisTuple[0]) # "apple"
print(thisTuple[1]) # "banana"

# Tuple Length
print(len(thisTuple)) # output: 3
print(type(thisTuple))  # output: <class 'tuple'>

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

# Access Tuple Items
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple[1])     # output: banana
print(thisTuple[2:5])   # output:('cherry', 'orange', 'kiwi')

# Check if Item Exists
thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
  print("Yes, 'apple' is in the fruits tuple")

# Add tuple to a tuple
thisTuple = ("apple", "banana", "cherry")
y = ("orange",)
thisTuple += y

print(thisTuple) # ('apple', 'banana', 'cherry', 'orange')

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)  # apple
print(yellow) # banana
print(red)    # cherry

# Loop Through a Tuple
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
  print(x)

# Loop Through the Index Numbers
thisTuple = ("apple", "banana", "cherry")
for i in range(len(thisTuple)):
  print(thisTuple[i])

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)