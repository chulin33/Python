a=int(input("Please enter the length of a side of the triangle:"))
b=int(input("Please enter the length of a side of the triangle:"))
c=int(input("Please enter the length of a side of the triangle:"))
if a==b==c:
  print("It is an equilateral.")
else:
  if a==b or a==c or b==c:
    print("It is an isosceles.")
  else:
    print("It is a scalene.")