# program to calculate area of traingle rectangle and circle in python
import math

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius**2

shape = input("Enter the shape (triangle, rectangle, circle): ")

if shape == "triangle":
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    area = calculate_triangle_area(base, height)
    print("The area of the triangle is:", area)
elif shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = calculate_rectangle_area(length, width)
    print("The area of the rectangle is:", area)
elif shape == "circle":
    radius = float(input("Enter the radius: "))
    area = calculate_circle_area(radius)
    print("The area of the circle is:", area)
else:
    print("Invalid shape entered. Please try again.")
