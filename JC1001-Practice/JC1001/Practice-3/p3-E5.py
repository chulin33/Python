sides=int(input("Please enter the number of sides:"))
if sides == 3:
    print("A shape with 3 sides is a triangle.")
elif sides == 4:
    print("A shape with 4 sides is a quadrilateral.")
elif sides == 5:
    print("A shape with 5 sides is a pentagon.")
elif sides == 6:
    print("A shape with 6 sides is a hexagon.")
elif sides == 7:
    print("A shape with 7 sides is a heptagon.")
elif sides == 8:
    print("A shape with 8 sides is an octagon.")
elif sides == 9:
    print("A shape with 9 sides is a nonagon.")
elif sides == 10:
    print("A shape with 10 sides is a decagon.")
else:
    print("Error: the number of sides must be between 3 and 10.")