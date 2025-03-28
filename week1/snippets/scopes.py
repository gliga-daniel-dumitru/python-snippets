# Global scope
x = "I am global"

def outer_function():
    # Enclosing scope
    x = "I am in outer_function"

    def inner_function():
        # Local scope
        x = "I am in inner_function"
        print(x)  # Output: I am in inner_function

        inner_function()
        print(x)  # Output: I am in outer_function

outer_function()
print(x)  # Output: I am global

def nonlocal_example():
    x = "outer value"

    def inner_function():
        nonlocal x
        x = "modified by inner_function"
        print(x)  # Output: modified by inner_function

    inner_function()
    print(x)  # Output: modified by inner_function

nonlocal_example()

      