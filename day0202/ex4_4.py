for i in range(1,10):
    for j in range(1,10):
        if i%2==0:
            continue
        else:
            num=i*j
            ans=format(num,'2')
            print(ans,end=' ')
            if num>50:
                break
       
    print('')
