import random
num=int(input('サイコロを何回フル?>>'))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print('出た目は',set(dices),'の',len(set(dices)),'種類')
