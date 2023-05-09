import turtle

nimi = turtle.Turtle()
ekraan = turtle.Screen()

def spiraal(nimi, pikkus):
    if pikkus > 0:
        nimi.forward(pikkus)
        nimi.right(90)
        spiraal(nimi, pikkus - 10)

spiraal(nimi, 200)
ekraan.exitonclick()
