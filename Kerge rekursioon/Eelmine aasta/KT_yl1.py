# 11. a programmeerimine
# Rekursioon Kontrolltöö
# Nimi : Liisi Bergmann
# Kuupäev : 20.05,2020
# Klass : 11a


import turtle


def fraktaal(tase, joonepikkus):
    if tase == 0:
        return
    else:
        for i in range(3):
            turtle.forward(joonepikkus)
            turtle.left(120)
            fraktaal(tase - 1, joonepikkus * 0.6)
            turtle.left(180)
            turtle.forward(joonepikkus)
            turtle.right(60)

turtle.speed(-1)
fraktaal(3,50)
turtle.exitonclick()
