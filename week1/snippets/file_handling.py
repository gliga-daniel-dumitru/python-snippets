# Open for reading
file = open("example.txt", "r")  # Open for reading

# Reading the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")

# Appending to a file
    with open("example.txt", "a") as file:
        file.write("\nAppending a new line.")

# Close the file
file.close()

        
    