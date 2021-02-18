import string
letters=string.ascii_letters 
n=int(input('幅>>'))
'''
for i in range(len(letters)):
    print(letters[i],end='')
    if (i+1)%n==0:
        print()
print()
'''
'''
for i,c in enumerate(letters):
    print(c,end='')
    if (i+1) % n==0:
        print()
print()
'''
for i in range(0,len(letters),n):
    print(letters[i:i+n])

line=int(len(letters)/n)
if len(letters)%n !=0:
    line+=1
l=int(input(f'何行目(1-{line})>>'))
print(letters[n*(l-1):n*(l-1)+n])
