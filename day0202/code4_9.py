ages=[28,50,8,20,'ひみつ',78,25,'無回答',22,10,27,33]
samples=list()
for age in ages:
    if not isinstance(age,int):
        continue
    if 20 <= age < 30:
         samples.append(age)
print(samples)
