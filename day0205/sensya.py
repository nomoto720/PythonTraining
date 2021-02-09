import random
medals=['鉄十字勲章','騎士鉄十字勲章','柏葉付騎士鉄十字勲章','柏葉・剣付騎士鉄十字勲章','柏葉・ 剣・ダイヤモンド付騎士鉄十字勲章','黄金柏葉・剣・ダイヤモンド付騎士鉄十字勲章']
days=1
hospital=0
bom_count=0
while days<=100:
    print(days,'日目の行動')
    if hospital>0 :
        print(f'後{hospital}日の入院が必要です')
        hospital-=1
        print('今は休んでくださいね(Enter)')
    else:
        print('出撃')
        bom=random.randint(1,15)
        bom_count+=bom
        damege=random.randint(1,100)
        print(f'戦功報告:{bom}輌の戦車を撃破しました!')
        if(damege==1):
            print('あなたは戦士してしまいました...')
            break
        elif 1<damege<12 :
            print('あなたは撃墜され、怪我をしてしまいました。６日間の入院が必要です')
            print('今は休んでくださいね(ENter)')
            hospital=6
        else:
            print('明日も頑張りましょう!(Enter)')
    days+=1
    input()
if days>100:
    print('戦争は集結しました!!') 
num=0
if bom_count<100 :
    num=0
elif bom_count<200:
    num=1
elif bom_count<300: 
    num=2
elif bom_count<400:
    num=3
elif bom_count<500:
    num=4
else:
    num=5
print(f'最終戦果報告!!あなたは{bom_count}の戦車を破壊した功績により{medals[num]}を授与されました!!')
