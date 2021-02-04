def eat(breakfast, lunch='ラーメン',dinner='カレー',*desserts):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))
    for d in desserts:
        print('おやつに{}をたべました'.format(d))
"""
eat(breakfast='納豆ご飯',dinner='カレーうどん')
eat(dinner='カレーうどん',breakfast='納豆ご飯')
eat('納豆ご飯',dinner='カレーうどん')
"""
eat('トースト','パスタ','カレー','アイス','チョコ','パフェ')
