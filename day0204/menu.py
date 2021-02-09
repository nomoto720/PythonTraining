import random
foods={'うどん':200,'ペペロンチーノ':280,'かつ丼':320,'味噌ラーメン':300}
foodNum=['うどん','ペペロンチーノ','かつ丼','味噌ラーメン']
COINS=random.randint(1000,2000)

while True:
    print('メニュー表')
    for i in range(len(foods)):
        print(i,foodNum[i],foods[foodNum[i]],'円') 
    print()
    print('所持金',COINS,'円')
    select=int(input('購入したいメニュー番号を入力してください>>'))
    if foods[foodNum[select]]>COINS:
        print('お金が足りません')
        continue
    COINS-=foods[foodNum[select]]
    foods.pop(foodNum[select])
    print(foodNum.pop(select),'を購入しました')
    print()

    if COINS<=0:
        print('お金がなくなりました')
        break
        
    if len(foods)==0:
        print('全て売り切れました')
        break
