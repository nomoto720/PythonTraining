def seisu(num):
    sum=0
    for i in range(num):
        sum+=i+1    
    return sum 

num=int(input('正の整数>>'))
num=seisu(num)
print(num)

    
