## Creating Variables
x = 5       # x is of type int
y = "John"  # y is of type str
print(x)    # 5
print(y)    # "John"

x = "John"  # x is now of type str
print(x)    # "John"

## Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

## Get the Type
x1 = 5
y1= "John"
print(type(x1)) # <class 'int'>
print(type(y1)) # <class 'str'>

## Many Values to Multiple Variables
a,b,c = "Orange", "Banana", "Cherry"
print(a,b,c)    # Orange Banana Cherry

## One Value to Multiple Variables
m = n = p = "Orange"
print(m, n, p)  # Orange Orange Orange