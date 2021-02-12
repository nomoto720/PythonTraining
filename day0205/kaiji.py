import random as r
card=['市民','奴隷','皇帝']
player=[0,0,0,0,1]
computer=[0,0,0,0,2]

print('ようこそeカードゲームへ')
input('>>enter')
count=1
while True:
    print(f'{count}戦目')
    print(f'手持ちのカード:市民{count}枚 奴隷{count}枚')
    num=input('カード選択「市民」なら「0」,「奴隷」なら「1」を入力>>')
    print('カードオープン')
    input('>>enter')
    num2=r.randint(0,3,2)
    print(f'あなた:{card[num]} PC:{card[num2]}')
    player.remove(num)
    computer.remove(num2)
    if num==num2:
        print('引き分け')
        count+=1
    elif num+3-num2%3==1:
        print('あなたの勝ち！')
        print('Congratulation!')
        break
    else:
        print('あなたの負け')
        print('GAME OVER')
        break

