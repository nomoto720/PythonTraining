import turtle
t=turtle.Turtle()
t.shape('turtle')
while True:
    num=int(input('カメちゃんに何角形を描いてもらう?(3以上の半角整数,0で終了)>>'))
    if num==0:
        turtle.bye()
        break
    t.clear()
    angle=360/num
    for i in range(num):
        t.right(angle)
        t.forward(100)
print('bye')
