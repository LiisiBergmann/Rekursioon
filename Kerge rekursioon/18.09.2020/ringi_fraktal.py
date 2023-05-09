import turtle

def fraktal(tase, pikkus):

    if tase == 0:
        return
    else:

        turtle.circle(pikkus)
        #turtle.circle(pikkus * tase)
        turtle.up()
        turtle.sety((pikkus * tase) * (-1))
        #turtle.forward(50)
        turtle.down()
        fraktal(tase-1, pikkus*tase)


turtle.speed(-1)
fraktal(5, 5)
turtle.exitonclick()