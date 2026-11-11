length1=int(input("Please enter the length of the room1:"))
width1=int(input("Please enter the width of the room1:"))
length2=int(input("Please enter the length of the room2:"))
width2=int(input("Please enter the width of the room2:"))
area1=length1*width1
area2=length2*width2
if area1>area2:
  print("the room1 is larger")
elif area1<area2:
  print("the room2 is larger")
else:
  print("the areas are the same")