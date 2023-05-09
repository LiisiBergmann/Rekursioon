def toodete_hinnad(tooted, kombinatsioon, summa):

    if summa > 100:
        return 0

    if summa <= 100:
        return summa


    else:
        max(toodete_hinnad(tooted[1:], summa), max(toodete_hinnad(tooted[1:], kombinatsioon + [tooted[0]], summa + tooted[0] * 2 )), len(toodete_hinnad(tooted[1:], kombinatsioon + [tooted[0]], summa + tooted[0])))


print(toodete_hinnad([5, 10, 50, 20, 0.5, 0.75, 15], 100, 3))
