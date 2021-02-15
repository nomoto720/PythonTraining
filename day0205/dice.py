import random as r

i=0
input('Enterで対決開始[Enter]')
while True:
    you_dice=[r.randint(1,6) for i in range(3)]
    pc_dice=[r.randint(1,6) for i in range(3)]
    print('あなたの出目')
    print(you_dice)
    print('コンピューターの出目')
    print(pc_dice)
    you_sum=0
    pc_sum=0
    for i in range(len(you_dice)):
        you_sum+=you_dice[i]
    for i in range(len(pc_dice)):
        pc_sum+=pc_dice[i]
    win_lose=''
    yous=set(you_dice)
    pcs=set(pc_dice)
    if len(yous)==1:
        you_sum*=2
    if len(pcs)==1:
        pc_sum*=2
    if you_sum>pc_sum:
        win_lose='あなたの勝ち'
    elif you_sum<pc_sum:
        win_lose='あなたの負け'
    else:
        win_lose='あいこ'
    print(f'{you_sum}対{pc_sum}で{win_lose}')
    select=input('もう一度対決しますか?<y/n>>>')
    if select=='n':
        break
print('対決を終了します')

