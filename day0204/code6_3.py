userinfo=input('名前と血液型をカンマで区切って１行で入力>>')
[name,blood]=userinfo.split(',')
blood=blood.upper().strip()
print('{}さんは{}型なので大吉です'.format(name,blood))

stst=['3','4','5']
print('&'.join(stst))

str='asdasdaweadawaadwae'
print(str.count('a'))
print(str.replace('a','&'))

for s in 'hello':
    print(s)
for u,s in enumerate('hello',1):
    print('{}文字目は{}です'.format(u,s))

s1='olleh'
s2=list(reversed(s1))
print(s2)
s1=''.join(s2)
print(s1)

s3=s1[::-1]
print(s3)

print(len(s1))
