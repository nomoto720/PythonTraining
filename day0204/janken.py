import random
hands=['グー','チョキ','パー']
    
while True:
    your=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
    pc=random.randint(0,2)
    print('あなたは',hands[your],'PCは',hands[pc],)
    num=your-pc+3 % 3
    if num==0:
        print('あいこ')
    elif num==1:
        print('あなたの負け')
        break
    else:
        print('あなたの勝ち')
        break

