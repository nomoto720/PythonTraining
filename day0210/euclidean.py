def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)
x,y=1071,432
print(gcd(x,y))
