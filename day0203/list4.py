import pprint

x=[n for n in range(1,8)]
print(x)

x=[n**2 for n in range(1,8)]
print(x)

x=[n for n in range(1,8) if n %2==0]
print(x)

x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)

x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
pprint.pprint(matrix)

matrix2=[]
for i in range(row):
    temp=[]
    for j in range(col):
        temp.append(1 if i==j else 0)
    matrix2.append(temp)
print(matrix2)



x=[[0 if i!=j else 1*i+1 for j in range(4)] for i in range(3)]
print(x)

print()
print('ふじむらさん')
x=[[ 101-i*10-j for j in range(1,11)] for i in range(10)]
pprint.pprint(x)

print()
print('佐久間さん')
x=[[1 if i==j or i+j==4 else 0 for j in range(5)] for i in range(5)]
pprint.pprint(x)

print()
print('武田さん')
x=[[i-j for j in range(0,100,10)] for i in range(10,100,10)]
pprint.pprint(x)

print()
print('佐藤さん')
x=[[1 if i==j else 2 if i>j else 0 for j in range(5)]for i in range(5)]
pprint.pprint(x)

print()
print('松尾さん')
x=[[i*10+j for j in range(60,69)] for i in range(4)]
pprint.pprint(x)

print()
print('廣瀬さん')
x=[[ j*i for j in range(1,10)]for i in range(1,10)]
pprint.pprint(x)

print()
print('はなもとさん')
x=[[3 if i==1 and j==1 else 7 for j in range(3)] for i in range (3)]
print(x)

print()
print('かのさん')
x=[[i*j for j in range(1,10)] for i in range(3,10,2)]
pprint.pprint(x)

print()
print('古屋さん')
x=[[j-i for j in range(2,11,2)]for i in range(2)]
pprint.pprint(x)
print()

print('上杉')
x=[['*' if i%2==0 and j%2==0 else '_' for j in range(1,11)] for i in range(10)]
pprint.pprint(x)
print()

print('早坂さん')
x=[[j+i*i for j in range(10)] for i in range(10)]
pprint.pprint(x)

print()
data=[[i*10+j for j in range(1,11)] for i in range(10)]
pprint.pprint(data)
