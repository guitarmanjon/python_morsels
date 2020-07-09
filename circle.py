from math import pi
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return 'Circle(' + str(self.radius) + ')'

    @property # getter
    def diameter(self):
        return self.radius * 2

    @property # getter
    def area(self):
        return pi * self.radius**2

    @diameter.setter
    def diameter(self, dia):
        self.radius = dia / 2
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, rad):
        if rad < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = rad
                

circle1 = Circle(5)

print(circle1.radius)
print(circle1.diameter)
print(circle1.area)
print(circle1)
# check that setting radius changes diameter and area
circle1.radius = 10
circle1.radius = -7