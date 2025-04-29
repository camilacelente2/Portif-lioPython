
#breakeecontinue.py

#Break
for i in range(10):
  print(i)
  if (i == 5):
    break

#Continue
i = 0
while (i<10):
  i+=1
  if (i%2==0):#É Par
    continue
  print(i)
