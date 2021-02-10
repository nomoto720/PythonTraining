import random as r
print('数当てゲームを始めます。3桁の数を当ててください!')
answer=[r.randint(0,9) for i in range(3)]
while True:    
    hit=0
    blow=0
    for i in range(3):
        num=int(input(f'{i}桁目の予想を入力(0~9)>>'))
        for j in range(3):
            if answer[j]==num:
                if j==i:
                    hit+=1
                else:
                    blow+=1

    print(f'{hit}ヒット!{blow}ボール!')

    if hit==3:
        print('正解です!')
        break
    else:
        select=int(input('続けますか?1:続ける2:終了>>'))
        if select==2:
            print(f'正解は{answer[0]}{answer[1]}{answer[2]}です')
            break

