from math import pi


class Circle:
    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius**2

    def __repr__(self):
        return 'Circle(' + str(self.radius) + ')'


circle1 = Circle(5)

print(circle1.radius)
print(circle1.diameter)
print(circle1.area)
print(circle1)

circle2 = Circle()

print(circle2.radius)
print(circle2.diameter)
print(circle2.area)
