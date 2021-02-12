import random as r
print('****宝探し****')
count=0

table=[i for i in range(1,10)]
hit=r.randrange(9)
while True:
    for i in range(3):
        for j in range(3):
            print(table[i*3+j],end='')
        print()
    if table[hit]=='O':
        break
    select=int(input('好きな場所の数字を選んで入力してください>>'))
    count+=1
    if hit==select-1:
        print('お宝を見つけました!')
        table[select-1]='O'
    else:
        print('ハズレです。',end='')
        if table[select-1]=='X':
            print('選択済みの場所です')
        elif hit>select:
            print('ここより大きな数字の場所にあります')
        else:
            print('ここより小さな数字の場所にあります')
        table[select-1]='X'

print(f'あなたはお宝を{count}回発見しました!')

