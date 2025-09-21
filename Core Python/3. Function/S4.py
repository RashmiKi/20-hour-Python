import math
def circle(radius):
    circumference = 2*math.pi*radius
    area = math.pi*(radius**2)
    return(circumference, area)

rad = float(input("Enter circle radius "))

print (circle(rad))