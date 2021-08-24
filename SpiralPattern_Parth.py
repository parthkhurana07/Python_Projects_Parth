import turtle
t= turtle.Pen()
t.shape("arrow")
turtle.bgcolor("black")
t.speed(0)
for x in range(100,10000, 25):
    t.pencolor("white")
    t.forward(x/100)
    t.left(16)
    t.pencolor("blue")
    t.forward(x/100)
    t.left(10)

