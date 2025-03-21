# Python Sets

mySet = {"apple", "banana", "cherry"} # Create a set by using {}

print(type(mySet)) # output: <class 'set'>

# Access Items
# You cannot access items in a set by referring to an index or a key.

# Loop through the set, and print the values:
thisSet = {"apple", "banana", "cherry"}

for x in thisSet:
  print(x)

thisSet = {"apple", "banana", "cherry"}
print("banana" in thisSet) # output: True

# Add Items
thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")

print(thisSet) # {'orange', 'banana', 'apple', 'cherry'}

# Add Sets
thisSet = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisSet.update(tropical)

print(thisSet) # {'cherry', 'banana', 'papaya', 'apple', 'mango', 'pineapple'}

# Remove Set Items
thisSet = {"apple", "banana", "cherry"}
thisSet.remove("banana")  # If the item to remove does not exist, remove() will raise an error.
thisSet.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.

print(thisSet)
