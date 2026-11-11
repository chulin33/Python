letter=input("Please enter a letter:")
if letter in ("a","e","i","o","u"):
  print(letter,"is a vowel")
elif letter=="y":
  print("y can sometimes be a vowel and sometimes is not")
else:
  print(letter,"is a consonant")