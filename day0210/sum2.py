def kaijyo(n):
    if n <=1:
        print(n)
        return n
    else:
        print(n,'*kaijyo(',n-1,')')
        return n*kaijyo(n-1)
num=int(input('整数を入力'))
ans=kaijyo(num)
print(ans)
