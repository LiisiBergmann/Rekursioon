from turtle import *

import forward as forward


def ruudu_fraktal(tase, pikkus):

    if tase == 0:
        forward(pikkus)

    else:
        for i in range(4):
            forward(pikkus)
            left(90)

        forward(pikkus)
        right(90)

        for i in range(4):
            forward(pikkus)
            left(90)
        forward(pikkus)
        right(90)
        ruudu_fraktal(tase-1,pikkus*0.5)





speed(-1)
ruudu_fraktal(1,100)
exitonclick()