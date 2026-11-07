data=input("请输入你的身高（m）和体重（kg），用空格隔开").split()
height=float(data[0])
weight=float(data[1])
BMI=weight/(height**2)
if BMI<18.5:
  print("Underweight")
elif 18.5<=BMI<24:
  print("Normal")
else:
  print("Overweight")
  print(round(BMI,2))
