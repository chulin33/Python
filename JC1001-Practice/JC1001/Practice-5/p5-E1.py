def withoutVowels(string):
  vowels="aeiouAEIOU"
  result=""
  for i in string:
    if i not in vowels:
      result+=i
  return result.lower()    

print(withoutVowels("No Vowels please"))