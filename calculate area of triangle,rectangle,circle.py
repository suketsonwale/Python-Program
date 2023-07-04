# program to find area of circle, triangle, rectangle.
# Area of triangle:
print("Area of triangle :-")
height = float(input("Enter height of triangle : "))
base = float(input("Enter the base of triangle : "))
area = (height*base)/2
print("The area of triangle with height = ",height," and base = ",base," is equal to : ",area)

# Area of rectangle:
print("\nArea of rectangle :-")
width = float(input("Enter the width of rectangle : "))
height = float(input("Enter height of rectangle : "))
area = (height*width)
print("The area of rectangle with height = ",height," and width = ",width," is equal to : ",area)

# Area of circle:
print("\nArea of circle :-")
radius = float(input("Enter the radius of circle : "))
area = 3.14*radius*radius
print("The area of circle with radius = ",radius," is equal to : ",area)