import pprint
H=10
W=10
data=[[0]*W]*H
data[1][1]=5
pprint.pprint(data)

data=[[i*j for i in range(W)] for j in range(H)]
pprint.pprint(data)
