import turtle


def fraktal(joone_pikkus, tase):

    if tase == 0:
        turtle.forward(joone_pikkus)

    else:
        fraktal(joone_pikkus*0.4, tase-1)
        turtle.right(60)
        fraktal(joone_pikkus*0.4, tase-1)
        turtle.left(120)
        fraktal(joone_pikkus*0.4, tase-1)
        turtle.right(60)
        fraktal(joone_pikkus*0.4, tase-1)

for i in range(3):
    fraktal(180,3)
    turtle.left(120)

turtle.speed(-1)
turtle.exitonclick()