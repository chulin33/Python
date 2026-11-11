a=0
b=int(input("Please enter a number:"))
while b!=0:
  if b>a:
    a=b
  b=int(input("Please enter a number:"))
print("the highest one is:",a)