import turtle


def nurgajoon(n):
    nurgajoon2(n,n)
def nurgajoon2(n,a):
    if n != 0:
        turtle.fd(100)
        turtle.left(360/a)
        nurgajoon2(n-1, a)


nurgajoon(3)
turtle.exitonclick()