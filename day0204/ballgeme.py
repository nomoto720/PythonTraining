import random
balls=[ i for i in range(1,100)]
acount=0
bcount=0

for i in range(1,6):
    print(i,'回戦')
    aball=random.randint(1,len(balls))
    aball=balls.pop(aball)
    bball=random.randint(1,len(balls))
    bball=balls.pop(bball)
    select=max(aball,bball)
    shori=( 'A'  if aball==select else 'B')
    acount+=int( '1' if shori=='A' else '0')
    bcount+=int( '1' if shori=='B' else '0')
    print('A:',aball,',B:',bball,'...',shori,'の勝ち')
select=max(acount,bcount)
shori=( 'A' if acount==select else 'B')
print(acount,'対',bcount,'で',shori,'の勝ち')

