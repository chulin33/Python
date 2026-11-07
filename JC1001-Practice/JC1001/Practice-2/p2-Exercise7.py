days=int(input("days:"))
hours=int(input("hours:"))
minutes=int(input("minutes:"))
seconds=int(input("seconds:"))
times1=days*24
times2=(times1+hours)*60
times3=(times2+minutes)*60
times4=times3+seconds
print("the total number of seconds is:",times4)