# Create function without return value
def hello(name):
    print(f"Hello {name}")


# Create function with return value
def area(width, height=0):
    return width * height


# Call hello() function
hello("Samit")

# Call area() function
print("Area is", area(5, 5), "sq.m")
