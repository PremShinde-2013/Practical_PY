#program to calculate volume of sphere using class
import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def calculate_volume(self):
        volume = (4/3) * math.pi * self.radius**3
        return volume

# Example usage
radius = float(input("Enter the radius of the sphere: "))

# Create an instance of the Sphere class
my_sphere = Sphere(radius)

# Calculate the volume
volume = my_sphere.calculate_volume()

print("The volume of the sphere is:", volume)
