# Python functions

# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Arbitrary Arguments, *args
"""
    If you do not know how many arguments that will be passed into your function,
    add a * before the parameter name in the function definition.
    This way the function will receive a 'tuple' of arguments,
    and can access the items accordingly.
"""

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

# output: The youngest child is Linus
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "John", lname = "Smith") # output: His last name is Smith