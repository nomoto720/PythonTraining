count=1;
print('カレーを召し上がれ')
while True :
    print(f'{count}皿のカレーを食べました')
    ans=input('おかわりはいかがですか?(y/n)>>')
    count+=1;
    if ans=='n' :
        print('ごちそうさまでした')
        break
