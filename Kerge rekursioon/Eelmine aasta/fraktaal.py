import turtle



def fraktal(tase, joone_pikkus):

    if tase == 0:
        turtle.forward(joone_pikkus)

    else:
        fraktal(tase-1, joone_pikkus)
        turtle.left(85)
        fraktal(tase-1, joone_pikkus)
        turtle.left(190)
        fraktal(tase-1, joone_pikkus)
        turtle.left(85)
        fraktal(tase-1, joone_pikkus)

def joone_pikkus(tase, pikkus):
    for i in range(tase):
        pikkus = pikkus - pikkus*0.30
    return pikkus

def nelja(tase):
    for i in range(4):
        fraktal(tase,joone_pikkus(tase,85))
        turtle.left(90)

        


turtle.speed(-1)
nelja(4)

turtle.exitonclick()