import math

#circumference of the circle

r = float(input("enter r of a circle: "))
circumference = 2 * math.pi * r
print(f"The circumference is {round(circumference, 2)}cm")

# Area of the circle

area = math.pi * pow(r,2)
print(f"An area of the circle is: {round(area,2)}cm^2")

print("Hypotenuse of the right triangle")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
h = math.sqrt(pow(a,2) + pow(b,2))
print(f"hypotenuse: {round(h,2)}")