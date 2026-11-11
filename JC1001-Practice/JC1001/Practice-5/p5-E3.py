def odd(rhyme):
  result=[i for i in rhyme if i%2!=0]
  return result

input_list=list(map(int,input().split()))
final=odd(input_list)
print(final)