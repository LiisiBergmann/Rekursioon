
import turtle

def kolmnurgad(tase, pikkus):

    if tase == 0:
        return
    else:
        turtle.forward(pikkus)
        turtle.left(120)
        turtle.forward(pikkus)
        turtle.left(120)
        turtle.forward(pikkus)
        turtle.left(120)
        turtle.forward(pikkus)
        turtle.right(60)
        kolmnurgad(tase-1, pikkus)



turtle.speed(-1)
kolmnurgad(6,50)
turtle.exitonclick()