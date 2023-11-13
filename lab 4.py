# Step 2
for i in range(11):
    print(i)


# Step 3
for i in range(1, 11):
    print(i)


# Step 4
for i in range(1, 11, 2):
    print(i)


# Step 5
radius = int(input("Enter the radius of the circle: "))

# Step 6
import math
pi = math.pi

# Step 7
if radius > 0:
    area_circle = pi * (radius ** 2)
    print("Area of the circle", area_circle)
else:
    print("Input parameters are not greater than 0. Cannot compute the area of the requested polygon.")


# Step 8
length = int(input("Enter the length of the rectangle: "))

# Step 9
width = int(input("Enter the width of the rectangle: "))

# Step 10
if length > 0 and width > 0:
    area_rectangle = length * width
    print("Area of the rectangle", area_rectangle)
else:
    print("Input parameters are not greater than 0. Cannot compute the area of the requested polygon.")

# Step 11
if radius > 0:
    area_circle = pi * (radius ** 2)
    print("Area of the circle", area_circle)
else:
    print("Input parameters are not greater than 0. Cannot compute the area of the requested polygon.")

if length > 0 and width > 0:
    area_rectangle = length * width
    print("Area of the rectangle", area_rectangle)
else:
    print("Input parameters are not greater than 0. Cannot compute the area of the requested polygon.")




