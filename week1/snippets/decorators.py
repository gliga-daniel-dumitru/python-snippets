def simple_decorator(func):
    def wrapper():
        print("Start of function execution.")
        func()
        print("End of function execution.")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")

# Example usage
greet()