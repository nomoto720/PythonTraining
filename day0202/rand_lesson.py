import random
indexs=list()
for i in range(100):
    indexs.append(random.randint(1,100))
print(indexs)
for i in range(100):
    if indexs[i]==77:
        print('77->',i)
        break
else:
    print('77->','なし')
