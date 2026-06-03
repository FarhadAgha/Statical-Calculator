# Define the function that calculates and prints circumference
def print_circum(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    print(f"Radius: {radius}, Circumference: {circumference}")

# Call the function three times with different radius values
print_circum(5)
print_circum(7.5)
print_circum(10)