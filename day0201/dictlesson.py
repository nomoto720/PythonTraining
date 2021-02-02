dict1=dict()
dict1['apple']='りんご'
dict1['orange']='みかん'
print(dict1)

print(len(dict1))
dict1['banana']='ばなな'

del dict1['orange']
print(dict1)

print(dict1['apple'])

print(dict1.get('pine'))

if 'apple' in dict1:
    print('含まれている')

if 'pine' not in dict1:
    print('含まれていません')

if 'りんご' in dict1.values():
    print('含まれている')
