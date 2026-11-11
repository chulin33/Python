import random
valid_signals=[]
for i in range(10):
  signal=random.randint(1,100)
  if signal<50:
    continue
  else:
    valid_signals.append(signal)
print(valid_signals)
print(len(valid_signals))  