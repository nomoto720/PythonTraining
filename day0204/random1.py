import random
num=int(input('100~1000の範囲の偶数をいくつ生成する>>'))
randoms=[random.randrange(100,1000,2) for _ in range(num)]
randoms.sort(reverse=True)
print(num,'個生成しました!降順に表示します',randoms)
