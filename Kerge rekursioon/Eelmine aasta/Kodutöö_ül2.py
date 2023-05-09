import turtle



def ruudud(pikkus, korrad):

    if korrad == 1:
        for b in range(4):
            turtle.forward(pikkus)
            turtle.right(90)

    else:
        for i in range(4):
            turtle.forward(pikkus)
            turtle.left(90)
            ruudud(pikkus * 0.6, korrad - 1)
            turtle.right(180)



turtle.speed(-1)
ruudud(50, 3)
turtle.exitonclick()