def sumof2(n):
    return sum(range(1,n+1))

def sumof3(n):
    if n <1:
        return n
    else:
        return n+sumof3(n-1)

num=int(input('正の整数'))
ans=sumof3(num)
print(ans)
