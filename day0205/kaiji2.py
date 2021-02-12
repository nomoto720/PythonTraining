import random as r
player=[
        ['市民','市民','市民','市民'],
        ['奴隷']
        ]
computer=[
        ['市民','市民','市民','市民'],
        [''],
        ['皇帝']
        ]

print('ようこそeゲームへ')
input('>>enter')
num=1

while True:
    print(f'{num}戦目')
    print(f"手持ちのカード:市民{player[0].count('市民')}枚 奴隷{player[1].count('奴隷')}枚")
    p_card=int(input('カード選択:市民なら0,奴隷なら1を入力>>'))
    print('カードオープン')
    print('>>enter')
    c_card=r.randrange(0,3,2)
    print(f'あなた:{player[p_card][0]} PC:{computer[c_card][0]}')
    player[p_card].pop(0)
    computer[c_card].pop(0)
    if p_card==c_card:
        print('引き分け!')
    elif (p_card+3-c_card)%3:
        print('あなたの勝ち!')
        break
    else:
        print('アナタの負け')
        break
    print('>>enter')

