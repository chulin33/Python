number=int(input("Please enter the total number of item purchased:"))
price=int(input("Please enter the price of the sum of all items:"))
if 10<=number<=19:
  print("the final amount to pay is:",price*0.8)
elif 20<=number<=30:
  print("the final amount to pay is:",price*0.7)
elif number>30:
  print("the final amount to pay is:",price*0.5)
else:
  print("the final amount to pay is:",price)