import random
import turtle
ts=[]

def setup():
    global ts
    startline=-620
    screen=turtle.Screen()
    screen.setup(1290,720)
    screen.bgpic('beach.gif')

    t_y=[-250,-225,-200,-175,-150,-125,-100,-75,-50,-25,0,25,50,75,100,125,150,175,200,225,250]
    t_color=['green','green','green','green','green','green','green','green','green','green','green','green','green','green','green','green','green','green','green','green','green']

    for i in range(len(t_y)):
        t=turtle.Turtle()
        t.shape('turtle')
        t.penup()
        t.setpos(startline,t_y[i])
        t.color(t_color[i])
        #t.pendown()
        ts.append(t)

def race():
    global ts
    finishline=540

    while True:
        for current_t in ts:
            move=random.randint(1,20)
            current_t.forward(move)
            current_t.right(move)
            current_t.left(move)
            x=current_t.xcor()
            if x >=finishline:
                winner_color=current_t.color()
                current_t.write('Win!'+winner_color[0],font=('Arial',26,'normal'))
                break
        else:
            continue
        break
setup()
race()
turtle.mainloop()
