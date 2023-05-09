
from turtle import *

def spiraal(tase, pikkus):
    if tase == 0:
        return
    else:
        forward(pikkus)
        right(35)
        spiraal(tase-1, pikkus + 5)

speed(-1)
spiraal(30, 10)
exitonclick()