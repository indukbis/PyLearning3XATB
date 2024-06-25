#Calculate the area of circle

#input - radius
#output - area

#datatype - input - int or float
#output - float

# core logic - pi*r*r = 3.14
#math.pi
import math

radius = float(input("Enter the radius\n"))
print(math.pi)
area = math.pi*(radius**2)
area2 = math.pi*(math.pow(radius,2))
print(area)
print(area2)

print(math.pi*(float(input("Enter the radius\n"))**2))
