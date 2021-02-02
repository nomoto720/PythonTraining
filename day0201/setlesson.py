scores={70,80,55,80}
scores.add(80)
print(scores)
print('要素数は{}'.format(len(scores)))
print('合計は{}'.format(sum(scores)))

scores={'network':60,'database':80,'security':60}
members=['松田','浅木','工藤']
print(tuple(members))
print(list(scores))
print(set(scores.values()))

dict1=dict(zip(['赤','緑','青'],['r','g','b']))
print(dict1)

a=['a','i','u']
b=['あ','い','う']
dict2=dict(zip(a,b))
print(dict2)

matsuda_scores={'netwark':60,'database':80,'security':50}
asagi_scores={'netwark':80,'database':75,'security':92}
member_scores={
        '松田':matsuda_scores,
        '浅木':asagi_scores
        }
print(member_scores)        
print(member_scores['松田']['netwark'])        
print(len(member_scores))


member_hobbies={
        '松田':{'SNS','麻雀','自転車'},
        '浅木':{'麻雀','食べ歩き','数学'},
        }
print(member_hobbies)
print(member_hobbies['松田'])
print(member_hobbies['浅木'])

common_hobbies=member_hobbies['松田'] & member_hobbies['浅木']
print(type(common_hobbies))
print(common_hobbies)

a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c)
print(c[0])
print(c[1][2])

d=[[1,2,3],[4,5,6],[7,8,9]]
print(d[2][2])


A={1,2,3,4}
B={2,3,4,5}
print(A | B)
print(A & B)
print(A - B)
print(A  B)
