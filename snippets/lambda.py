# Python Lambda

# A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

myDoubler = myfunc(2)
print(myDoubler(11))