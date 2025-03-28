## Lists
mylist = ["apple", "banana", "cherry"] # Create a list by using []

## List items are indexed, the first item has index [0], the second item has index [1] etc.
print(mylist[0]) # "apple"
print(mylist[1]) # "banana"

# List Length
thisList = ["apple", "banana", "cherry"]
print(len(thisList))    # output: 3
print(type(thisList))   # output: <class 'list'>

# The list() Constructor
thisList = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thisList)   # output: ['apple', 'banana', 'cherry']

# Add List Items
thisList.append("orange")
print(thisList) # output: ['apple', 'banana', 'cherry', 'orange']

# Remove Specified Item

thisList.remove("banana") # Remove the first occurrence of "banana"
thisList.pop(1) # Remove Specified Index
del thisList[0] # The 'del' keyword also removes the specified index

# Clear the List
thisList.clear()

# Loop Through a List
thisList = ["apple", "banana", "cherry"]
for x in thisList:
  print(x)

# Loop Through the Index Numbers
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
  print(thisList[i])

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if "a" in x]
print(newList) # ['apple', 'banana', 'mango']

# Sort Lists
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(reverse = True)
print(thisList)

# Copy a List
thisList = ["apple", "banana", "cherry"]
mylist = thisList.copy()
print(mylist)

## Use the list() method
thisList = ["apple", "banana", "cherry"]
mylist = list(thisList)
print(mylist)

## Use the slice Operator
thisList = ["apple", "banana", "cherry"]
mylist = thisList[:]
print(mylist)