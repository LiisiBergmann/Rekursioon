import turtle



turtle.sety(-100)

def fraktal(pikkus, tase):
    if tase == 0:
        return

    else:
        turtle.forward(pikkus)
        turtle.left(24)
        fraktal(pikkus*0.7,tase-1)
        turtle.right(24)
        turtle.backward(pikkus)

        turtle.forward(pikkus)
        turtle.right(43)
        fraktal(pikkus * 0.7, tase - 1)
        turtle.left(43)
        turtle.backward(pikkus)

turtle.left(90)
turtle.speed(-1)
turtle.delay(0)
fraktal(100,9)
turtle.exitonclick()