import random
COINS=200
TW=5
table=[]



def createTable():
    global table
    table=[[random.randint(0,9) for j in range(TW)]for i in range(TW)]
    for row in table:
        print(row)

#createTable()

def countBingoLine():
    global table
    vertical=[[table[j][i] for j in range(TW)]for i in range(TW)]
    cross=[[table[j][j] if i==0 else table[j][TW-1-j] for j in range(TW)]for i in range(2)]

    bingo_line=0
    for row in table+vertical+cross:
        if len(set(row))==1:
            bingo_line+=1
    return bingo_line

while True:
    print(f'残り枚数:{COINS}')
    #bet=int(input(f'BET枚数を入力。1-{COINS}>>'))
    bet=1
    if bet==0:
        break
    if bet>COINS:
        print('コインが不足してます')
        continue
    COINS -=bet
    createTable()
    bingo_line=countBingoLine()

    if bingo_line>0:
        get_coin=bingo_line*12*bet
        COINS+=get_coin
        print(f'{bingo_line} LINE BINGO !win:{get_coin}')
    else:
        print('boo')

    if COINS==0:
        print('コインがなくなりました')
        break
print('Game Over')


