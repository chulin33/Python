def multiply10(rhyme):
  result=[i*10 for i in rhyme]
  return result

input_list=list(map(int,input().split()))
final=multiply10(input_list)
print(final)