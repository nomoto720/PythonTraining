import pprint
q1=[[100-10*i-j for j in range(10)] for i in range(10)]

q2=[[1 if i==j or i+j==4 else 0 for j in range(5)]for i in range(5)]

q3=[[i*10-j*10 for j in range(10)]for i in range(10)]

q4=[[1 if i==j else 2 if j<i else 0 for j in range(5)]for i in range(5)]

q5=[[j+1 if j==i else 0 for j in range(4)]for i in range(4)]

q6=[[i+j for j in range(0,9)]for i in range(60,99,10)]

q7=[[i*j for j in range(1,10)]for i in range(1,10)]

q8=[[3 if j==1 and i==1 else 7 for j in range(3)]for i in range(3)]

q9=[[i*j for j in range(1,10)]for i in range(3,10,2)]

q10=[[(j-i)*2 for j in range(5)]for i in range(2,0,-1c:wq
    )]
pprint.pprint(q10)


