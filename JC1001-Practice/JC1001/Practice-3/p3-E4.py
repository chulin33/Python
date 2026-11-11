month=input("Please enter the name of the month:")
if month in ("January","March","May","July","August","October","December"):
  print("It has 31 days.")
elif month in ("April","June","September","November"):
  print("It has 30 days.")
else:
  print("Sometimes it has 28 days and sometimes it has 29 days")